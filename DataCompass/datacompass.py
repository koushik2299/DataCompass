import pandas as pd

class DataFrameCompass:
    def __init__(self, df, basic_info=True, unique=False, missing=False, description=False):
        self.df = df
        self.show_basic_info = basic_info
        self.show_unique = unique
        self.show_missing = missing
        self.show_description = description

    def display_basic_info(self):
        columns = self.df.shape[1]
        rows = self.df.shape[0]
        print("Number of Columns:", columns)
        print("Number of Rows:", rows)
        print("\nFirst 6 Observations of Our Data:\n", self.df.head(6))

    def display_unique_values(self):
        for col in self.df.columns:
            unique_values = self.df[col].unique()
            if len(unique_values) > 50:
                print(f"{col} has {len(unique_values)} unique values")
            else:
                print(f"{col} contains: {', '.join(map(str, unique_values))}")

    def display_missing_info(self):
        missing_count = self.df.isnull().sum()
        total_values = self.df.shape[0]
        missing_percentage = (missing_count / total_values) * 100
        missing_data_summary = pd.DataFrame({
            'Missing Count': missing_count,
            'Missing Percentage': missing_percentage
        })
        print(missing_data_summary)

    def describe_columns(self):
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        print("Number of Numerical Columns:", len(numeric_cols))
        print(list(numeric_cols))
        print('-' * 85)
        print("Number of Categorical Columns:", len(categorical_cols))
        print(list(categorical_cols))

    def fit(self):
        if self.show_basic_info:
            self.display_basic_info()
        
        if self.show_missing:
            self.display_missing_info()
        
        if self.show_description:
            self.describe_columns()

        if self.show_unique:
            self.display_unique_values()

# Example of usage:
# df = pd.DataFrame(...)  # your pandas DataFrame
# compass = DataFrameCompass(df, unique=True, missing=True)
# compass.fit()
