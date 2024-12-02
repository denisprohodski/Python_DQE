import random
import string
import re

def generate_random_dicts(num_dicts: int, num_keys: int) -> list[dict]:
    dicts_list = []
    for i in range(num_dicts):
        new_dict = {}
        for i in range(num_keys):
            key = random.choice(string.ascii_lowercase)
            value = random.randint(0, 100)
            new_dict[key] = value
        dicts_list.append(new_dict)
    return dicts_list

def combine_dicts(dicts_list: list[dict]) -> dict:
    combined_dict = {}

    for dict_index, single_dict in enumerate(dicts_list, start=1):
        for key, value in single_dict.items():
            if key in combined_dict:
                if value > combined_dict[key][0]:
                    combined_dict[key] = (value, dict_index)
            else:
                combined_dict[key] = (value, dict_index)
    return combined_dict

def rename_keys(combined_dict: dict, dicts_list: list[dict]) -> dict:
    renamed_dict = {}
    for key, (value, dict_index) in combined_dict.items():
        if len([d for d in dicts_list if key in d]) > 1:
            renamed_key = f"{key}_{dict_index}"
        else:
            renamed_key = key
        renamed_dict[renamed_key] = value
    return renamed_dict

num_dicts = random.randint(2, 10)
num_keys = random.randint(1, 5)
dicts_list = generate_random_dicts(num_dicts, num_keys)
combined_dict = combine_dicts(dicts_list)
renamed_dict= rename_keys(combined_dict, dicts_list)
# print(dicts_list)
# print(combined_dict)
print(renamed_dict)



def normalize_text(text: str) -> str:
    lines = text.split('\n')
    normalized_lines = [line.strip().capitalize() for line in lines if line.strip()]
    return '\n'.join(normalized_lines)

def extract_last_words(normalized_text: str) -> str:
    sentences = re.split(r'[.!?]', normalized_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    last_words = [sentence.split()[-1] for sentence in sentences]
    new_sentence = ' '.join(last_words) + '.'
    return normalized_text + '\n\n' + new_sentence.capitalize()

def correct_misspelling(text: str) -> str:
    return re.sub(r'\b[iI][zZ]\b', 'is', text)

def count_whitespace(text: str) -> str:
    return sum(1 for char in text if char.isspace())


text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

normalized_text = normalize_text(text)
extended_text = extract_last_words(normalized_text)
corrected_text = correct_misspelling(extended_text)
whitespace_count = count_whitespace(corrected_text)

print(corrected_text)
print(whitespace_count)