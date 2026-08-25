import pandas as pd

def validate_orders(path):
    df=pd.read_csv(path)
    checks={
        "not_null_order_id": df["order_id"].notna().all(),
        "unique_order_id": df["order_id"].is_unique,
        "positive_amount": (df["amount"] > 0).all(),
    }
    failed=[name for name,ok in checks.items() if not ok]
    if failed:
        raise ValueError(f"Data quality failed: {failed}")
    return checks

if __name__=="__main__":
    print(validate_orders("data/orders.csv"))
