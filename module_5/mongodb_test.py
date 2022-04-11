#Imports
from pymongo import MongoClient

#
#   Title: mongodb_test.py
#   Author: Jacob Stevens
#   Date: 10 April 2022
#   Description: Test program for connecting to a
#                 MongoDB Atlas cluster


# MongoDB connection string
URI = "mongodb+srv://admin:admin@mycluster.w4rfd.mongodb.net/pytech?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"

# connect to the MongoDB cluster
client = MongoClient(URI)

# connect pytech database
db = client.pytech

# show the connected collections
print("\n -- Pytech Collection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press any key to exit... ")
