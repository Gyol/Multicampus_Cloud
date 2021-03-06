use python_db


db.createCollection('articles')

show collections

db.articles.insertMany([
    { "_id" : ObjectId("512bc95fe835e68f199c8686"), "author" : "john", "score" : 80, "views" : 100 },
    { "_id" : ObjectId("512bc962e835e68f199c8687"), "author" : "john", "score" : 85, "views" : 521 },
    { "_id" : ObjectId("55f5a192d4bede9ac365b257"), "author" : "ahn", "score" : 60, "views" : 1000 },
    { "_id" : ObjectId("55f5a192d4bede9ac365b258"), "author" : "li", "score" : 55, "views" : 5000 },
    { "_id" : ObjectId("55f5a1d3d4bede9ac365b259"), "author" : "annT", "score" : 60, "views" : 50 },
    { "_id" : ObjectId("55f5a1d3d4bede9ac365b25a"), "author" : "li", "score" : 94, "views" : 999 },
    { "_id" : ObjectId("55f5a1d3d4bede9ac365b25b"), "author" : "ty", "score" : 95, "views" : 1000 }
    ])

db.articles.find()


db.articles.aggregate([
    {$match:{author:"john"}}])

// score >= 80
db.articles.aggregate([
    {$match:{score:{$gte:80}}}
])

// author = 'li' and score > 60
db.articles.aggregate([
    {$match:{
        author:"li",
        score:{$gt:60}
    }}
])

// select author, sum(score) as total from articles group by author
// having total >  100
db.articles.aggregate([
    {
        $group:{
            _id:"$author",
            total:{$sum:"$score"}
        }
    }, // 이거는 group by랑 관련된 중괄호이기 때문에 having 관련을 쓰려면 따로 열어줘야..
    {
        $match:{
            total:{$gt:100}
        }
    }
])

