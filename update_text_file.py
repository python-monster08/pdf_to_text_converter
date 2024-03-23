

import re


def reformat_question(text):
    # Regular expression pattern to match the question structure
    pattern = r'(\d+\.\s+Match List-I with List-IIand select the correct answer using\s+the codes given below the lists:)\s+\[(\d{4})\](.*?)(?=^\d+\.\s+|\Z)'

    # Function to format a single match
    def format_match(match):
        intro, year, content = match.groups()
        formatted_intro = f"{intro}    [{year}]"

        # Splitting and aligning List-I and List-II items
        list_parts = re.split(r'(List-I\s+List-II)', content, flags=re.DOTALL)
        list_i_items = re.findall(r'([ABCD]\. \d{4})(.*?)\n(?=[ABCD]\. \d{4}|$)', list_parts[2], flags=re.DOTALL)
        list_ii_items = re.findall(r'(\d+\.\s+.*?)(?=\n\d+\.|\Z)', list_parts[2], flags=re.DOTALL)

        formatted_list = "List-I                             List-II\n"
        for i, (li, lii) in enumerate(zip(list_i_items, list_ii_items)):
            li_text = ' '.join(li).replace('\n', ' ')
            lii_text = lii[0].replace('\n', ' ')
            if i == len(list_i_items) - 1:  # Handle the last line differently if there's an extra List-II item
                formatted_list += f"{li_text:<35}{lii_text}\n"
            else:
                formatted_list += f"{li_text:<35}{lii_text}\n"

        # Adding remaining List-II item if exists
        if len(list_ii_items) > len(list_i_items):
            formatted_list += f"{'':<35}{list_ii_items[-1][0]}\n"

        # Finding and formatting the codes section
        codes_section = re.search(r'(Codes:\n(?:\(a\).*\n)+)', content, flags=re.DOTALL).group(1)

        return f"{formatted_intro}\n\n{formatted_list}\n{codes_section}"

    # Apply the format_match function to each match of the pattern
    updated_text = re.sub(pattern, format_match, text, flags=re.MULTILINE | re.DOTALL)

    return updated_text


# Path to your original .txt file and the path for the updated file
original_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text2.txt'
updated_file_path = r'F:\Question Bank trials\ExtractList\OutputFiles\updated_text.txt'


# Read the original text
with open(original_file_path, 'r', encoding='utf-8') as file:
    original_text = file.read()

# Reformat the text
updated_text = reformat_question(original_text)

# Save the updated text to a new file
with open(updated_file_path, 'w', encoding='utf-8') as file:
    file.write(updated_text)

print(f"Updated text saved to {updated_file_path}")
