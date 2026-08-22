# PREPSQL01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com

Write queries for the following Aggregations & Grouping operations based on the tables that we created and the data that we inserted.

### Task

Find the highest-priced product along with its name.

### Expected output

```
┌─────────────────┬──────────┐
│      name       │  price   │
├─────────────────┼──────────┤
│ Apple iPhone 15 │ 1099.989 │
└─────────────────┴──────────┘

```

### Tables
- Customers

```
┌─────────────┬─────────────┬──────────────────────┬────────────┬─────────────┐
│ customer_id │    name     │        email         │   phone    │   address   │
└─────────────┼─────────────┼──────────────────────┼────────────┼─────────────┘

```

- Products

```
┌────────────┬────────────────────┬─────────────┬────────┬────────────────┐
│ product_id │        name        │  category   │ price  │ stock_quantity │
└────────────┴────────────────────┴─────────────┴────────┴────────────────┘

```

- Orders

```
┌──────────┬─────────────┬────────────┬──────────────┬─────────────────┐
│ order_id │ customer_id │ order_date │ total_amount │ Remarks_if_any  │
└──────────┴─────────────┴────────────┴──────────────┴─────────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T13:21:02.330Z  

```sql
/* Write your query below this line*/
select name , price from products where price=(select max(price) from products)
```

---

[View on CodeChef](https://www.codechef.com/problems/PREPSQL01)