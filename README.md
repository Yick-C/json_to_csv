# JSON to CSV Converter
## Description
This Python script allows you to convert JSON files to CSV format using the powerful Pandas library. It leverages the Pandas DataFrame and Series objects to efficiently process and transform data from JSON to CSV.

## Requirements
- Python 3.x
- Pandas library (install using pip install pandas)

## Usage
1. Make sure you have Python installed on your system.
2. Install the required Pandas library using pip install pandas.
3. Place your JSON file in the same directory as the script or provide the file path as an argument while running the script.
4. Execute the script by running the following command:

Run it by typing 
```
python json_to_csv.py
```
The script will convert the JSON file named "data.json" in the current directory and save the output as "output.csv."

## How it Works
The script reads the JSON file and loads its data into a Pandas DataFrame. The DataFrame is a two-dimensional tabular data structure, much like a spreadsheet, where rows and columns hold the data. The script then processes the data and converts it into CSV format using the DataFrame's built-in capabilities.

-----

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
