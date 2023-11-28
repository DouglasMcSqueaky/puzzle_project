from docx import Document
from docx.shared import RGBColor

# Read the list of words from the .txt file
with open('reduced_puzzle_words.txt', 'r') as file:
    words_to_find = file.read().splitlines()

# Open the .docx file
doc = Document('Puzzle Story (copy).docx')

# Loop through paragraphs
for paragraph in doc.paragraphs:
    for word_to_find in words_to_find:
        for run in paragraph.runs:
            if word_to_find in run.text.split():
                # Split text by spaces to match whole words
                words = run.text.split()
                for i, word in enumerate(words):
                    if word_to_find == word:
                        # Bold and change font color to red
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 0, 0)  # Red color

# Save the modified document
doc.save('modified_document.docx')

