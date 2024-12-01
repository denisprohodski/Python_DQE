import random
import string

num_dicts = random.randint(2, 10)
num_keys = random.randint(1, 5)
dicts_list = []

for i in range(num_dicts):
    new_dict = {}
    for i in range(num_keys):
        key = random.choice(string.ascii_lowercase)
        value = random.randint(0, 100)
        new_dict[key] = value
    dicts_list.append(new_dict)

# print(dicts_list)

combined_dict = {}

for dict_index, single_dict in enumerate(dicts_list, start=1):
    for key, value in single_dict.items():
        if key in combined_dict:
            if value > combined_dict[key][0]:
                combined_dict[key] = (value, dict_index)
        else:
            combined_dict[key] = (value, dict_index)

renamed_dict = {}
for key, (value, dict_index) in combined_dict.items():
    if len([d for d in dicts_list if key in d]) > 1:
        renamed_key = f"{key}_{dict_index}"
    else:
        renamed_key = key
    renamed_dict[renamed_key] = value

print(dicts_list)
print(renamed_dict)