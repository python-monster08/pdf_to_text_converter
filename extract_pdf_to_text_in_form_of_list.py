# import fitz  # PyMuPDF
# import re
#
#
# def extract_text_from_pdf(pdf_path):
#     """
#     Extracts text from a PDF file.
#
#     Parameters:
#     pdf_path (str): The path to the PDF file from which to extract text.
#
#     Returns:
#     str: The extracted text from the PDF.
#     """
#     doc = fitz.open(pdf_path)
#     # text = ""
#     text = """
#     Please examine the combination of the following Lists and accordingly select the correct Code:
#     List I List II (crop) (state) A. Groundnut 1. Andhra Pradesh B. Mustard 2. Rajasthan C. Soyabean 3. Madhya Pradesh D. Cocunut 4. Kerala Code : A B C D a) 1 3 2 4 b) 2 1 3 4 c) 1 2 3 4 d) 4 3 2 1 U.P.P.C.S. (Mains) 2008 Answer -(c)
#     """
#     for page in doc:
#         text += page.get_text()
#     doc.close()
#     return text
#
#
# def format_extracted_text(text):
#     """
#     Formats the extracted text to match the specified structure.
#
#     Parameters:
#     text (str): The extracted text from the PDF.
#
#     Returns:
#     str: The formatted text.
#     """
#     # Regular expression to capture the content structure
#     pattern = re.compile(
#         r"List I\s+List II\s+\(crop\)\s+\(state\)\s+(A\. Groundnut\s+1\. Andhra Pradesh\s+B\. Mustard\s+2\. Rajasthan\s+C\. Soyabean\s+3\. Madhya Pradesh\s+D\. Cocunut\s+4\. Kerala\s+Code :)\s+A\s+B\s+C\s+D\s+(a\) 1 3 2 4\s+b\) 2 1 3 4\s+c\) 1 2 3 4\s+d\) 4 3 2 1\s+U\.P\.P\.C\.S\. \(Mains\) 2008\s+Answer -\(c\))")
#
#     match = pattern.search(text)
#     if match:
#         # Construct the formatted text based on the match
#         formatted_text = f"""List I                        List II
# (crop)                        (state)
#
# A. Groundnut            1. Andhra Pradesh
#
# B. Mustard              2. Rajasthan
#
# C. Soyabean             3. Madhya Pradesh
#
# D. Cocunut              4. Kerala
#
# Code :  A   B    C   D
#
# a) 1 3 2 4
# b) 2 1 3 4
# c) 1 2 3 4
# d) 4 3 2 1
# U.P.P.C.S. (Mains) 2008
# Answer -(c)"""
#         return formatted_text
#     else:
#         return "The specified pattern was not found in the text."
#
#
# # Specify the path to your PDF file
# pdf_path = r"F:\Question Bank trials\ExtractList\OutputFiles\formatted_text.txt"  # Update this with the actual path to your PDF
#
# # Extract text from the PDF
# extracted_text = extract_text_from_pdf(pdf_path)
#
# # Format the extracted text
# formatted_text = format_extracted_text(extracted_text)
#
# # Print the formatted text
# print(formatted_text)


import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Parameters:
    pdf_path (str): The path to the PDF file from which to extract text.

    Returns:
    str: The extracted text from the PDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def format_extracted_text(text):
    """
    Formats the extracted text to match the specified structure.

    Parameters:
    text (str): The extracted text from the PDF.

    Returns:
    str: The formatted text.
    """
    pattern = re.compile(
        r"List I\s+List II\s+\(crop\)\s+\(state\)\s+(A\. Groundnut\s+1\. Andhra Pradesh\s+B\. Mustard\s+2\. Rajasthan\s+C\. Soyabean\s+3\. Madhya Pradesh\s+D\. Cocunut\s+4\. Kerala\s+Code :)\s+A\s+B\s+C\s+D\s+(a\) 1 3 2 4\s+b\) 2 1 3 4\s+c\) 1 2 3 4\s+d\) 4 3 2 1\s+U\.P\.P\.C\.S\. \(Mains\) 2008\s+Answer -\(c\))"
    )
    match = pattern.search(text)
    if match:
        formatted_text = match.group(0)
        return formatted_text
    else:
        return "The specified pattern was not found in the text."

def read_text_from_file(file_path):
    """
    Reads text from a given file.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    str: The text read from the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

# Specify the paths
pdf_path = r"F:\Question Bank trials\ExtractList\generate_pdf_to_row_text_data_file.py"  # Path to the PDF file
input_text_file_path = r"F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt"  # Path to the text file containing the input text
output_file_path = r"F:\Question Bank trials\ExtractList\OutputFiles\formated_file.txt"  # Path to the output file

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Read the input text from a file (if needed)
# extracted_text = read_text_from_file(input_text_file_path)

# Format the extracted text
formatted_text = format_extracted_text(extracted_text)

# Save the formatted text to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(formatted_text)

# Print the formatted text (optional)
print(formatted_text)
