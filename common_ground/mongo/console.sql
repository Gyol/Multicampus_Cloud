// python_db 생성
use python_db

// people collection 생성
db.createCollection("people")

// isCapped()
db.people.isCapped()

// collection statis 정보
db.people.stats()

// emp collection을 생성하고 drop
db.createCollection("emp")

// emp -> employees로 rename
// db.emp.renameCollection('employees')
db.emp.drop()

// document(row) 한 개 insert
db.people.insertOne({user_id:"Gyol", age:"27", status:"Gorgeous"})

// 조회하기 select * from people
db.people.find()
db.people.find({})

// seelct _id, user_id, age from people
// 얘네는 select할때 조건을 먼저 앞에 줌 근데 지금 조건 없으니까 빈 column
// sql할때는 뭘찾는지 먼저 쓰고 뒤에 조건을 덧붙였잖아
db.people.find({},{user_id:1, age:1})

// select user_id, status from people
// 안 보고싶은 column이 있으면 0 입력 1은 보고싶은거
// 아예 암것도 안주면 자동으로 select * 처리
// 내가 만든 column은 안씀=안보임인데 _id는 얘가만든거라 안쓰면 자동보임
db.people.find({}, {user_id:1, status:1, _id:0})

// document를 여러 개 한번에 끼워넣는 insertMany
// 얘도 python이랑 똑같이 list가 있고 뭐 그래
db.people.insertMany([
    { user_id: "bcd002", age:25,status:"B" },
    { user_id: "bcd003", age:50,status:"A" },
    { user_id: "bcd004", age:35,status:"A" },
    { user_id: "abc001", age:28,status:"B" }
])
db.people.find()

// 원하는 document 갯수 지정
db.people.find().limit(2)

// select * from people where status = 'Gorgeous'
db.people.find({status:"Gorgeous"})

// select user_id, status from people where status = 'A'
db.people.find({status:"A"}, {user_id:1, status:1, _id:0})

// select * from people where status != 'A'
db.people.find({status:{$ne:'A'}})

// select user_id, status, age from people user_id != 'abc001'
db.people.find({user_id:{$ne:'abc001'}}, {_id:0, user_id:1, status:1, age:1})

// select * from people where status = 'A' and age = 50
db.people.find({status:'A', age:50})

// select * from people where status = 'A' or age = 50
db.people.find({$or: [{status:'A'}, {age:50}]})

// select status, age from people where status = 'A' or age = 50
db.people.find({$or: [{status:'A'}, {age:50}]}, {_id:0, status:1, age:1})

// select * from people where age > 25
db.people.find({age:{$gt:25}})

// select * from people where age > 25 and age <= 50
db.people.find({age:{$gt:25, $lte:50}})

// select * from people where age in (25, 50)
db.people.find({age:{$in:[25, 50]}})

// status = 'C', user_id만 포함한 document 추가 (insertOne)
db.people.insertOne({user_id:'dunno', status:'C'})

// status가 A이거나 C인것 찾기
db.people.find({$or: [{status:'A'}, {status:'C'}]})

// select * from people where age not in (5, 25)
db.people.find({age:{$nin:[5, 25]}})

// select * from people where user_id like '%cd%'
db.people.find({user_id:{$regex:/cd/}})

// select * from people where user_id like 'bc%'
db.people.find({user_id:{$regex:/^bc/}})

// select * from people where user_id like '%01'
db.people.find({user_id:{$regex:/01$/}})

// select * from people status = 'A' order by user_id asc
db.people.find({status:'A'}).sort({user_id:1})

// select user_id, age, status from people status = 'A' order by age desc
db.people.find({status:'A'}, {_id:0, user_id:1, age:1, status:1}).sort({age:1})

// select user_id, age from people where user_id like %cd% and age > 40
// order by user_id asc
db.people.find({user_id:{$regex:/cd/}, age:{$gt:40}},
                {user_id:1, age:1}).sort({user_id:-1})

// select user_id, status, age from people
// where age >= 25 and age <= 45
// and status in ('A', 'B')
db.people.find({age:{$gte:25, $lte:45}, status:{$in:['A','B']}}, {_id:0})


// select ccount(*) from people
db.people.count()

// select count(*) from people where age>30
// 이 경우에는 count안에 find쓰듯이 조건을 주면 도빈디ㅏ
db.people.count({age:{$gt:30}})

// age 필드의 값이 존재하는 row count
db.people.count({age:{$exists:true}})

// select distinct(status) from people
db.people.aggregate([{$group:{_id:"$status"}}])
db.people.findOne({age:{$gte:25}})

db.people.find().limit(3).skip(1)

// updateMany
// update people set status = 'C' where age>= 45
db.peple.updateMany({age:{$gte:45}}, {$set:{status:'C'}})

// update people set age = age+10 where status = 'B'
db.people.updateMany({status:'B'}, {$inc:{age:10}})

// updateOne
// update people set age = 100 where user_id = 'bcd001'
db.people.updateOne({user_id:'bcd001'}, {$set:{age:100}})

// update people set age = age+7 where status = 'B'
db.people.updateOne({status:'B'}, {$inc:{age:7}})

// delete from people where status = 'C'
db.people.deleteMany({status:'C'})

db.people.find()

db.people.updateMany({status:'B'},{$set:{size:100}})

