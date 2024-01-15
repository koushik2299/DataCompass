# DataCompass

DataCompass is a Python package designed to enhance data analysis with pandas DataFrames. It provides a set of tools to quickly inspect and understand the structure and contents of DataFrames, aiding in efficient data exploration and preprocessing.

## Features

- **Describe Columns**: Analyze and list numerical and categorical columns in a DataFrame.
- **Display Missing Information**: Calculate and display the count and percentage of missing values in each column.
- **Display Basic Information**: Show basic details like the number of columns, rows, and the first few observations.
- **Display Unique Values**: Enumerate unique values or the count of unique values in each column.

## Installation

To install DataCompass, simply use pip:

```bash
pip install datacompass
```
```bash
import pandas as pd
from datacompass import describe_columns, display_missing_info, display_basic_info, display_unique_values

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, None, 4], 'B': ['a', 'b', 'b', 'c']})

# Describe Columns
describe_columns(df)

# Display Missing Information
display_missing_info(df)

# Display Basic Information
display_basic_info(df)

# Display Unique Values
display_unique_values(df)
```
```bash
### Describe Columns Output

Number of Numerical Columns: 1
['A']
-------------------------------------------------------------------------------------
Number of Categorical Columns: 1
['B']

### Display Missing Information Output

|   Missing Count | Missing Percentage |
|----------------:|-------------------:|
| A              |                  1 |             25.0 |
| B              |                  0 |              0.0 |

### Display Basic Information Output

Number of Columns: 2
Number of Rows: 4

First 6 Observations of Our Data:
  A    B
1.0  a
2.0  b
NaN  b
4.0  c

### Display Unique Values Output

A contains: 1.0, 2.0, nan, 4.0
B contains: a, b, c

```


## Requirements

- pandas

## Contribution

Contributions to DataCompass are welcome! Please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/koushik2299/datacompass).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**[Sai Koushik Gandikota](https://www.linkedin.com/in/gandikota-sai-koushik/)**


