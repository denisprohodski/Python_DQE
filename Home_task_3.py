import re

text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


lines = text.split('\n')
# print(lines)
normalized_lines = []
for line in lines:
    line = line.strip()
    if line:
        line = line[0].upper() + line[1:].lower()
        normalized_lines.append(line)

normalized_text = '\n'.join(normalized_lines)
# print(normalized_text)


sentences = re.split(r'[.!?]', normalized_text)
sentences = [s.strip() for s in sentences if s.strip()]

last_words = [sentence.split()[-1] for sentence in sentences]
new_sentence = ' '.join(last_words) + '.'
# print(new_sentence)
normalized_text += '\n\n' + new_sentence.capitalize()

corrected_text = re.sub(r'\b[iI][zZ]\b', 'is', normalized_text)

whitespace_count = sum(1 for char in corrected_text if char.isspace())

print(corrected_text)
print(f"Number of whitespace characters:", whitespace_count)