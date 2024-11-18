# NLP_NgramModelUsingFileInput
This script generates N-Grams from a text file and counts their frequencies.

This script reads a text file, generates N-Grams (sequences of N words), and calculates their frequencies using Python's collections.Counter and NLTK.
Steps:
1. File Handling: The script prompts the user to input the file path and the desired N-Gram size (n).
The file is read and its contents are stored as a string.
2. Tokenization: The input text is split into words using Python's built-in split() method. This generates a list of tokens (words).
3. N-Gram Generation: The ngrams() function from NLTK is used to generate N-Grams from the list of tokens. This function creates all possible sequences of n consecutive words.
4. Frequency Count: The Counter class from the collections module is used to count the frequency of each N-Gram.
5. Error Handling: If the file is not found, a FileNotFoundError is caught, and an error message is displayed.
Output: The generated N-Grams and their frequencies are printed.

Notes:
File Path: Ensure the file path is correct, and the file is readable.
N-Grams: You can adjust the value of n to extract different lengths of word sequences (e.g., Bi-Grams for n=2 or Tri-Grams for n=3).
Applications: This can be used in text analysis, language modeling, or identifying frequently occurring word sequences in documents.
