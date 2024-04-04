# import re
# import pandas as pd
#
# # Define the regular expression pattern for the specific question type
# question_pattern = r'(\d+\..*?)\s+List\s+I\s+(.*?)\s+List\s+II\s+(.*?)\s+Code\s+:\s+(.*?)\s+(U\.P\s+\.P\s+\.C\.S\.\s+\(Mains\)\s+\d{4})\s+Answer\s+-\((.*?)\)'
#
# # Function to extract questions using the new pattern
# def extract_questions_v2(file_path, pattern):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#
#     # Use re.DOTALL to ensure '.' matches newlines as well
#     matches = re.findall(pattern, text, re.DOTALL)
#
#     # Process each match into a structured dictionary
#     questions = []
#     for match in matches:
#         if any(match):
#             question_dict = {
#                 'question_text': match[0].strip(),
#                 'list': match[1].strip() + '\n' + match[2].strip(),
#                 'question_code': match[3].strip(),
#                 'exam_name': 'U.P .P .C.S.',
#                 'exam_section': '(Mains)',
#                 'exam_year': match[4][-4:],
#                 'correct_answer': 'Answer -' + match[5].strip()
#             }
#             questions.append(question_dict)
#
#     return questions
#
# # Path to your .txt file (ensure this is the correct path)
# file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text.txt'
#
# # Extract questions based on the updated pattern
# questions = extract_questions_v2(file_path, question_pattern)
#
# # Convert list of dictionaries to a pandas DataFrame
# questions_df = pd.DataFrame(questions)
#
# # Save the DataFrame to an Excel file
# output_excel_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_questions.xlsx'
# questions_df.to_excel(output_excel_path, index=False)
#
# print(f"Saved {len(questions)} questions to '{output_excel_path}'")


# import re
# import pandas as pd

# # Define the regular expression pattern for the specific question type
# question_pattern = r'(\d+\..*?)\s+List\s+I\s+(.*?)\s+List\s+II\s+(.*?)\s+Code\s+:\s+(.*?)\s+(U\.P\s+\.P\s+\.C\.S\.\s+\(Mains\)\s+\d{4})\s+Answer\s+-\((.*?)\)'

# # Function to extract questions using the new pattern
# def extract_questions_v2(file_path, pattern):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()

#     # Use re.DOTALL to ensure '.' matches newlines as well
#     matches = re.findall(pattern, text, re.DOTALL)

#     # Process each match into a structured dictionary
#     questions = []
#     for match in matches:
#         if any(match):
#             # Improved splitting for List I and List II
#             list_i_content = match[1].split('List II')[0].strip()
#             list_ii_content = match[2].split('Code :')[0].strip()

#             list_i = "List I:\n" + list_i_content
#             list_ii = "List II:\n" + list_ii_content

#             question_dict = {
#                 'question_text': match[0].strip(),
#                 'list_i': list_i,
#                 'list_ii': list_ii,
#                 'question_code': match[3].strip(),
#                 'exam_name': 'U.P .P .C.S.',
#                 'exam_section': '(Mains)',
#                 'exam_year': match[4][-4:],
#                 'correct_answer': 'Answer -' + match[5].strip()
#             }
#             questions.append(question_dict)

#     return questions

# # Path to your .txt file (ensure this is the correct path)
# file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text.txt'  # Updated to the uploaded file's path

# # Extract questions based on the updated pattern
# questions = extract_questions_v2(file_path, question_pattern)

# # Convert list of dictionaries to a pandas DataFrame
# questions_df = pd.DataFrame(questions)

# # Save the DataFrame to an Excel file
# output_excel_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_questions.xlsx'  # Saving to accessible path
# questions_df.to_excel(output_excel_path, index=False)

# print(f"Saved {len(questions)} questions to '{output_excel_path}'")


import pandas as pd
import re

# Function to read file content and extract questions
def extract_questions_from_file(file_path, pattern):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use re.DOTALL to ensure '.' matches newlines as well
    matches = re.findall(pattern, content, re.DOTALL)

    # Process each match into a structured dictionary
    questions = []
    for match in matches:
        if any(match):
            # Splitting list I and II into separate parts
            list_i_lines = match[1].strip().split('\n')
            list_ii_lines = match[2].strip().split('\n')

            # Keeping the titles and reconstructing the lists
            list_i_title = list_i_lines[0]  # The title 'List I (crop)'
            list_i = '\n'.join(list_i_lines[1:])  # The rest of List I
            
            list_ii_title = list_ii_lines[0]  # The title 'List II (state)'
            list_ii = '\n'.join(list_ii_lines[1:])  # The rest of List II

            question_dict = {
                'question_text': match[0].strip(),
                'list_i': list_i_title + '\n' + list_i,
                'list_ii': list_ii_title + '\n' + list_ii,
                'question_code': match[3].strip(),
                'exam_name': ' '.join(match[4].split(' ')[0:3]),
                'exam_section': match[4].split(' ')[3].replace('(', '').replace(')', ''),
                'exam_year': match[4].split(' ')[4],
                'correct_answer': 'Answer -' + match[5].strip()
            }
            questions.append(question_dict)

    return questions

# Replace the placeholder path with the actual path to your text or word file
file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text.txt'

# Define the regular expression pattern for the specific question type
question_pattern = r'(\d+\..*?)\s+List\s+I\s+(.*?)\s+List\s+II\s+(.*?)\s+Code\s+:\s+(.*?)\s+(U\.P\s+\.P\s+\.C\.S\. \(Mains\) \d{4})\s+Answer\s+-\((.*?)\)'

# Extract questions from the file
questions = extract_questions_from_file(file_path, question_pattern)

# Convert list of dictionaries to a pandas DataFrame
questions_df = pd.DataFrame(questions)

# Define path for the Excel file
excel_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_questions.xlsx'

# Save the DataFrame to an Excel file
questions_df.to_excel(excel_file_path, index=False)

# The path to the saved Excel file will be returned
print(excel_file_path)
