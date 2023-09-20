from courseDict import courseDictNew as courseDictionary
from courseCodeDict import courseCodesDict as courseCodesDictionary
#from flask import request, make_response, jsonify
from yearsDict import yearsDict
from semestersDict import semestersDict
import joblib
import pandas as pd
import random
from application import db
from coursePlanWithoutPre import courseListGenerator


def courseAvailabilityPredictor(courseCode,year,semester):
    print(courseCode,year,semester)
    rf_reg_new =joblib.load("./application/rf_reg_new1.pkl")
    df=pd.read_excel('./application/avg_df1.xlsx')
    df = df.drop('Unnamed: 0', axis=1)
    if courseCode not in courseCodesDictionary:
         return random.uniform(0.1, 1)
    COURSE_CODE = courseCodesDictionary[courseCode]
    COURSE_NAME = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'COURSE_NAME'].values[0]
    SECTION_NUMBER = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'SECTION_NUMBER'].values[0]
    UNITS = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'UNITS'].values[0]
    CLASS_TYPE = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'CLASS_TYPE'].values[0]
    MEETING_DAYS = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'MEETING_DAYS'].values[0]
    CLASS_HOURS = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'CLASS_HOURS'].values[0]
    INSTRUCTOR = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'INSTRUCTOR'].values[0]
    #YEAR = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'YEAR'].values[0]
    YEAR=yearsDict[year]
    #SEMESTER = df.loc[df['COURSE_CODE'] == COURSE_CODE, 'SEMESTER'].values[0]
    SEMESTER=semestersDict[semester]
    single_course_df = pd.DataFrame({'COURSE_CODE': [COURSE_CODE], 
                                    'COURSE_NAME': [COURSE_NAME],
                                    'SECTION_NUMBER': [SECTION_NUMBER],
                                    'UNITS': [UNITS],
                                    'CLASS_TYPE': [CLASS_TYPE],
                                    'MEETING_DAYS': [MEETING_DAYS],
                                    'CLASS_HOURS': [CLASS_HOURS],
                                    'INSTRUCTOR': [INSTRUCTOR],
                                    'YEAR': [YEAR],
                                    'SEMESTER': [SEMESTER]})

    # use the trained random forest regressor model to predict SEATS_AVAILABLE for the single course
    single_pred = rf_reg_new.predict(single_course_df.drop('CLASS_HOURS', axis=1))
    # print(single_pred)
    x = 0
    for i,j in courseDictionary[COURSE_CODE].items():
    #     print(i)
        if(i>=single_pred):
    #         print(course_dict[COURSE_CODE][i])
            x=i
            break
        x=i
    predictedValue=courseDictionary[COURSE_CODE][x]
    #print(predictedValue)
    # if courseCode!="CMPE 295A" and courseCode!="CMPE 295B" and courseCode predictedValue==1.0:
    #     predictedValue=random.uniform(0.5, 0.9)
    return predictedValue

def findCoreCourses(degree):
    coreCourses=db.degreerequirement.find(
        {"Degree": degree},
        {"_id":0,"coreRequirements.courseName":1,"coreRequirements.courseCode":1}
    )
    coreCourseDict={}
    for course in coreCourses[0]["coreRequirements"]:
        courseName=course['courseName']
        courseCode=course['courseCode']
        coreCourseDict[courseCode]=courseName
    return coreCourseDict

def findSpecializations(mainspecialization,degree):
    specializationCourses=db.degreerequirement.find({
        "Degree":degree,
        "specialization.choiceOfSpecialization":mainspecialization
    },
    {"_id":0,"specialization.coreCourses.courseName":1,"specialization.choiceOfSpecialization":1,"specialization.coreCourses.courseCode":1}
    )
    specializationCoursesDict={}

    for document in specializationCourses:
        for course in document["specialization"]:
            if course["choiceOfSpecialization"] == mainspecialization:
                for spCourse in course["coreCourses"]:
                    courseName=spCourse["courseName"]
                    courseCode=spCourse["courseCode"]
                    specializationCoursesDict[courseCode]=courseName
    return specializationCoursesDict
            
def findElectives(electivesString):
    electives=electivesString.split(",")
    electivesDict={}
    for course in electives:
        electiveList=db.coursecatalog.find(
            {"coursecode":course},
            {"_id":0,"coursecode":1,"coursename":1}
        )
        electivesDict[electiveList[0]["coursecode"]]=electiveList[0]["coursename"]
    return electivesDict

def alterOutputArray(outputArray,previousSemester,previousYear):
    if previousSemester=="spring":
        for record in outputArray[8:11]:
            record[4]="fall"
    elif previousSemester=="fall":
        for record in outputArray[8:11]:
            temp=int(previousYear)
            temp+=1
            record[3]=str(temp)
            record[4]="spring"
    return outputArray


def seCoursePredictionConditional(specialization,startingSemester,startingYear,semesterCount,crossSpecializations,electives,conditionalAdmit):
    suggestionList=[]
    output=[]
    coreCoursesDict=findCoreCourses("Software Engineering")
    specializationsDict=findSpecializations(specialization,"Software Engineering")
    electivesDict=findElectives(electives)
    crossSpecializationDict=findElectives(crossSpecializations)
    
    if conditionalAdmit=='yes':
        output=[1.0,1.0,1.0]
        suggestionList.append("CMPE 180A")
        suggestionList.append("CMPE 180B")
        suggestionList.append("CMPE 180C")
        suggestionList.append("CMPE 272")
        suggestionList.append("CMPE 202")
        suggestionList.append("CMPE 255")
        suggestionList.append(list(specializationsDict.keys())[0])
        suggestionList.append(list(specializationsDict.keys())[1])
        suggestionList.append(list(crossSpecializationDict.keys())[0])
        suggestionList.append("CMPE 294")
        suggestionList.append("CMPE 295A")
        
        y=[0,1]
        x=random.choice(y)
        if x == 0:
            suggestionList.append(list(electivesDict.keys())[0])
            suggestionList.append(list(electivesDict.keys())[1])
            suggestionList.append("CMPE 295B")
        else:
            suggestionList.append(list(electivesDict.keys())[1])
            suggestionList.append(list(electivesDict.keys())[0])
            suggestionList.append("CMPE 295B")
        
        outputWithCourseNames=[["CMPE 180A","Data Structures and Algorithms in C++",startingYear,startingSemester,1.0],["CMPE 180B", "Database Systems",startingYear,startingSemester,1.0],["CMPE 180C","Operating Systems Design",startingYear,startingSemester,1.0]]
        index=3
        count=3
        currentSemester=startingSemester
        currentYear=startingYear
        for course in suggestionList[3::]:
            courseCatalog=db.coursecatalog.find(
                {"coursecode":course},
            )
            tempArray=[]
            tempArray.append(courseCatalog[0]["coursecode"])
            tempArray.append(courseCatalog[0]["coursename"])
            #tempArray.append(courseAvailabilityPredictor(courseCatalog[0]["coursecode"],currentYear,currentSemester))
            outputWithCourseNames.append(tempArray)
            index+=1
            if count==4 or count ==8:
                if currentSemester=="fall":
                    currentSemester="spring"
                    currentYear=int(currentYear)+1
                    currentYear=str(currentYear)
                elif currentSemester=="spring":
                    currentSemester="fall"
            tempArray.append(currentYear)
            tempArray.append(currentSemester)
            tempArray=[]
            count+=1
        a=[0,1]
        b=random.choice(a)
        previousSemester=outputWithCourseNames[7][2]
        previousYear=outputWithCourseNames[7][3]
        print(b)
        if b==0:
            startIndex=11
            outputWithCourseNames=alterOutputArray(outputWithCourseNames,previousSemester,previousYear)
            previousSemester=outputWithCourseNames[10][3]
            previousYear=outputWithCourseNames[10][2]
        elif b==1:
            startIndex=12
            outputWithCourseNames=alterOutputArray(outputWithCourseNames,previousSemester,previousYear)
            previousSemester=outputWithCourseNames[11][3]
            previousYear=outputWithCourseNames[11][2]
        for element in outputWithCourseNames[startIndex::]:
            if previousSemester=='spring':
                element[3]='fall'
            elif previousSemester=='fall':
                element[3]='spring'
                temp=int(previousYear)
                temp+=1
                element[2]=str(temp)
        for record in outputWithCourseNames[3::]:
            courseCode=record[0]
            courseYear=record[2]
            courseSemester=record[3]
            record.append(round(courseAvailabilityPredictor(courseCode,courseYear,courseSemester),2))
        #Making master project courses 1
        outputWithCourseNames[-4][4]=1.0
        outputWithCourseNames[-1][4]=1.0


        return outputWithCourseNames


def seCoursePredictionNonConditional(specialization,startingSemester,startingYear,semesterCount,crossSpecializations,electives,conditionalAdmit):
    coursesList=courseListGenerator(specialization,startingSemester,startingYear,semesterCount,crossSpecializations,electives,conditionalAdmit)
    currentSem=startingSemester
    currentYear=startingYear
    finalList=[]
    for Semcourses in coursesList:
        for course in Semcourses:
            tempArray=[]
            courseCatalog=db.coursecatalog.find(
                {"coursecode":course},
            )
            tempArray.append(courseCatalog[0]["coursecode"])
            tempArray.append(courseCatalog[0]["coursename"])
            tempArray.append(currentYear)
            tempArray.append(currentSem)
            if course=="CMPE 295A" or course=="CMPE 295B" or course=="CMP 299A" or course=="CMPE 299B":
                tempArray.append(1.0)
            else:
                percentage=round(courseAvailabilityPredictor(course,currentYear,currentSem),2)
                if percentage>0.1:
                    tempArray.append(percentage)
                else:
                    tempArray.append(0.10)
            finalList.append(tempArray)
        if currentSem=='fall':
            currentSem='spring'
            currentYear=int(currentYear)+1
            currentYear=str(currentYear)
        elif currentSem=='spring':
            currentSem='fall'
    return finalList 








      

        

        
    