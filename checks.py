EXPECTED_COLUMNS = {"order_id", "price"}  # edit to match head -5 sales.csv


def check_schema(df):
    missing = EXPECTED_COLUMNS - set(df.columns)
    assert not missing, f"missing columns: {missing}"


def check_quality(df):
    assert len(df) > 0, "no rows"
    assert df["order_id"].notna().all(), "blank order_id found"
    assert df["order_id"].is_unique, f"{df['order_id'].duplicated().sum()} duplicate order_ids"
    assert (df["new_price"] > 0).all(), f"{(~(df['new_price'] > 0)).sum()} bad prices"