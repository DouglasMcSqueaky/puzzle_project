from bip32utils import BIP32Key
from mnemonic import Mnemonic
import hashlib

def derive_private_key_from_seed(seed_phrase):
    mnemo = Mnemonic("english")
    seed_bytes = mnemo.to_seed(seed_phrase, passphrase="")
    root_key = BIP32Key.fromEntropy(seed_bytes)
    child_key = root_key.ChildKey(0)
    return child_key.WalletImportFormat()

input_file = 'generated_sentences.txt'  # Replace with your file containing 12-word seed phrases

try:
    with open(input_file, 'r') as file:
        seed_phrases = file.read().splitlines()

    for seed_phrase in seed_phrases:
        private_key = derive_private_key_from_seed(seed_phrase)
        print(f"12-word phrase: {seed_phrase}")
        print(f"Private Key: {private_key}")
        print("\n")

except FileNotFoundError:
    print("File not found. Please provide a valid path to the input file.")

