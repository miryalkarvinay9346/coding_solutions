/* Write your query below this line*/
select name , price from products where price=(select max(price) from products)