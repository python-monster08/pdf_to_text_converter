# import re
# import pandas as pd
#
# # Define the regular expression pattern to match the question structure
# # This pattern captures the question number, text, optionally a year, and the options.
# question_pattern = r'(\d+)\.\s+(.*?)\s*(?:\[(\d{4})\])?\n\((a)\)\s+(.*?)\s*\((b)\)\s+(.*?)\s*\((c)\)\s+(.*?)\s*\((d)\)\s+(.*?)(?=\n\d+\.|\Z)'
#
# def extract_questions(file_path, pattern):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#
#     questions = []
#     for match in re.finditer(pattern, text, re.DOTALL):
#         # Extract and format question details
#         question_no = match.group(1).strip()
#         question_text = match.group(2).strip()
#         year = match.group(3) if match.group(3) else ''
#         objectives = '\n'.join(match.group(i).strip() + ') ' + match.group(i + 1).strip() for i in range(4, 10, 2))
#
#         # Add extracted data to the list
#         questions.append({
#             "question_no": question_no,
#             "question": question_text,
#             "year": year,
#             "objectives": objectives
#         })
#
#     return questions
#
# # Path to your .txt file
# file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'  # Update this path to the actual file location
#
# # Extract questions based on the pattern
# questions_data = extract_questions(file_path, question_pattern)
#
# # Create a DataFrame from the extracted data
# df_questions = pd.DataFrame(questions_data)
#
# # Define the file name for the Excel file
# excel_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\mcqs.xlsx'  # Update this path to where you want to save the Excel file
#
# # Save the DataFrame to an Excel file
# df_questions.to_excel(excel_file_path, index=False)
#
# print(f"Questions have been saved to '{excel_file_path}'.")

import re
import pandas as pd

# Updated regular expression pattern
question_pattern = r'(\d+\.\s+.*?)\s+List\s+I\s+(.*?)\s+List\s+II\s+(.*?)\s+Code\s+:\s+(.*?)\s+(U\.P\.P\.C\.S\. \(Mains\) \d{4})\s+Answer\s+-\((.*?)\)'

def extract_questions(file_path, pattern):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    questions_data = []
    for match in re.finditer(pattern, text, re.DOTALL):
        questions_data.append({
            "question_no": match.group(1).split('.')[0],  # Extracting just the number part
            "question_text": match.group(2).strip(),
            "list": "List I " + match.group(3).strip() + " List II " + match.group(4).strip(),
            "list_heading": "(crop) (state)",
            "list_items": "\n".join([match.group(3).strip(), match.group(4).strip()]),  # Corrected to join List I and List II items properly
            "code_section": match.group(5).strip(),
            "years": match.group(6).strip(),
            "right_answer": match.group(7).strip()
        })

    return questions_data

# Path to your .txt file (ensure this path is correct for your environment)
file_path = 'F:/Question Bank trials/ExtractList/OutputFiles/extracted_text2.txt'

# Extract questions based on the updated pattern
questions_data = extract_questions(file_path, question_pattern)

# Convert the extracted data into a pandas DataFrame
df_questions = pd.DataFrame(questions_data)

# Define the file name for the Excel file (ensure this path is correct for your environment)
excel_file_name = 'F:/Question Bank trials/ExtractList/OutputFiles/koat.xlsx'

# Save the DataFrame to an Excel file
df_questions.to_excel(excel_file_name, index=False)

print(f"Data saved to {excel_file_name}")
