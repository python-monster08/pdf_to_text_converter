import re

# Define the regular expression pattern for the specific question type
question_pattern = r'(\d+\..*?)\s+List\s+I\s+(.*?)\s+List\s+II\s+(.*?)\s+Code\s+:\s+(.*?)\s+(U\.P\s+\.P\s+\.C\.S\. \(Mains\) \d{4})\s+Answer\s+-\((.*?)\)'

# Function to extract questions using the new pattern
def extract_questions_v2(file_path, pattern):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Use re.DOTALL to ensure '.' matches newlines as well
    matches = re.findall(pattern, text, re.DOTALL)

    # Filter out empty strings and strip leading/trailing whitespace from each question
    questions = ['\n'.join(match).strip() for match in matches if any(match)]

    return questions

# Path to your .txt file (ensure this is the correct path)
file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text.txt'

# Extract questions based on the updated pattern
questions = extract_questions_v2(file_path, question_pattern)

# Print each extracted question, separated by a line
for question in questions:
    print(question)
    print("\n---\n")  # Separator between questions




# Separate new line
# import re
#
# # Define the regular expression pattern to match the question structure
# # This pattern assumes questions start with a number followed by a period and a space,
# # then the question text, optionally followed by a year in brackets, and then the options.
# question_pattern = r'(\d+\.\s+.*?)(?:\s+\[\d{4}\])?\s*\((a)\)\s+(.*?)\s*\((b)\)\s+(.*?)\s*\((c)\)\s+(.*?)\s*\((d)\)\s+(.*?)(?=\n\d+\.|\Z)'
#
# def extract_questions(file_path, pattern):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#
#     # Use re.DOTALL to ensure '.' matches newlines as well
#     matches = re.findall(pattern, text, re.DOTALL)
#
#     questions = []
#     for match in matches:
#         # Join the captured groups with new lines to format each question part
#         question = '\n'.join(match)
#         questions.append(question.strip())
#
#     return questions
#
# # Path to your .txt file
# file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'  # Make sure to update this path to your actual file location
#
# # Extract questions based on the pattern
# questions = extract_questions(file_path, question_pattern)
#
# # Print each extracted question, formatted with new lines
# for question in questions:
#     print(question)
#     print("\n---\n")  # Separator between questions


# import re
#
# # Define the regular expression pattern to match the question structure
# # This pattern captures the question number and text, followed by the options.
# question_pattern = r'(\d+\.\s+.*?)(?=\n\(\w+\))\s*((?:\n\(\w+\)\s+.*?)+)(?=\n\d+\.|\Z)'
#
#
# def extract_questions(file_path, pattern):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#
#     questions = []
#     for match in re.finditer(pattern, text, re.DOTALL):
#         # Extract question text and options, and format them
#         question_text = match.group(1).strip()
#         options = match.group(2).strip().split('\n')
#         formatted_options = '\n'.join(option.strip() for option in options)
#
#         # Combine question text and formatted options
#         formatted_question = f"{question_text}\n{formatted_options}"
#         questions.append(formatted_question)
#
#     return questions
#
#
# # Path to your .txt file
# file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'  # Make sure to update this path to your actual file location
#
# # Extract questions based on the pattern
# questions = extract_questions(file_path, question_pattern)
#
# # Print each extracted question, formatted with new lines and separated by dashed lines
# for question in questions:
#     print(question)
#     print("\n---\n")
