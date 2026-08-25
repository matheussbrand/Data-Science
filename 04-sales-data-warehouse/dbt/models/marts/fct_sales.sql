select
    order_id,
    customer_id,
    product_id,
    order_date,
    quantity,
    unit_price,
    revenue
from {{ ref('stg_sales') }}
