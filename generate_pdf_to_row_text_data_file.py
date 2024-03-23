# import fitz  # PyMuPDF
#
# def extract_and_format_text(pdf_path):
#     """
#     Extracts text from a PDF file and formats it according to a specific structure.
#
#     Parameters:
#     pdf_path (str): The path to the PDF file.
#
#     Returns:
#     str: The formatted text.
#     """
#     # Open the PDF file
#     doc = fitz.open(pdf_path)
#
#     # Initialize a variable to store the extracted text
#     text = ""
#
#     # Extract text from each page
#     for page in doc:
#         text += page.get_text()
#
#     # Close the PDF document
#     doc.close()
#
#     # Format the extracted text
#     formatted_text = """Please examine the combination of the following Lists and accordingly select the correct Code:
# List I List II (crop) (state) A. Groundnut 1. Andhra Pradesh B. Mustard 2. Rajasthan C. Soyabean 3. Madhya Pradesh D. Cocunut 4. Kerala Code : A B C D a) 1 3 2 4 b) 2 1 3 4 c) 1 2 3 4 d) 4 3 2 1 U.P.P.C.S. (Mains) 2008 Answer -(c)"""
#
#     return formatted_text
#
#
# def save_text_to_file(text, file_path):
#     """
#     Saves the provided text to a file.
#
#     Parameters:
#     text (str): The text to save.
#     file_path (str): The full path to the file, including the file name and extension.
#     """
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(text)
#
# # Example usage
# if __name__ == "__main__":
#     pdf_path = r"F:\Question Bank trials\ExtractList\extract_list.pdf"  # Replace with your PDF file path
#     output_file_path = r"F:\Question Bank trials\ExtractList\OutputFiles\formatted_text.txt"  # Adjusted path to include filename
#     formatted_text = extract_and_format_text(pdf_path)
#     save_text_to_file(formatted_text, output_file_path)
#     print(f"Formatted text has been saved to {output_file_path}.")
#
# import PyPDF2
#
# # Open the PDF file
# with open(r'F:\Question Bank trials\ExtractList\extract_list.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)  # Updated to use PdfReader
#
#     # Initialize a variable to hold all the text
#     all_text = ''
#
#     # Loop through each page in the PDF
#     for page in pdf_reader.pages:  # Updated to iterate directly over pages
#         # Extract text from the page
#         text = page.extract_text()
#
#         # Append the text to the all_text variable
#         all_text += text
#
# # Save the extracted text to a .txt file
# with open(r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text.txt', 'w') as text_file:
#     text_file.write(all_text)
#
# print("Text extracted and saved to extracted_text.txt")


#  ***********************Workin code*******************
# import PyPDF2
#
# # Define your PDF file path and output file path
# pdf_path = r'F:\Question Bank trials\ExtractList\History Medieval Ques Only Pages 15-16.pdf'
# output_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'
#
# # Open the PDF file
# with open(pdf_path, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)  # Updated to use PdfReader
#
#     # Initialize a variable to hold all the text
#     all_text = ''
#
#     # Loop through each page in the PDF
#     for page in pdf_reader.pages:  # Updated to iterate directly over pages
#         # Extract text from the page
#         text = page.extract_text()
#
#         # Append the text to the all_text variable
#         all_text += text
#
# # Save the extracted text to a .txt file
# with open(output_file_path, 'w') as text_file:
#     text_file.write(all_text)
#
# print(f"Text extracted and saved to {output_file_path}")



# import PyPDF2
# import re
#
# # Define your PDF file path and output file path
# pdf_path = r'F:\Question Bank trials\ExtractList\History Medieval Ques Only Pages 15-16.pdf'
# output_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'
#
# # Open the PDF file
# with open(pdf_path, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#
#     # Initialize a variable to hold all the text
#     all_text = ''
#
#     # Loop through each page in the PDF
#     for page in pdf_reader.pages:
#         # Extract text from the page
#         text = page.extract_text()
#
#         # Append the text to the all_text variable
#         all_text += text
#
# # Define patterns to remove
# patterns_to_remove = [
#     r'EBD_8342',
#     r'Medieval History A15',
#     r'Medieval History',
#     r'Topicwise Solved PapersA16'
# ]
#
# # Remove the defined patterns and extra spaces
# for pattern in patterns_to_remove:
#     all_text = re.sub(pattern, '', all_text)
# all_text = re.sub(r'\n\s*\n', '\n', all_text)  # Replace multiple newlines with a single newline
# all_text = re.sub(r' +', ' ', all_text)  # Replace multiple spaces with a single space
#
# # Save the cleaned text to a .txt file
# with open(output_file_path, 'w', encoding='utf-8') as text_file:
#     text_file.write(all_text.strip())  # Use .strip() to remove leading and trailing whitespace
#
# print(f"Text extracted and cleaned up, then saved to {output_file_path}")





# '''This is working in good formate'''


# import PyPDF2
# import re
#
# # Define your PDF file path and output file path
# pdf_path = r'F:\Question Bank trials\ExtractList\History Medieval Ques Only Pages 15-16.pdf'
# output_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'
#
# # Open the PDF file
# with open(pdf_path, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)  # Using PdfReader
#
#     # Initialize a variable to hold all the text
#     all_text = ''
#
#     # Loop through each page in the PDF
#     for page in pdf_reader.pages:  # Iterating directly over pages
#         # Extract text from the page
#         text = page.extract_text()
#
#         # Append the text to the all_text variable
#         all_text += text + "\n"  # Adding a newline after each page's text
#
# # Define unwanted phrases to remove
# unwanted_phrases = [
#     "EBD_8342",
#     "Medieval History A15",
#     "Medieval History",
#     "Topicwise Solved PapersA16"
# ]
#
# # Remove unwanted phrases and extra spaces
# for phrase in unwanted_phrases:
#     all_text = all_text.replace(phrase, "")
# all_text = re.sub(' +', ' ', all_text)  # Replace multiple spaces with a single space
#
# # Add a newline before each question number
# all_text = re.sub(r'(\d+\.)', r'\n\1', all_text)
#
# # Replace ' - ' with '-' and remove leading/trailing whitespace
# all_text = all_text.replace(" - ", "-").strip()
#
# # Save the cleaned text to a .txt file
# with open(output_file_path, 'w', encoding='utf-8') as text_file:
#     text_file.write(all_text)
#
# print(f"Text extracted and cleaned. Saved to {output_file_path}")



import PyPDF2
import re

# Define your PDF file path and output file path
pdf_path = r'F:\Question Bank trials\ExtractList\History Medieval Ques Only Pages 15-16.pdf'
output_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'

# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)  # Using PdfReader

    # Initialize a variable to hold all the text
    all_text = ''

    # Loop through each page in the PDF
    for page in pdf_reader.pages:  # Iterating directly over pages
        # Extract text from the page
        text = page.extract_text()

        # Append the text to the all_text variable
        all_text += text + "\n"  # Adding a newline after each page's text

# Define unwanted phrases to remove
unwanted_phrases = [
    "EBD_8342",
    "Medieval History A15",
    "Medieval History",
    "Topicwise Solved PapersA16"
]

# Remove unwanted phrases and extra spaces
for phrase in unwanted_phrases:
    all_text = all_text.replace(phrase, "")
all_text = re.sub(' +', ' ', all_text)  # Replace multiple spaces with a single space

# Add a newline before each question number
all_text = re.sub(r'(\d+\.)', r'\n\1', all_text)

# Formatting specific question types
all_text = re.sub(r'(\d+\.)\s+(.*?:)\s+\[', r'\1 \2\n[', all_text)  # Ensure year and question text are on separate lines
all_text = re.sub(r'((?:\n[ABCD]\. \d{4})+)\s+(\d+\.\s+)', r'\1\n\n\2', all_text)  # Ensure space between list items and next question

# Handle specific list formatting
def format_list(match):
    content = match.group(0)
    # Split lines, strip spaces, and rejoin with a single space
    lines = content.split('\n')
    formatted_lines = [' '.join(line.split()) for line in lines if line.strip()]
    return '\n'.join(formatted_lines)

# Apply list formatting to specific question types
all_text = re.sub(r'(?<=List-II)(.*?)(?=Codes:)', format_list, all_text, flags=re.DOTALL)
all_text = re.sub(r'(?<=lists:)(.*?)(?=Codes:)', format_list, all_text, flags=re.DOTALL)

# Replace ' - ' with '-' and remove leading/trailing whitespace
all_text = all_text.replace(" - ", "-").strip()

# Save the cleaned text to a .txt file
with open(output_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(all_text)

print(f"Text extracted and cleaned. Saved to {output_file_path}")
