import json
import pandas as pd

# Step 1: Read the JSON file
with open('aflac-life-insurance.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Step 2: Iterate over the keys in the JSON object
for key in data:
    # Create a DataFrame from the JSON array
    df = pd.DataFrame(data[key])

    # Step 3: Write the DataFrame to an Excel file
    excel_filename = f"{key}.xlsx"
    df.to_excel(excel_filename, index=False)

print("Excel files created successfully.")
