use mydb

for(i=1;i<=1388940;i++)
{
  db.testIndex.insert({"ssn":i,"district":"Calcutta","state":"WB" })
}

db.testIndex.count()
db.testIndex.explain().find()

db.testIndex.find({"ssn":{$lt:170}})

db.testIndex.find({"ssn":170})

db.testIndex.find({"_id":ObjectId("5b2365d049042adf926b851a")})

db.testIndex.createIndex({"ssn":-1})

db.testIndex.find({"ssn":{$lt:170}})

db.testIndex.find({"ssn":17450})



