use python_db

db.createCollection("orders")

show collections

db.orders.deleteMany({})

db.orders.insertMany([
        {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'A',
      price: 100,
      items: [ { sku: "xxx", qty: 25, price: 1 },
               { sku: "yyy", qty: 25, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'A',
      price: 500,
      items: [ { sku: "xxx", qty: 25, price: 1 },
               { sku: "yyy", qty: 25, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'B',
      price: 130,
      items: [ { sku: "jkl", qty: 35, price: 2 },
               { sku: "abv", qty: 35, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'B',
      price: 250,
      items: [ { sku: "jkl", qty: 25, price: 2 },
               { sku: "abv", qty: 25, price: 1 } ]
    },
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-01-02T17:04:11.102Z"),
      status: 'A',
      price: 130,
      items: [ { sku: "xxx", qty: 15, price: 1 },
               { sku: "yyy", qty: 15, price: 1 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'C',
      price: 70,
      items: [ { sku: "jkl", qty: 45, price: 2 },
               { sku: "abv", qty: 45, price: 3 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'A',
      price: 150,
      items: [ { sku: "xxx", qty: 35, price: 4 },
               { sku: "yyy", qty: 35, price: 5 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'B',
      price: 20,
      items: [ { sku: "jkl", qty: 45, price: 2 },
               { sku: "abv", qty: 45, price: 1 } ]
    },
    {
      cust_id: "abc456",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'B',
      price: 20,
      items: [ { sku: "jkl", qty: 45, price: 2 },
               { sku: "abv", qty: 45, price: 1 } ]
    },
    {
      cust_id: "abc780",
      ord_date: ISODate("2012-02-02T17:04:11.102Z"),
      status: 'B',
      price: 260,
      items: [ { sku: "jkl", qty: 50, price: 2 },
               { sku: "abv", qty: 35, price: 1 } ]
    }
])

db.orders.find()

// 1. select count(*) as count from orders
db.orders.aggregate([
    {
        $group:{
            _id:null, // ~별 에 대한 조건이 없으니까.. 그런게 있으면 _id에 조건적어줘야해
            count:{$sum:1} // 이건 count한걸 보여줘라~ 하는거
        }
    }
])


// select sum(price) as total
db.orders.aggregate([
    {
        $group:{
            _id:null,
            total:{$sum:"$price"}
        }
    }
])

// select cust_id, sum(price) as total from orders group by cust_id
db.orders.aggregate([
    {
        $group:{
            _id:"$cust_id",
            total:{$sum:"$price"}
        }
    }
])

// select cust_id, sum(price) as total from orders group by cust_id
// order by total desc
db.orders.aggregate([
    {
        $group:{
            _id:"$cust_id",
            total:{$sum:"$price"}
        }
    }, // 여기까지 group by 였구요 아래부터는 order by 관련 중괄호에요
    {
        $sort: {total:-1} // -1은 descending 1은 ascending
    }
])

// select cust_id, ord_date, sum(price) as total
// from orders group by cust_id, ord_date
db.orders.aggregate([
    {
        $group:{
            _id:{ // select에 붙은 조건이 여러개니까 중괄호 열어줘
                cust_id:"$cust_id", // cust_id:이거는 표시명 :"$"붙은건 실제 table에 있는 이름
                ord_date:{$dateToString: { format: "%Y-%m-%d", date: "$ord_date" }}
            },
            total:{$sum:"$price"}
        }
    }
])

// select cust_id, count(*) from orders group by cust_id
// having count(*) > 1
// 그니까 cust_id가 1개 이상인애들을 모아서 각 몇명인지 보여달라는거잖아?
db.orders.aggregate([
    {
        $group:{
            _id:"$cust_id",
            count:{$sum:1}
        }
    },
    {
        $match:{count:{$gt:1}}
    }
])

// select status, count(*) from orders group by status
db.orders.aggregate([
    {
        $group:{
            _id:"status",
            count:{$sum:1}
        }
    }
])

// select status, sum(price) as total from orders group by status
db.orders.aggregate([
    {
        $group:{
            _id:"status",
            total:{$sum:"$price"}
        }
    }
])

// select cust_id, ord_date, sum(price) as total
// from orders group by cust_id, ord_date
// having total > 250
db.orders.aggregate([
    {
        $group:{
            _id:{ // select에 붙은 조건이 여러개니까 중괄호 열어줘
                cust_id:"$cust_id", // cust_id:이거는 표시명 :"$"붙은건 실제 table에 있는 이름
                ord_date:{$dateToString: { format: "%Y-%m-%d", date: "$ord_date" }}
            },
            total:{$sum:"$price"}
        }
    },
    {
        $match:{total:{$gt:250}}
    }
])

// select cust_id, sum(price) as total from orders
// where status = 'A'
// group by cust_id
db.orders.aggregate([
    {
        $match:{status:'B'} // match라고 무조건 뒤에 주는건 아니고 where역할이니까 먼저..
    },
    {
        $group:{
            _id:"$cust_id",
            total:{$sum:"$price"}
        }
    }
])

// select cust_id, ord_date, sum(price) as total
// from orders where status = 'B'
// group by cust_id, ord_date
db.orders.aggregate([
    {
        $match:{status:'B'}
    },
    {
        $group:{
            _id:{
                cust_id:"$cust_id",
                ord_date:{$dateToString: { format: "%Y-%m-%d", date: "$ord_date" }},
            },
            total:{$sum:"$price"}
        },
    }
])

