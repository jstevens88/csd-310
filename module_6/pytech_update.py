#Imports
from pymongo import MongoClient

#
#   Title: mongodb_test.py
#   Author: Jacob Stevens 
#   Date: 15 April 2022
#   Description: Test program for updating the students documents in the pytech collection of our AtlasDB Database


# MongoDB connection string
URI = "mongodb+srv://admin:admin@mycluster.w4rfd.mongodb.net/pytech?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"

# connect to the MongoDB cluster
client = MongoClient(URI)

# connect pytech database
db = client.pytech

# get the students collection
students = db.students

# find all students in the collection
student_list = students.find({})

# display message
print("\n**** DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY ****")

# loop over the collection and output the results
for item in student_list:
    print("\tStudent ID: " + item["student_id"] + "\n\tFirst Name: " + item["first_name"] + "\n\tLast Name: " + item["last_name"] + "\n")

update_student = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Thermopolopolis VI"}})

thorin = students.find_one({"student_id": "1007"})

# display message
print("\n****DISPLAYING STUDENT DOCUMENT 1007****")

# output the updated document to the terminal window
print("\tStudent ID: " + thorin["student_id"] + "\n\tFirst Name: " + thorin["first_name"] + "\n\tLast Name: " + thorin["last_name"] + "\n")

# exit message 
input("\n\nEnd of program, press any key to continue...")