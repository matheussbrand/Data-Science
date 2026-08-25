create schema if not exists staging;
create schema if not exists marts;

create table if not exists staging.sales (
  order_id bigint, customer_id bigint, product_id bigint,
  order_date date, quantity int, unit_price numeric(12,2)
);
