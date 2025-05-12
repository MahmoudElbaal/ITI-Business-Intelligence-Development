/////////////////////////////////////////////////////////////////////////////////
//Find documents where the "tags" field exists

db.inventory.find({tags:{$exists:true}})


/////////////////////////////////////////////////////////////////////////////////
//Find documents where the "tags" field does not contain values "ssl" or "security."

db.inventory.find({tags:{$nin:["ssl" , "security"]}})



/////////////////////////////////////////////////////////////////////////////////
//Find documents where the "qty" field is equal to 85.

db.inventory.find({qty:85})


/////////////////////////////////////////////////////////////////////////////////
//Find documents where the "tags" array contains all of the values [ssl, security] using the `$all` operator.

db.inventory.find({tags:{$all:["ssl", "security"]}})


/////////////////////////////////////////////////////////////////////////////////
//Find documents where the "tags" array has a size of 3.

db.inventory.find({tags:{$size:3}})



/////////////////////////////////////////////////////////////////////////////////
//Update the "item" field in the "paper" document, setting "size.uom" to "meter" and using the `$currentDate` operator.
// - Also, use the upsert option and change filter condition item:”paper”.
// - Use the `$setOnInsert` operator.
// - Try `updateOne`, `updateMany`, and `replaceOne`.

//update where item : "paper" , set size.uom >= meter
db.inventory.find({item:"paper"})
db.inventory.updateOne(
{ item : "paper" },
{ $set:{ "size.uom" : "meter" },
    $currentDate :{ lastmodified : true }})


db.inventory.updateOne(
{ item : "book" },
{ $set:{ "size.uom" : "meter" },
    $currentDate :{ lastmodified : true }},
    {upsert : true})


db.inventory.updateOne(
{ item : "book" },
{ $set:{ "size.uom" : "meter" },
    $currentDate :{ lastmodified : true },
    $setOnInsert: { condition : "good"}  // If inserting, set 'condition' to "good"
    },
    {upsert : true})



db.inventory.updateMany(
  { item: "book" },
  { $set: { "size.uom": "meter" }, 
    $currentDate: { lastModified: true }, 
    $setOnInsert: { condition: "good" } 
  },
  { upsert: true } )



db.inventory.replaceOne(
  { item: "book" }, 
  { item: "Pens", // new document structure
    size: { uom: "meter" }, 
    lastModified: new Date(), 
    condition: "good" },
  { upsert: true })



/////////////////////////////////////////////////////////////////////////////////
//Insert a document with incorrect field names "neme" and "ege," then rename them to "name" and "age."
db.inventory.insertOne(
{neme:"Mahmoud", ege:26}
)

db.inventory.updateOne(
{neme:"Mahmoud"},
{$rename:{"neme":"name", "ege":"age"}}
)

db.inventory.find({name:"Mahmoud"})


/////////////////////////////////////////////////////////////////////////////////
//Try to reset any document field using the `$unset` function.

db.inventory.find({})

db.inventory.updateOne(
{_id : 4},
{
    $unset : {address : ""}})


db.inventory.find({_id : 4})


/////////////////////////////////////////////////////////////////////////////////
//Try update operators like `$inc`, `$min`, `$max`, and `$mul` to modify document fields.


db.inventory.insertOne(
{item:"keyboard", qty:50 , price:110 })

db.inventory.find({item:"keyboard"})


db.inventory.updateOne(
  { item: "keyboard" },
  { $inc: { qty: 10 } } // increase qty by 10
)


db.inventory.updateOne(
  { item: "keyboard" },
  { $min: { price: 100 } } // minimum prcie 100
)



db.inventory.updateOne(
  { item: "keyboard" },
  { $max: { price: 120 } } // max price 120
)


db.inventory.updateOne(
  { item: "keyboard" },
  { $mul: { price: 1.2 } } // price mltiply  by 1.2
)

/////////////////////////////////////////////////////////////////////////////////
//Calculate the total revenue for product from sales collection documents within the date range '01-01-2020' to '01-01-2023' and then sort them in descending order by total revenue.
//Total Revenue=  Sum (Quantity * Price)

db.sales.find({})

db.sales.aggregate([
  {
    $match: {
      date: {
        $gte: ISODate("2020-01-01"),
        $lte: ISODate("2023-01-01")
      }
    }
  },
  {
    $group: {
      _id: "$product",
      totalRevenue: {
        $sum: { $multiply: ["$quantity", "$price"] } 
      }
    }
  },
  {
    $sort: { totalRevenue: -1 }
  }
])



/////////////////////////////////////////////////////////////////////////////////
//Calculate the average salary for employees for each department from the employee’s collection.
db.employees.find({})


db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      AVGSalary:{
        $avg: "$salary" }
    }
  }
])



/////////////////////////////////////////////////////////////////////////////////
db.likes.find({})


db.likes.aggregate([
  {$group: {_id: "$title",           
      maxLikes: { $max: "$likes" },  
      minLikes: { $min: "$likes" } 
    }
  }
])







