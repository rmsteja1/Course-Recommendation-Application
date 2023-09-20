import random



def courseListGenerator(specialization,startingSemester,startingYear,semesterCount,crossSpecialization,electives,conditionalAdmit):
    sem1 = []
    sem2 = []
    sem3 = []
    sem4 = []
    electiveArr = electives.split(',')

    divisionArr = [[3,3,3,2],[4,3,3,1],[3,4,3,1],[3,3,4,1]]
    courseDivision = random.choice(divisionArr)

    if specialization == 'Enterprise Software Technologies':
        choices = [1,2,3,4]
        choice = random.choice(choices)
        electiveDivision = [0,1]
        electiveSem = random.choice(electiveDivision)
        if courseDivision == divisionArr[0]:  
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 273', 'CMPE 275']
                sem2 = ['CMPE 255', 'CMPE 202', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==2:
                sem1 = ['CMPE 255', 'CMPE 272', 'CMPE 202']
                sem3 = ['CMPE 273', 'CMPE 275', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 273', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 275', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 273', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 275', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
        elif courseDivision == divisionArr[1]:
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 273', 'CMPE 255', 'CMPE 202']
                sem2 = ['CMPE 275', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 272', 'CMPE 273', 'CMPE 275', 'CMPE 202']
                sem2 = ['CMPE 255', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 273', 'CMPE 275', 'CMPE 202']
                sem2 = ['CMPE 255', electiveArr[1], electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 273', 'CMPE 275', 'CMPE 202']
                sem2 = ['CMPE 255',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[2]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 273', 'CMPE 275', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 273', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 275', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 273', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 275', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A',electiveArr[0], electiveArr[1] ]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 273', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 275', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[3]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 273', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 275', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 273', 'CMPE 275', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 273', 'CMPE 275',electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 273', 'CMPE 275','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']
            
    elif specialization == 'Cloud Computing and Virtualization':
        choices = [1,2,3,4]
        choice = random.choice(choices)
        electiveDivision = [0,1]
        electiveSem = random.choice(electiveDivision)
        if courseDivision == divisionArr[0]:  
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 281', 'CMPE 283']
                sem2 = ['CMPE 255', 'CMPE 202', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==2:
                sem1 = ['CMPE 255', 'CMPE 272', 'CMPE 202']
                sem3 = ['CMPE 281', 'CMPE 283', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 281', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 283', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 281', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 283', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
        elif courseDivision == divisionArr[1]:
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 281', 'CMPE 255', 'CMPE 202']
                sem2 = ['CMPE 283', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 272', 'CMPE 281', 'CMPE 283', 'CMPE 202']
                sem2 = ['CMPE 255', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 281', 'CMPE 283', 'CMPE 202']
                sem2 = ['CMPE 255', electiveArr[1], electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 281', 'CMPE 283', 'CMPE 202']
                sem2 = ['CMPE 255',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[2]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 281', 'CMPE 283', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 281', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 283', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 281', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 283', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A',electiveArr[0], electiveArr[1] ]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 281', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 283', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[3]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 281', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 283', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 281', 'CMPE 283', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 281', 'CMPE 283',electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 281', 'CMPE 283','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']

    elif specialization == 'Software Systems Engineering':
        choices285287 = [1,2,3,4,5]
        choice285287 = random.choice(choices285287)
        electiveDivision = [0,1]
        electiveSem = random.choice(electiveDivision)
        if courseDivision == divisionArr[0]:  
            if choice285287==1:
                sem1 = ['CMPE 202', 'CMPE 285', 'CMPE 287']
                sem2 = ['CMPE 255', 'CMPE 272', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice285287==2:
                sem1 = ['CMPE 255', 'CMPE 272', 'CMPE 202']
                sem3 = ['CMPE 285', 'CMPE 287', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice285287==3:
                sem1 = ['CMPE 202', 'CMPE 285', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 287', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice285287==4:
                sem1 = ['CMPE 202', 'CMPE 285', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 287', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice285287==5:
                sem1 = ['CMPE 202', 'CMPE 287', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 285', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
        elif courseDivision == divisionArr[1]:
            if choice285287==1:
                sem1 = ['CMPE 272', 'CMPE 285', 'CMPE 255', 'CMPE 202']
                sem2 = ['CMPE 287', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice285287==2:
                sem1 = ['CMPE 272', 'CMPE 285', 'CMPE 287', 'CMPE 202']
                sem2 = ['CMPE 255', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice285287==3:
                sem1 = ['CMPE 272', 'CMPE 285', 'CMPE 287', 'CMPE 202']
                sem2 = ['CMPE 255', electiveArr[1], electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice285287==4:
                sem1 = ['CMPE 272', 'CMPE 285', 'CMPE 287', 'CMPE 202']
                sem2 = ['CMPE 255',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice285287==5:
                sem1 = ['CMPE 272', 'CMPE 285', 'CMPE 287', 'CMPE 202']
                sem2 = ['CMPE 255',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[2]:
            if choice285287==1:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 285', 'CMPE 287', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice285287==2:
                sem1 = ['CMPE 202', 'CMPE 285', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 287', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice285287==3:
                sem1 = ['CMPE 202', 'CMPE 285', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 287', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A',electiveArr[0], electiveArr[1] ]
                sem4 = ['CMPE 295B']
            elif choice285287==4:
                sem1 = ['CMPE 202', 'CMPE 285', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 287', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice285287==5:
                sem1 = ['CMPE 202', 'CMPE 287', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 285', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[3]:
            if choice285287==1:
                sem1 = ['CMPE 202', 'CMPE 285', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 287', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice285287==2:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 285', 'CMPE 287', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice285287==3:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 285', 'CMPE 287',electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice285287==4:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 285', 'CMPE 287','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice285287==5:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 285', 'CMPE 287','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']


    elif specialization == 'Networking Software':
        choices = [1,2,3,4]
        choice = random.choice(choices)
        electiveDivision = [0,1]
        electiveSem = random.choice(electiveDivision)
        if courseDivision == divisionArr[0]:  
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 206', 'CMPE 207']
                sem2 = ['CMPE 255', 'CMPE 202', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==2:
                sem1 = ['CMPE 255', 'CMPE 272', 'CMPE 202']
                sem3 = ['CMPE 206', 'CMPE 207', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 206', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 207', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 206', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 207', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
        elif courseDivision == divisionArr[1]:
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 206', 'CMPE 255', 'CMPE 202']
                sem2 = ['CMPE 207', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 272', 'CMPE 206', 'CMPE 207', 'CMPE 202']
                sem2 = ['CMPE 255', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 206', 'CMPE 207', 'CMPE 202']
                sem2 = ['CMPE 255', electiveArr[1], electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 206', 'CMPE 207', 'CMPE 202']
                sem2 = ['CMPE 255',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[2]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 206', 'CMPE 207', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 206', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 207', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 206', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 207', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A',electiveArr[0], electiveArr[1] ]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 206', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 207', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[3]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 206', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 207', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 206', 'CMPE 207', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 206', 'CMPE 207',electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 206', 'CMPE 207','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']

    elif specialization == 'Data Science':
        choices256257 = [1,2,3,4,5]
        choice256257 = random.choice(choices256257)
        electiveDivision = [0,1]
        electiveSem = random.choice(electiveDivision)
        if courseDivision == divisionArr[0]:  
            if choice256257==1:
                sem1 = ['CMPE 255', 'CMPE 257', 'CMPE 258']
                sem2 = ['CMPE 272', 'CMPE 202', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice256257==2:
                sem1 = ['CMPE 255', 'CMPE 272', 'CMPE 202']
                sem3 = ['CMPE 257', 'CMPE 258', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice256257==3:
                sem1 = ['CMPE 272', 'CMPE 257', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 258', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice256257==4:
                sem1 = ['CMPE 272', 'CMPE 257', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 258', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice256257==5:
                sem1 = ['CMPE 272', 'CMPE 258', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 257', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
        elif courseDivision == divisionArr[1]:
            if choice256257==1:
                sem1 = ['CMPE 272', 'CMPE 257', 'CMPE 255', 'CMPE 202']
                sem2 = ['CMPE 258', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice256257==2:
                sem1 = ['CMPE 255', 'CMPE 257', 'CMPE 258', 'CMPE 202']
                sem2 = ['CMPE 272', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice256257==3:
                sem1 = ['CMPE 255', 'CMPE 257', 'CMPE 258', 'CMPE 202']
                sem2 = ['CMPE 272', electiveArr[1], electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice256257==4:
                sem1 = ['CMPE 255', 'CMPE 257', 'CMPE 258', 'CMPE 202']
                sem2 = ['CMPE 272',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice256257==5:
                sem1 = ['CMPE 255', 'CMPE 257', 'CMPE 258', 'CMPE 202']
                sem2 = ['CMPE 272',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[2]:
            if choice256257==1:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 257', 'CMPE 258', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice256257==2:
                sem1 = ['CMPE 202', 'CMPE 257', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 258', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice256257==3:
                sem1 = ['CMPE 202', 'CMPE 257', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 258', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A',electiveArr[0], electiveArr[1] ]
                sem4 = ['CMPE 295B']
            elif choice256257==4:
                sem1 = ['CMPE 202', 'CMPE 257', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 258', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice256257==5:
                sem1 = ['CMPE 202', 'CMPE 258', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 257', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[3]:
            if choice256257==1:
                sem1 = ['CMPE 202', 'CMPE 257', 'CMPE 255']
                sem2 = ['CMPE 272', 'CMPE 258', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice256257==2:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 257', 'CMPE 258', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice256257==3:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 257', 'CMPE 258',electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice256257==4:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 257', 'CMPE 258','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice256257==5:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 257', 'CMPE 258','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']

    elif specialization == 'Cybersecurity':
        choices = [1,2,3,4]
        choice = random.choice(choices)
        electiveDivision = [0,1]
        electiveSem = random.choice(electiveDivision)
        if courseDivision == divisionArr[0]:  
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 209', 'CMPE 279']
                sem2 = ['CMPE 255', 'CMPE 202', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==2:
                sem1 = ['CMPE 255', 'CMPE 272', 'CMPE 202']
                sem3 = ['CMPE 209', 'CMPE 279', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 209', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 279', crossSpecialization]
                if electiveSem == 0:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[0]]
                    sem4 = ['CMPE 295B', electiveArr[1]]
                else:
                    sem3 = ['CMPE 295A', 'CMPE 294', electiveArr[1]]
                    sem4 = ['CMPE 295B', electiveArr[0]]
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 209', 'CMPE 255']
                sem2 = ['CMPE 202', 'CMPE 279', electiveArr[1]]
                sem3 = [crossSpecialization, 'CMPE 294', 'CMPE 295A']
                sem4 = ['CMPE 295B', electiveArr[0]]
        elif courseDivision == divisionArr[1]:
            if choice==1:
                sem1 = ['CMPE 272', 'CMPE 209', 'CMPE 255', 'CMPE 202']
                sem2 = ['CMPE 279', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 272', 'CMPE 209', 'CMPE 279', 'CMPE 202']
                sem2 = ['CMPE 255', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A', electiveArr[1], electiveArr[0]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 272', 'CMPE 209', 'CMPE 279', 'CMPE 202']
                sem2 = ['CMPE 255', electiveArr[1], electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 272', 'CMPE 209', 'CMPE 279', 'CMPE 202']
                sem2 = ['CMPE 255',electiveArr[0],crossSpecialization]
                sem3 = ['CMPE 295A',electiveArr[1], 'CMPE 294']
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[2]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 209', 'CMPE 279', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 209', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 279', electiveArr[0], electiveArr[1]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294']
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 209', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 279', crossSpecialization, 'CMPE 294']
                sem3 = ['CMPE 295A',electiveArr[0], electiveArr[1] ]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 209', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 279', electiveArr[0], 'CMPE 294']
                sem3 = ['CMPE 295A',crossSpecialization, electiveArr[1]]
                sem4 = ['CMPE 295B']
        elif courseDivision == divisionArr[3]:
            if choice==1:
                sem1 = ['CMPE 202', 'CMPE 209', 'CMPE 272']
                sem2 = ['CMPE 255', 'CMPE 279', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==2:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 209', 'CMPE 279', crossSpecialization]
                sem3 = ['CMPE 295A', electiveArr[0], 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==3:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 209', 'CMPE 279',electiveArr[0]]
                sem3 = ['CMPE 295A', crossSpecialization, 'CMPE 294', electiveArr[1]]
                sem4 = ['CMPE 295B']
            elif choice==4:
                sem1 = ['CMPE 202', 'CMPE 255', 'CMPE 272']
                sem2 = ['CMPE 209', 'CMPE 279','CMPE 294']
                sem3 = ['CMPE 295A', crossSpecialization,electiveArr[0], electiveArr[1]]
                sem4 = ['CMPE 295B']
    return[sem1,sem2,sem3,sem4]
    