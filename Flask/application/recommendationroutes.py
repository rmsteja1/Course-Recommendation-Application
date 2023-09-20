from application import app, db
from flask import request,jsonify
import bson.json_util as json_util
from flask_cors import cross_origin
import jwt
from functools import wraps




def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
            current_user = db.users.find_one({"email": data["email"]})
            if(current_user == None):
                return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        except Exception as e:
            print(e)
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated

@app.route("/api/v1/getRecommendationHistory",methods=["GET"])
@cross_origin(support_credentials=True)
@token_required
def getRecommendationHistory(current_user):

    try:
        userId = request.args.get("userId")
        semesterRecommendation = db.recommendationhistory.find({"userId":userId,"type":"SEMESTER"})
        semester = []
        for data in semesterRecommendation:
            semester.append(data)
        masterRecommendation = db.recommendationhistory.find({"userId":userId,"type":"MASTER"})
        master = []
        for data in masterRecommendation:
            master.append(data)
        response = {
            "semester":semester,
            "master":master
        }
        return json_util.dumps(response) , 200
    except Exception as e:
        print(e)
        return "Server down. Please try again!" , 500
    
@app.route("/api/v1/getDepartmentInfo",methods=["GET"])
@cross_origin(support_credentials=True)
@token_required
def getDepartmentInfo(current_user):
    try:
        department = request.args.get("department")
        degree = request.args.get('degree')
        departmentInfo = db.degreerequirement.find_one({"DeptName":department,"Degree":degree})

        if department == "Computer Science":
            rawelectives = db.coursecatalog.find({"department":department,"elective":1})
            
        elif department == "Computer Engineering":
            rawelectives = db.coursecatalog.find({"department":department})

        electives = []
        for elec in rawelectives:
            electives.append(elec)
        departmentInfo["electives"]=electives
        return json_util.dumps(departmentInfo), 200

    except Exception as e:
        print(e)
        return "Server down. Please try again!" , 500
    
@app.route("/api/v1/createRecommendationHistory",methods=["POST"])
@cross_origin(support_credentials=True)
def createRecommendationHistory():
    try:
        json = request.json
        db.recommendationhistory.insert_one(json);
        return "Insertion Successful", 200

    except Exception as e:
        print(e)
        return "Server down. Please try again!" , 500