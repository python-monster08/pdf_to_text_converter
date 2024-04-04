from docx import Document
import json

def extract_questions_from_docx(file_path):
    # Load the Word document
    doc = Document(file_path)

    # Initialize an empty list to hold the questions
    questions = []

    # Initialize an empty dictionary to hold the current question being processed
    current_question = {}

    # Define the keys we're looking for
    keys = [
    "[QUESTION_HEADING]", "[LIST_HEADING]", "[LIST_HEADING_I]", "[LIST_HEADING_II]",
    "[LIST_CONTENT1]", "[LIST_CONTENT1_A]", "[LIST_CONTENT1_1]",
    "[LIST_CONTENT2]", "[LIST_CONTENT2_B]", "[LIST_CONTENT2_2]",
    "[LIST_CONTENT3]", "[LIST_CONTENT3_C]", "[LIST_CONTENT3_3]",
    "[LIST_CONTENT4]", "[LIST_CONTENT4_D]", "[LIST_CONTENT4_4]",
    "[CODE]", "[OBJECTIVES]", "[OBJECTIVE1]", "[OBJECTIVE2]",
    "[OBJECTIVE3]", "[OBJECTIVE4]", "[EXAM_NAME]", "[EXAM_TYPE]", "[EXAM_YEAR]",
    "[CORRECT_ANSWER]"
]


    # Iterate through each paragraph in the document
    for para in doc.paragraphs:
        # Check if the paragraph is a key
        if any(key in para.text for key in keys):
            # Split the paragraph text by ': ' to separate the key and the value
            key, _, value = para.text.partition(': ')
            # Remove brackets from the key to match the desired format
            key = key.replace("[", "").replace("]", "")
            # Add the key and value to the current question
            current_question[key] = value.strip()
        else:
            # If the paragraph is not a key, check if we've been building a question
            if current_question:
                # Add the completed question to the list of questions
                questions.append(current_question)
                # Reset the current question dictionary for the next question
                current_question = {}

    # Check if the last question in the document was added
    if current_question:
        questions.append(current_question)

    return questions

# Use the path to the Word document created previously
file_path = 'match_questions.docx'
questions = extract_questions_from_docx(file_path)

# Convert the list of questions to a JSON string
questions_json = json.dumps(questions, indent=4)

# Save the JSON data to a file
output_file_path = 'OutputFiles/questions_output.json'
with open(output_file_path, 'w') as f:
    f.write(questions_json)

print('Generated file is saved on path: ',output_file_path)
