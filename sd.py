from datacompass import display_basic_info
from datacompass import describe_columns
import pandas as pd

df = pd.read_csv('Train.csv')

describe_columns(df)

display_basic_info(df)