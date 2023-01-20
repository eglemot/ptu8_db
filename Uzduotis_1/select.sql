-- CREATE TABLE status (
-- id INTEGER PRIMARY KEY NOT NULL,
-- name VARCHAR(30));

-- CREATE TABLE order_ (
-- id INTEGER PRIMARY KEY NOT NULL,
-- customer_id INTEGER,
-- date_ VARCHAR(20),
-- status_id INTEGER,
-- FOREIGN KEY (customer_id) REFERENCES customer (id),
-- FOREIGN KEY (status_id) REFERENCES status (id));

-- CREATE TABLE product_order (
-- order_id INTEGER,
-- product_id INTEGER,
-- quantity INTEGER,
-- FOREIGN KEY (order_id) REFERENCES order_ (id),
-- FOREIGN KEY (product_id) REFERENCES product (id));

-- CREATE TABLE product (
-- id INTEGER PRIMARY KEY NOT NULL,
-- name VARCHAR(50),
-- price DECIMAL(10,2));

-- INSERT INTO customer (f_name, l_name, email) VALUES ("Gintas", "Gintauskas", "gintox@rol.com");
-- INSERT INTO customer (f_name, l_name, email) VALUES ("Rita", "Ritauske", "ritux@rol.com");
-- INSERT INTO customer (f_name, l_name, email) VALUES ("Timas", "Timauskas", "timac@rol.com");
select * from customer;

-- INSERT INTO product_order (order_id, product_id, quantity) VALUES (1,1,30);
-- INSERT INTO product_order (order_id, product_id, quantity) VALUES (2,2,40);
-- INSERT INTO product_order (order_id, product_id, quantity) VALUES (3,3, 200);
-- INSERT INTO product_order (order_id, product_id, quantity) VALUES (4,4,300);
-- INSERT INTO product_order (order_id, product_id, quantity) VALUES (5,5,100);
-- INSERT INTO product_order (order_id, product_id, quantity) VALUES (6,2,2);


select * from product_order;

-- insert INTO product (id, name, price) VALUES (not null, "arbuzas", 4.20);
-- insert INTO product (id, name, price) VALUES (not null, "stalas", 400.50);
-- insert INTO product (id, name, price) VALUES (not null, "vazonas", 67.30);

select * from product;

-- insert INTO status (id, name) VALUES (1, "Patvirtintas");
-- insert INTO status (id, name) VALUES (2, "Vykdomas");
-- insert INTO status (id, name) VALUES (3, "Ivykdytas");
-- insert INTO status (id, name) VALUES (4, "Atmestas");
SELECT * from status;

-- INSERT INTO order_ (customer_id, status_id, date_) VALUES (1,1, "2023-01-02");
-- INSERT INTO order_ (customer_id, status_id, date_) VALUES (2,2, "2023-01-03");
-- INSERT INTO order_ (customer_id, status_id, date_) VALUES (3,1, "2023-01-05");
-- INSERT INTO order_ (customer_id, status_id, date_) VALUES (4,3, "2023-01-10");
-- INSERT INTO order_ (customer_id, status_id, date_) VALUES (5,3, "2023-01-18");
-- INSERT INTO order_ (customer_id, status_id, date_) VALUES (2,3, "2023-01-18");
SELECT * FROM order_;

-- insert INTO product (id, name, price) VALUES (not null, "lova", 600.50);
-- insert INTO product (id, name, price) VALUES (not null, "kompiuteris", 800.15);
-- insert INTO product (id, name, price) VALUES (not null, "lova", 600.5);

-- kad rezultate matytųsi užsakymo id, užsakovo pavardė, data, bendra užsakymo suma:

-- SELECT product_order.order_id, l_name, order_.date_,
--  price * quantity as suma FROM customer
--  JOIN product_order ON order_id = order_.id
--  JOIN order_ ON customer_id= customer.id
--  JOIN product on product_id = product.id;

--  kad rezultate matytųsi užsakymo id, pozicijos su kiekiais,
--   kainomis ir bendra pozicijos suma:

-- SELECT product_order.order_id, product.name, product_order.quantity, product.price,
-- product_order.quantity * product.price as suma FROM customer
-- JOIN product_order ON order_id = order_.id
-- JOIN product on product_id = product.id
-- JOIN order_ ON customer_id= customer.id;

-- prieš tai buvusios užklausos pagrindu sukurkite užklausą,
--  kurioje matytųsi, kiek ir kokio produkto buvo užsakyta:

-- SELECT product.name, sum(product_order.quantity), product.price,
-- sum(product_order.quantity) * product.price as suma FROM customer
-- JOIN product_order ON order_id = order_.id
-- JOIN product on product_id = product.id
-- JOIN order_ ON customer_id= customer.id
-- where status_id = 3
-- GROUP BY product_order.product_id;









