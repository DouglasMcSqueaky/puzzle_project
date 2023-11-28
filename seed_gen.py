from mnemonic import Mnemonic

def convert_to_seed(mnemonics):
    mnemo = Mnemonic("english")
    seeds = []
    for mnemonic in mnemonics:
        seed = mnemo.to_seed(mnemonic, passphrase="")
        seeds.append(seed.hex())
    return seeds

input_file = 'valid_puzzle_mnemonics.txt'  # Replace with your file containing 12-word mnemonics
output_file = 'puzzle_seeds.txt'

try:
    with open(input_file, 'r') as file:
        mnemonics = file.read().splitlines()

    seeds = convert_to_seed(mnemonics)

    with open(output_file, 'w') as output:
        for seed in seeds:
            output.write(seed + '\n')

    print(f"BIP39 seeds written to '{output_file}'")

except FileNotFoundError:
    print("File not found. Please provide a valid path to the input file.")

