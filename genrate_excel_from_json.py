import pandas as pd
import json
# Load the JSON data
with open('new_parsed_questions.json', 'r') as f:
    questions_data = json.load(f)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(questions_data)

# Save the DataFrame to an Excel file
excel_file_path = 'OutputFiles/new_questions_output.xlsx'
df.to_excel(excel_file_path, index=False)

print(excel_file_path)
