import pymongo

# Connect to MongoDB server (e.g., local or remote)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or switch to a database
db = client["school"]

# Create or switch to a collection
students_collection = db["students"]

students_collection.drop()

#Inserting a single document
student = {"name": "John", "age": 21, "courses": ["Math", "CS"]}
students_collection.insert_one(student)

# Insert multiple documents
students = [
    {"name": "Alice", "age": 22, "courses": ["Math", "Physics"]},
    {"name": "Bob", "age": 23, "courses": ["Biology", "Chemistry"]}
]
students_collection.insert_many(students)

# Find one document
student = students_collection.find_one({"name": "John"})
print(student)

# Find multiple documents
for student in students_collection.find({"age": {"$gt": 21}}):
    print(student)

# Update one document
students_collection.update_one({"name": "John"}, {"$set": {"age": 22}})

# Update multiple documents
students_collection.update_many({"age": {"$lt": 22}}, {"$set": {"status": "Undergraduate"}})

# Delete one document
students_collection.delete_one({"name": "John"})

# Delete multiple documents
students_collection.delete_many({"age": {"$lt": 22}})

# Sort by age (ascending)
for student in students_collection.find().sort("age", 1):
    print(student)

# Limit to 5 results
for student in students_collection.find().limit(5):
    print(student)

#Creating an index on name field in students collection (table).
students_collection.create_index([("name", pymongo.ASCENDING)])


#Using try-except blocks.
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["school"]
    students_collection = db["students"]
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s") % e



