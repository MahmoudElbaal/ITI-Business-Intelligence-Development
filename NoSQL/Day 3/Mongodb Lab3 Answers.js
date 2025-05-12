// Provide the MongoDB code for enforcing JSON schema validation when creating a collection named "employees" with required fields "name," "age" (min. 18), and "department" (limited to ["HR," "Engineering," "Finance"]).

db.createCollection("employees", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      title : "Missing data",
      required: ["name", "age", "department"],
      properties: {
        name: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        age: {
          bsonType: "int",
          minimum: 18,
          description: "must be an integer and more than 18 and is required"
        },
        department: {
          enum: ["HR", "Engineering", "Finance"],
          description: "must be one of the specified values and is required"
        }
      }
    }
  }
});

///////////////////////////////////////////////////////////////////////////////////////////////

// Create new Database named Demo
// And Collections named trainningCenter1, trainningCenter2 
// Insert documents into trainningCenter1 collection contains (Use Variable named data as Array)
// _id , name as firstName lastName , age , address as array , status
// Using insert ONE from data Variable
// Using Same Variable (data) with same data and insert MANY into trainningCenter2 collection


use Demo

db.createCollection("trainningCenter1") ,
db.createCollection("trainningCenter2")


var data = [
  {
    _id: 1,
    name: {firstName: "Mahmoud",lastName: "Saied",
    age: 26,
    address: ["Cairo", "Egypt"],
    status: "Active"
    }
  },
  {
    _id: 2,
    name: {firstName: "Mahmoud",lastName: "Saied",
    age: 26,
    address: ["Cairo", "Egypt"],
    status: "Active"
  }
 }
];

db.trainningCenter1.insertOne(data);      // added all the documents in the var as 1 document with 1 object id.
db.trainningCenter2.insertMany(data)      // added all the documents in the var as it is.

db.trainningCenter1.find({})
db.trainningCenter2.find({})


///////////////////////////////////////////////////////////////////////////////////////////////

// Use find. explain function (find by age field) and mention scanning type 

db.trainningCenter1.find({ age: 26 }).explain("executionStats")  //COLLSCAN


///////////////////////////////////////////////////////////////////////////////////////////////

// Create index on created collection named it “IX_age” on age field  

db.trainningCenter1.createIndex({ age: 1 }, { name: "IX_age" })


///////////////////////////////////////////////////////////////////////////////////////////////

// Use find. explain view winning plan for index created (find by age field) and mention scanning type 

db.trainningCenter1.find({ age: 26 }).explain("executionStats")  //IXSCAN

///////////////////////////////////////////////////////////////////////////////////////////////

/* Create index on created collection named it “compound” on firstNsme and lastName 
    a. Try find().explain before create index and mention scanning type 
    b. Try find().explain after create index and mention scanning type*/
    
    db.trainningCenter1.find({ firstName: "Mahmoud", lastName: "Saied" }).explain("executionStats")    // before "COLLSCAN"
    
db.trainningCenter1.createIndex({ firstName: 1, lastName: 1 }, { name: "compound" })
  
db.trainningCenter1.find({ firstName: "Mahmoud", lastName: "Saied" }).explain("executionStats")        // after "IXSCAN"


///////////////////////////////////////////////////////////////////////////////////////////////

// Try deleteOne , deleteMany from any Collection 

db.trainningCenter1.deleteOne({ _id: 1 })
db.trainningCenter2.deleteMany({ status: "A" })

///////////////////////////////////////////////////////////////////////////////////////////////

// Drop Demo Database 

db.dropDatabase()

show dbs            /// to show if the db actually been dropped or not






























