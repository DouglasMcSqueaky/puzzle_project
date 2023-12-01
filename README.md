# puzzle_project
some research related to the wallet puzzle located here: https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254

This Bitcoin seed puzzle has been posted for a few years but has not been solved. I played with some Python scripts in an attempt to brute force the seed phrase. Brute forcing in this manner is highly unlikely to succeed so this is more for entertainment/education. 

The first step is to save all text from the link above to a .txt document locally. Then using Python the idea is to scan the entire document, identify valid BIP39 seed words, isolate those words in a new document, and finally generate valid seed phrase combinations from those words. 

