from docx import Document
from docx.shared import RGBColor
import re

# Read the list of words from the .txt file
with open('word_list.txt', 'r') as file:
    words_to_find = file.read().splitlines()

# Open the .docx file
doc = Document('your_document.docx')

# Function to apply formatting to matching words
def apply_formatting_to_word(run, word):
    if word in run.text:
        # Find all occurrences of the word with regex
        matches = re.finditer(r'\b{}\b'.format(re.escape(word)), run.text)
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            # Bold and change font color to red for the matching word
            run.text = run.text[:start_index] + run.text[start_index:end_index].replace(word, f"<b><font color=red>{word}</font></b>") + run.text[end_index:]
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 0, 0)  # Red color

# Loop through paragraphs
for paragraph in doc.paragraphs:
    for word_to_find in words_to_find:
        for run in paragraph.runs:
            apply_formatting_to_word(run, word_to_find)

# Save the modified document
doc.save('modified_document.docx')

