def assemble_sentence(word_list):
    import random
    return ' '.join(random.sample(word_list, 12))

def generate_sentences(word_list, num_sentences):
    sentences = set()
    while len(sentences) < num_sentences:
        sentence = assemble_sentence(word_list)
        sentences.add(sentence)
    return list(sentences)

def write_sentences_to_file(sentences, output_file):
    with open(output_file, 'w') as file:
        for sentence in sentences:
            file.write(sentence + '\n')

# Reading words from a text file
word_file_path = 'reduced_puzzle_words.txt'  # Replace with your word file path

try:
    with open(word_file_path, 'r') as word_file:
        word_list = word_file.read().splitlines()

    num_sentences_input = input("How many sentences would you like to generate?: ")
    num_sentences = int(num_sentences_input)

    if num_sentences <= 0:
        raise ValueError

    sentences = generate_sentences(word_list, num_sentences)
    output_file = 'generated_sentences.txt'
    write_sentences_to_file(sentences, output_file)
    print(f"{num_sentences} unique sentences generated. Saved to {output_file}")

except FileNotFoundError:
    print("File not found. Please provide a valid path to the word file.")
except ValueError:
    print("Please enter a valid positive integer for the number of sentences.")

