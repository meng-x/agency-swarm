# filename: json_to_excel.py

import pandas as pd
import json

# Function to convert JSON to Excel
def json_to_excel(json_file, excel_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Extract the 'products' list
    products = data['products list']
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(products)
    
    # Reorder the DataFrame columns as specified
    df = df[['product name', 'url', 'details']]
    
    # Save the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)
    print(f"Excel file '{excel_file}' has been created successfully.")

# Replace 'input.json' with the path to your JSON file and 'output.xlsx' with your desired Excel file name
json_to_excel('aflac-life-insurance-products_file-usUOiz8DeZegjZZWYr3ObOiu.json', 'output.xlsx')