-- Day 21: reading query plans and testing indexes

-- Small table: Seq Scan even with a primary key
EXPLAIN SELECT * FROM sales_clean WHERE customer_id = 'C001';
EXPLAIN SELECT * FROM sales_clean WHERE order_id = 1001;

-- Big test table, no index
CREATE TABLE big_orders AS
SELECT
    g                                         AS order_id,
    (random() * 10000)::int                   AS customer_id,
    DATE '2025-01-01' + (random() * 365)::int AS order_date,
    (random() * 500)::numeric(10,2)           AS amount
FROM generate_series(1, 500000) AS g;

ANALYZE big_orders;

-- Before the index: Parallel Seq Scan, about 44 ms
EXPLAIN ANALYZE SELECT * FROM big_orders WHERE customer_id = 42;

-- Add the index
CREATE INDEX idx_big_customer ON big_orders(customer_id);
ANALYZE big_orders;

-- After the index: Bitmap Index Scan, about 1.5 ms
EXPLAIN ANALYZE SELECT * FROM big_orders WHERE customer_id = 42;

-- Not selective (about 90% of rows): Seq Scan again
EXPLAIN ANALYZE SELECT * FROM big_orders WHERE customer_id < 9000;
