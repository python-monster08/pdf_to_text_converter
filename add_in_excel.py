# import re
# import pandas as pd
#
#
# # Function to extract data from text
# def extract_data_from_text(text):
#     # Regex patterns for different parts of the question
#     question_pattern = r"Please examine the combination of the following Lists and(.+?)U\.P \.P \.C\.S\. \(Mains\) (\d{4})\s+Answer -\((\w)\)"
#
#     # Search for patterns in the text
#     match = re.search(question_pattern, text, re.DOTALL)
#     if not match:
#         raise ValueError("Pattern not found in the text.")
#
#     question_text, year, correct_answer = match.groups()
#
#     # Extracted data dictionary
#     extracted_data = {
#         "exam_year": year,
#         "exam_name": "UPSC",
#         "exam_stage": "Mains",
#         "subject_area": "HI",
#         "part": "GS1",
#         "sub_topic": "Ancient",
#         "question_type": "list_type_2",
#         "question": question_text.strip(),
#         "correct_answer_option": correct_answer
#     }
#
#     return extracted_data
#
#
# # Function to save extracted data to an Excel file
# def save_to_excel(data, filename):
#     df = pd.DataFrame([data])
#     df.to_excel(filename, index=False)
#
#
# # Main function to read the file, extract data, and save to Excel
# def process_file(filepath, output_excel):
#     with open(filepath, 'r', encoding='utf-8') as file:
#         text = file.read()
#
#     extracted_data = extract_data_from_text(text)
#     save_to_excel(extracted_data, output_excel)
#
#
# # Replace 'your_file.txt' with the path to your actual text file
# input_file = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_text1.txt'
# output_excel = r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_data.xlsx'
#
# # Process the file
# process_file(input_file, output_excel)


import re
import pandas as pd

def extract_data_from_text(text):
    # Assuming 'question_main_part' and 'all_answers_str' are defined elsewhere in your function

    # Regular expression pattern to match exactly four answer options
    # This pattern assumes that each answer option is in the format "(letter) number number number number"
    # Adjust the pattern if your actual answer options are formatted differently
    answer_pattern = r"\(([abcd])\)\s*(\d+,\s*\d+,\s*\d+,\s*\d+)"

    all_answers_matches = re.findall(answer_pattern, text)

    # Ensure exactly four answer options are found
    if len(all_answers_matches) != 4:
        raise ValueError(f"Expected 4 answer options, but found {len(all_answers_matches)}")

    # Unpack the matched answer options
    # Note: This unpacks a list of tuples (letter, answer sequence) into two separate lists
    letters, answer_options = zip(*all_answers_matches)

    # Convert the answer sequences into a single string for 'all_answers_str'
    all_answers_str = "\n".join([f"({letter}) {option}" for letter, option in all_answers_matches])

    # Extracting the year and correct answer
    year = re.search(r"(\d{4})", text).group(1)
    correct_answer = re.search(r"Answer -\(([abcd])\)", text).group(1)

    # Assembling the data dictionary with the extracted information
    extracted_data = {
        "exam_year": year,
        "exam_name": "UPSC",
        "exam_stage": "Mains",
        "subject_area": "HI",
        # Add other fields as required
        "all_answers": all_answers_str,
        "answer_option_a": answer_options[0],
        "answer_option_b": answer_options[1],
        "answer_option_c": answer_options[2],
        "answer_option_d": answer_options[3],
        "correct_answer_option": correct_answer,
        # Add other fields as required
    }

    return extracted_data

def save_to_excel(data, filename):
    df = pd.DataFrame([data])
    df.to_excel(filename, index=False)



# Replace 'your_text' with the actual content of your .txt file
your_text = """
1. The Mughal school of painting formed the spinal column of
different schools of Indian miniature art. Which one of the
following painting styles was not affected by Mughal
painting? [1995]
(a) Pahari (b) Rajasthani
(c) Kangra (d) Kalighata

2. Who among the following were famous jurists of medieval
India? [1995]
(a) Vijnanesvara (b) Hemadri
(c) Rajasekhara (d) Jimutavahana
Select the correct answer using the codes given below:
(a) 1, 2 and 3 (b) 2, 3 and 4
(c) 1, 2 and 4 (d) 1 and 4

3. Which one of the following monuments has a dome which
is said to be one of the largest in the world? [1995]
(a) Tomb of Sher Shah, Sasaram
(b) Jama Masjid, Delhi
(c) Tomb of Ghiyas-ud-din Tughlaq, Delhi
(d) Gol Gumbaz, Bijapur

4. Ashtapradhan was a council of ministers:
[1995]
(a) in the Gupta administration
(b) in the Chola administration
(c) in the Vijayanagar administration
(d) in the Maratha administration

5. Consider the map given below:
[1995]
The route indicated in the map was followed, during the
course of his military exploits, by:
(a) Chandragupta II (b) Harshavardhana
(c) Rajendra Chola (d) Malik Kafur

6. The term 'Apabhramsa' was used in medieval Sanskrit texts
to denote: [1996]
(a) outcastes among the Rajputs
(b) deviations from V edic rituals
(c) early forms of some of the modern Indian language
(d) non-Sanskrit verse metres

7. Nastaliq was:
[1996]
(a) a persian script used in medieval India
(b) a raga composed by Tansen(c) a cess levied by the Mughal rulers
(d) a manual of code of conduct for the Ulemas

8. The sufi saint who maintained that devotional music was
one way of coming close to God was; [1996]
(a) Muin-ud-din Chisti
(b) Baba Farid
(c) Saiyid Muhammad Gesudaraz
(d) Shah Alam Bukhari

9. Mughal painting reached its zenith under:
[1996]
(a) Humayun (b) Akbar
(c) Jahangir (d) Shahjahan

10. In medieval India, Mansabdari system was introduced for:
(a) making recruitment to the army [1996]
(b) facilitating revenue collection
(c) ensuring religious harmony
(d) effecting clean administration

11. Which of the following pairs is correctly matched?
(a) Guru Amar Das–Miri and Piri [1996]
(b) Guru Arjun Dev–Adi Granth
(c) Guru Ram Das–Dal Khalsa
(d) Guru Gobind Singh– Manji

12. Prem Vatika, poems on the life of Krishna, were composed by :
(a) Bihari (b) Surdas [1996]
(c) Raskhan (d) Kabir

13. After consolidating his power, Balban assumed the grand
title of : [1997]
(a) Tute-Hind (b) Kaisr-I-Hind
(c) Zil-I-Ilahi (d) Din-I-Ilahi

14. Head of the military department under the recognised central
machinery of administration during Akbar's reign was:
(a) Diwan (b) Mir Bakshi [1997]
(c) Mir Saman (d) Bakshi

15. Assertion (A): The sponsor and the most prominent figure
of the Chisti order of Sufis in India is Khwaja Moinuddin
Chisti.
Reason (R): The Chisti order takes its name from a village
Chisti in Ajmer.
In the context of the above two statements, which one of
the following is correct? [1997]
(a) Both A and R are true but R is the correct explanation
of A
(b) Both A and R are true but R is not the correct explanation
of A
(c) A is true but R is false
(d) A is false but R is true

16. Which one of the following pairs of composers in different
languages and their works on the Mahabharata theme is
correctly matched? [1997]
(a) Sarladasa–Bengali (b) Kasirama–Oriya
(c) Tikkana–Marathi (d) Pampa–Kannada2 



17. The medieval Indian writer who refers to the discovery of
America is : [1997]
(a) Malik Muhammad Jayasi
(b) Amir Khusrau
(c) Raskhan
(d) Abul Fazl

18. The member of Shivaji's Ashtapradhan who looked after
foreign affairs was: [1998]
(a) Peshwa (b) Sachiv
(c) Pandit Rao (d) Sumant

19. The loss of Qandhar was a big blow to the Mughal empire
from the view point of : [1998]
(a) natural resources (b) buffer territory
(c) communication (d) strategic stronghold

20. Fawazil in the Sultanate period meant:
[1998]
(a) extra payment to the nobles
(b) revenue assigned in lieu of salary
(c) excess amount paid to the exchequer by the Iqtadars
(d) illegal exactions extracted from the peasants

21. Sultan of Delhi who is reputed to have built the biggest
network of canals in India was: [1998]
(a) Iltutmish
(b) Ghiyasuddin Tughlaq
(c) Firoz Shah Tughlaq
(d) Sikandar Lodi

22. Assertion (A): At first the Turkish administration in India
was essentially military .
Reason (R): The country was parcelled out as 'Iqtas' among
leading military leaders. [1998]
(a) Both A and R are true but R is the correct explanation of A
(b) Both A and R are true but R is not a correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

23. Assertion (A): During the reign of Shahjahan, Dara Sikoh
was sent on expedition to Balkha, Badakhshan and
Qandahar.
Reason (R): The expedition sent by Shahjahan to the
Middle-East was a marvellous success. [1998]
(a) Both A and R are true but R is the correct explanation of A
(b) Both A and R are true but R is not a correct explanation
of A
(c) A is true but R is false
(d) A is false but R is true

24. Consider the following statements:
[1998]
Ahadis were those troopers who:

1. offered their services singly

2. did not attach themselves to any chief

3. had the emperor as their immediate colonel

4. attached themselves to Mirzas
Of these statements:
(a) 1, 3 and 4 are correct
(b) 1, 2 and 3 are correct
(c) 2 and 3 are correct
(d) 1 and 4 are correct

25. Consider the following:
[1998]

1. Tughlaqabad fort 
2. Lodi Garden

3. Qutab Minar 
4. Fatehpur Sikri
The correct chronological order in which they were built is :
(a) 3, 1, 4, 2 (b) 3, 1, 2, 4
(c) 1, 3, 2, 4 (d) 1, 3, 4, 2

26. Match List-I with List-II and select the correct answer using
the codes given below the lists:[1998]
List-I                      List-II
(years)                     (wors)
A . 1556            1. Battle of Haldi Ghati
B. 1600             2. Nadir Shah's capture of Delhi
C. 1686             3. Death of Shivaji
D. 1739             4. Grant of Charter to East India Company
                    5. Accession of Akbar
Codes:
(a) A – 3; B – 4; C – 2; D – 1
(b) A – 5; B – 4; C – 3; D – 2
(c) A – 5; B – 2; C – 1; D – 4
(d) A – 1; B – 5; C – 3; D – 2
U.P .P .C.S. (Mains) 2010
Answer -(d)

27. In the given map, the shaded part represents Akbar's empire
at a certain juncture, A stands for an independent country
and 'B' marks the site of city . Which one of the following
alternative gives all correct information? [1998]
(a) Akbar in 1557 : (A) Gokunda, (B) Lahore
(b) Akbar in 1557 : (A) Khandesh, (B) Multan
(c) Akbar in 1605: (A) Gondwana, (B) Multan
(d) Akbar in 1605: (A) Gondwana, (B) Lahore

28. The first writer to use Urdu as the medium of poetic
expression was: [1999]
(a) Amir Khusrau (b) Mirza Ghalib
(c) Bahadur Shah Zafar (d) Faiz

29. To which Lodi Sultan does the given map relate and what
town does the site marked. A represent [1999]
A on the map represent?
(a) Bahlol Lodi – Jaunpur
(b) Sikandar Lodi – Aligarh
(c) Ibrahim Lodi – Jaunpur
(d) Ibrahim Lodi – Aligarh

30. Assertion (A): During the time of Akbar, for every ten
cavalrymen, the mansabdars had to maintain twenty horses.
Reason (R): Horses had to be rested while on march and
replacements' were necessary in times of war. [1999]
(a) Both A and R are true but R is the correct explanation
of A
(b) Both A and R are true but R is not a correct explanation
of A
(c) A is true but R is false
(d) A is false but R is true

31. Please examine the combination of the following Lists and accordingly
select the correct Code:
List I    List II
(crop)   (state)
A. Groundnut   1. Andhra Pradesh
B. Mustard   2. Rajasthan
C. Soyabean   3. Madhya Pradesh
D. Cocunut   4. Kerala
Code : A B C D
a) 1 3 2 4
b) 2 1 3 4
c) 1 2 3 4
d) 4 3 2 1
U.P .P .C.S. (Mains) 2008
Answer -(c)
"""

# Extract data and save to Excel
extracted_data = extract_data_from_text(your_text)
save_to_excel(extracted_data, r'F:\Question Bank trials\ExtractList\OutputFiles\extracted_data.xlsx')
