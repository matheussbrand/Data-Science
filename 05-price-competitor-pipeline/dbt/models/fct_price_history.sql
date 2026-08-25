select
    sku,
    competitor,
    cast(price as numeric) as price,
    collected_at
from {{ ref('stg_prices') }}
