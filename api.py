# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import os
# import ast

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


users_file = "./data/users.csv"


class Users(Resource):
    def get(self):
        data = pd.read_csv(users_file)
        data = data.to_dict()
        return {"data": data}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("userID", required=True)
        parser.add_argument("name", required=True)
        parser.add_argument("city", required=True)

        args = parser.parse_args()

        new_data = pd.DataFrame(
            {
                "userID": args["userID"],
                "name": args["name"],
                "city": args["city"],
            },
            index=[1],  # This line needs to be there but doesn't matter.
        )

        data = pd.read_csv(users_file)
        data = pd.concat([data, new_data], ignore_index=True)
        data.to_csv(users_file, index=False)
        data = pd.read_csv(users_file)
        return {"data": data.to_dict()}, 200


class Locations(Resource):
    pass


api.add_resource(Users, "/users")
api.add_resource(Locations, "/locations")

if not os.path.exists("./data/users.csv"):
    os.mkdir("data")
    with open(users_file, "w") as f:
        f.write("userID,name,city\n")

# driver function
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
