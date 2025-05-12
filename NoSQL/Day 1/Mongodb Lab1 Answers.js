//1 Create a Database named "ITI_Mongo". 
use ITI_Mongo

//////////////////////////////////////////////////////////////////////////
//2. Create a Collection named "Staff".
db.Staff

//////////////////////////////////////////////////////////////////////////
//3. Insert one document into the "Staff" collection: {_id, name, age, gender, department}.
db.Staff.insertOne({"name" : "Mahmoud", "age" : 26, "gender" : "male", "department" : "HR"})

//////////////////////////////////////////////////////////////////////////
// 4. Insert many documents into the "Staff" collection: 
//•    Object: {_id, name, age: 20, gender: "male", department} 
//•    Object: {_id, name, age: 25, gender: "female", managerName, department} 
//•    Object: {_id, name, age: 15, gender, DOB} 

db.Staff.insertMany([
  {
    "name": "",
    "age": 20,
    "gender": "male",
    "department": ""
  },
  {
    "name": "",
    "age": 25,
    "gender": "female",
    "managerName": "",
    "department": ""
  },
  {
    "name": "",
    "age": 15,
    "gender": "",
    "DOB": ""
  }
])


//////////////////////////////////////////////////////////////////////////
//5. Query to find data from the "Staff" collection: 

//1) Find all documents. 

db.Staff.find({})


//////////////////////////////////////////////////////////////////////////
//2) Find documents where gender is "male". 

db.Staff.find({"gender" : "male"})


//////////////////////////////////////////////////////////////////////////
//3) Find documents with age between 20 and 25.

db.Staff.find({"age": { $gte: 20, $lte: 25 }})


//////////////////////////////////////////////////////////////////////////
//4) Find documents where age is 25 and gender is "female"

db.Staff.find({"age" : 25, "gender" : "female"}) 
  

//////////////////////////////////////////////////////////////////////////
//5) Find documents where age is 20 or gender is "female". 

db.Staff.find({"$or" : [{"age" : 20}, {"gender" : "female"}]})


//////////////////////////////////////////////////////////////////////////
//6. Update one document in the "Staff" collection where age is 15, set the name to "new student". 

db.Staff.updateOne({"age" : 15} , {"$set" : {"name" : "newStudent"}})


//////////////////////////////////////////////////////////////////////////
//7. Update many documents in the "Staff" collection, setting the department to "AI".

db.Staff.updateMany({} ,{"$set" : {"department" : "AI"} } )


//////////////////////////////////////////////////////////////////////////
//8. Create a new collection called "test" and insert documents from Question 3. 

db.test.insertOne({"name" : "Mahmoud", "age" : 26, "gender" : "male", "department" : "HR"})


db.test.insertMany([
  {
    "name": "",
    "age": 20,
    "gender": "male",
    "department": ""
  },
  {
    "name": "",
    "age": 25,
    "gender": "female",
    "managerName": "",
    "department": ""
  },
  {
    "name": "",
    "age": 15,
    "gender": "",
    "DOB": ""
  }
])

db.test.find({})


//////////////////////////////////////////////////////////////////////////
//9. Try to delete one document from the "test" collection where age is 15. 

db.test.deleteOne({"age" : 15})

//////////////////////////////////////////////////////////////////////////
//10.  try to delete all male gender 

db.test.deleteMany({"gender" : "male"})

db.test.deleteMany({"$or" : [{"gender" : "male"}, {"name"  : "Ahmed" } ]  })  // OR Delete 


//////////////////////////////////////////////////////////////////////////
//11. Try to delete all documents in the "test" collection.
db.test.deleteMany({});
