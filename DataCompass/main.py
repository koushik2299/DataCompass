import pandas as pd

def describe_columns(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    print("Number of Numerical Columns:", len(numeric_cols))
    print(list(numeric_cols))
    print('-' * 85)
    print("Number of Categorical Columns:", len(categorical_cols))
    print(list(categorical_cols))

def display_missing_info(df):
    missing_count = df.isnull().sum()
    total_values = df.shape[0]
    missing_percentage = (missing_count / total_values) * 100
    missing_data_summary = pd.DataFrame({
        'Missing Count': missing_count,
        'Missing Percentage': missing_percentage
    })
    print(missing_data_summary)

def display_basic_info(df):
    columns = df.shape[1]
    rows = df.shape[0]
    print("Number of Columns:", columns)
    print("Number of Rows:", rows)
    print("\nFirst 6 Observations of Our Data:\n", df.head(6))

def display_unique_values(df):
    for col in df.columns:
        unique_values = df[col].unique()
        if len(unique_values) > 50:
            print(f"{col} has {len(unique_values)} unique values")
        else:
            print(f"{col} contains: {', '.join(map(str, unique_values))}")