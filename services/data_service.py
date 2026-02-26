import pandas as pd

def read_data(file_path, limit=100):
    df = pd.read_csv(file_path)

    # 🔥 VERY IMPORTANT: clean column names (Snowflake friendly)
    df.columns = [col.strip().lower() for col in df.columns]

    # 🔥 Convert NaN → None (Airbyte requirement)
    df = df.where(pd.notnull(df), None)

    return df.head(limit).to_dict(orient="records")