from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64
from feast.infra.offline_stores.file_source import FileSource

customer=Entity(name="customer_id", value_type="INT64")
source=FileSource(path="data/features/customer_features", timestamp_field="event_timestamp")
customer_features=FeatureView(
    name="customer_features",
    entities=[customer],
    ttl=None,
    schema=[Field(name="orders_30d",dtype=Int64),Field(name="revenue_30d",dtype=Float32)],
    online=True,
    source=source,
)
