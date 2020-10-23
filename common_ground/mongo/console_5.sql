use python_db

db.createCollection("items")

show collections

/*
select cust_id, sum(li.qty) as qty
from orders o, order_lineitem li
where o_id= li.order_ld
group by cust_id
*/
db.orders.aggregate([
    {
        $unwind:"$items"
    },
    {
        $group:{
            _id:"$cust_id",
            qty:{$sum:"$items.qty"}
        }
    }
])

/*
select count(*)
from(
    select cust_id, ord_date
    from orders
    group by cust_id, ord_date
    ) as d
*/
db.orders.aggregate([
    {
        $group:{
            _id:{cust_id:"$cust_id",
                ord_date:{$dateToString: { format: "%Y-%m-%d", date: "$ord_date" }}
            }
        }
    }, // 이건 괄호안의 것에 대한 group by
    {
        $group:{
            _id:null,
            count:{$sum:1}
        }
    } // 이건 그 바깥 것에 대한 group by
])





db.items.insertMany([
    { "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : ISODate("2014-03-01T08:00:00Z") },
    { "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : ISODate("2014-03-01T09:00:00Z") },
    { "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 10, "date" : ISODate("2014-03-15T09:00:00Z") },
    { "_id" : 4, "item" : "xyz", "price" : 5, "quantity" : 20, "date" : ISODate("2014-04-04T11:21:39.736Z") },
    { "_id" : 5, "item" : "abc", "price" : 10, "quantity" : 10, "date" : ISODate("2014-04-04T21:23:13.331Z") }
])

db.items.find()
db.items.aggregate([
    {
        $group:{
            _id:{year:{$year:"$date"}, month:{$month:"$date"}, day:{$dayOfMonth:"$date"}},
            totalPrice:{$sum:{$multiply:["$price","$quantity"]}},
            avgQuantity:{$avg:"$quantity"},
            count:{$sum:1}
        }
    }
])


db.createCollection("inventory")
db.inventory.insertOne({ "_id" : 1, "item" : "ABC1", sizes: [ "S", "M", "L"] })
db.inventory.find()
db.inventory.aggregate([
    {
        $unwind:"$sizes"
    }
])