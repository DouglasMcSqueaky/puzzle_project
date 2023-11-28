from mnemonic import Mnemonic

def validate_mnemonics(mnemonics):
    valid_mnemonics = []
    mnemo = Mnemonic("english")
    for mnemonic in mnemonics:
        if mnemo.check(mnemonic):
            valid_mnemonics.append(mnemonic)
    return valid_mnemonics

input_file = 'generated_sentences.txt'  # Replace with your file containing 12-word mnemonics

try:
    with open(input_file, 'r') as file:
        mnemonics = file.read().splitlines()

    valid_mnemonics = validate_mnemonics(mnemonics)

    print("Valid Mnemonics:")
    for mnemonic in valid_mnemonics:
        print(mnemonic)

except FileNotFoundError:
    print("File not found. Please provide a valid path to the input file.")

