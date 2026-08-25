select
    order_id,
    customer_id,
    product_id,
    order_date,
    quantity,
    unit_price,
    quantity * unit_price as total_amount
from {{ ref('stg_orders') }}
