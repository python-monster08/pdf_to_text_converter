import re

def extract_questions(file_path, pattern):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    questions_data = []
    for match in re.finditer(pattern, text, re.DOTALL):
        question_no = match.group(1)
        question_text = "Please examine the combination of the following Lists and accordingly select the correct Code:"
        list_info_raw = match.group(2).strip().split('\n')
        code_section = "Code : A B C D"
        options = match.group(3).replace('\n', '\n')
        year = match.group(4)
        answer = match.group(5)

        # Split the list info into two columns and format each line
        list_info = []
        for line in list_info_raw:
            parts = line.split('   ')
            if len(parts) < 2:
                parts.append('---')  # Default value if second part is missing
            list_info.append(f"{parts[0]:<35}{parts[1]}")

        formatted_list_info = '\n'.join(list_info)

        formatted_question = f"{question_no}. {question_text}\nList I                               List II\n(crop)                             (state)\n{formatted_list_info}\n\n{code_section}\n{options}\nU.P .P .C.S. (Mains) {year}\nAnswer -({answer})"

        questions_data.append(formatted_question)

    return questions_data

# Path to your .txt file
file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text1.txt'  # Update this path to your actual file location

# Define the regular expression pattern to match the specific question format
question_pattern = r'(\d+)\. Please examine the combination of the following Lists and accordingly\s+select the correct Code:\s+List I\s+List II\s+(.*?)Code :\s+A B C D\s+(a\).+?d\).+?)U\.P \.P \.C\.S\. \(Mains\) (\d+)\s+Answer -\((c)\)'

# Extract questions that match the pattern
matching_questions = extract_questions(file_path, question_pattern)

# Print each found question
for question in matching_questions:
    print(question)
    print("\n---\n")

# import re
#
# def extract_questions(file_path, pattern):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#
#     questions_data = []
#     for match in re.finditer(pattern, text, re.DOTALL):
#         # Extracting the whole match as a single question
#         whole_match = match.group(0).strip()
#
#         # Append the extracted question to the list
#         questions_data.append(whole_match)
#
#     return questions_data
#
# # Regular expression pattern to match the continuous structure of questions
# # This pattern assumes that each section starts on a new line
# question_pattern = (
#     r'(\d+\..*?)\n'  # Question number and text
#     r'(List I\s+List II\s+.*?)\n'  # List I and List II
#     r'(Code\s+:.*?)\n'  # Code section
#     r'((?:U\.P\.P\.C\.S\.|U\.P\s+\.\s+P\s+\.\s+C\.S\.) \(Mains\) \d{4})\n'  # Year section
#     r'(Answer\s+-\(.*?\))'  # Answer section
# )
#
# # Path to your .txt file
# file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text1.txt'  # Update this to the actual path of your file
#
# # Extract questions that match the pattern
# matching_questions = extract_questions(file_path, question_pattern)
#
# # Print each found question
# for question in matching_questions:
#     print(question)
#     print("\n---\n")

