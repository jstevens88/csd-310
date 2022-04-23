#Imports
from pymongo import MongoClient

#
#   Title: pytech_delete.py
#   Author: Jacob Stevens 
#   Date: 15 April 2022
#   Description: Test program for deleting the students documents in the pytech collection of our AtlasDB Database


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
print("\n****DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY****")

# loop over the collection and output the results
for item in student_list:
    print("\tStudent ID: " + item["student_id"] + "\n\tFirst Name: " + item["first_name"] + "\n\tLast Name: " + item["last_name"] + "\n")

# create new entry to insert into database
new_doc = {
    "student_id": "1010",
    "first_name": "Jenessica",
    "last_name": "Myers"
}
# insert new_doc and store the _id in variable
new_doc_id = students.insert_one(new_doc).inserted_id

# insert statements with output
print("\n****INSERT STATEMENTS****")
print("Inserted student record into the students collection with document_id " + str(new_doc_id))

# call the find_one() method by student_id 1010
student_find_doc = students.find_one({"student_id": "1010"})

# display results
print("\n****DISPLAYING NEW STUDENT DOC****")
print("\tStudent ID: " + student_find_doc["student_id"] + "\n\tFirst Name: " + student_find_doc["first_name"] + "\n\tLast Name: " + student_find_doc["last_name"] + "\n")

# call the delete_one() method to remove the student_find_doc
deleted_student_find_doc = students.delete_one({"student_id": "1010"})


# find all students in the collection
new_student_list = students.find({})

# display message
print("\n****DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY AFTER delete_one()****")

# loop over the new collection and output the results
for doc in new_student_list:
    print("\tStudent ID: " + doc["student_id"] + "\n\tFirst Name: " + doc["first_name"] + "\n\tLast Name: " + doc["last_name"] + "\n")

# exit message
input("\n\n  End of program, press any key to continue...")