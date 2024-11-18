from collections import Counter
from nltk.util import ngrams

def generate_ngrams_from_file(file_path, n):

    try:
        # Read the content of the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Tokenize the text into words
        tokens = text.split()
        
        # Generate n-grams
        n_grams = ngrams(tokens, n)
        
        # Count frequencies of n-grams
        ngram_freq = Counter(n_grams)
        
        return ngram_freq
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return {}

# Ask user for file location and N value
file_path = input("Enter the file location (full path): ").strip()
n = int(input("Enter the size of N-Grams (e.g., 2 for Bi-Grams): "))

# Generate and print N-Grams
ngrams_output = generate_ngrams_from_file(file_path, n)
if ngrams_output:
    print(f"\n{n}-Grams and their frequencies:")
    for ngram, freq in ngrams_output.items():
        print(f"{ngram}: {freq}")

#OUTPUT
# Enter the file location (full path): Textfile.txt
# Enter the size of N-Grams (e.g., 2 for Bi-Grams): 3

# 3-Grams and their frequencies:
# ('Natural', 'Language', 'Processing'): 1
# ('Language', 'Processing', '(NLP)'): 1
# ('Processing', '(NLP)', 'is'): 1
# ('(NLP)', 'is', 'a'): 1
# ('is', 'a', 'field'): 1
# ('a', 'field', 'of'): 1
# ('field', 'of', 'Artificial'): 1
# ('of', 'Artificial', 'Intelligence'): 1
# ('Artificial', 'Intelligence', 'that'): 1
# ('Intelligence', 'that', 'focuses'): 1
# ('that', 'focuses', 'on'): 1
# ('focuses', 'on', 'the'): 1
# ('on', 'the', 'interaction'): 1
# ('the', 'interaction', 'between'): 1
# ('interaction', 'between', 'computers'): 1
# ('between', 'computers', 'and'): 1
# ('computers', 'and', 'humans'): 1
# ('and', 'humans', 'using'): 1
# ('humans', 'using', 'natural'): 1
# ('using', 'natural', 'language.'): 1
# ('natural', 'language.', 'It'): 1
# ('language.', 'It', 'enables'): 1
# ('It', 'enables', 'machines'): 1
# ('enables', 'machines', 'to'): 1
# ('machines', 'to', 'understand,'): 1
# ('to', 'understand,', 'interpret,'): 1
# ('understand,', 'interpret,', 'and'): 1
# ('interpret,', 'and', 'generate'): 1
# ('and', 'generate', 'human'): 1
# ('generate', 'human', 'language'): 1
# ('human', 'language', 'in'): 1
# ('language', 'in', 'a'): 1
# ('in', 'a', 'way'): 1
# ('a', 'way', 'that'): 1
# ('way', 'that', 'is'): 1
# ('that', 'is', 'meaningful.'): 1
# ('is', 'meaningful.', 'Applications'): 1
# ('meaningful.', 'Applications', 'of'): 1
# ('Applications', 'of', 'NLP'): 1
# ('of', 'NLP', 'include'): 1
# ('NLP', 'include', 'language'): 1
# ('include', 'language', 'translation,'): 1
# ('language', 'translation,', 'sentiment'): 1
# ('translation,', 'sentiment', 'analysis,'): 1
# ('sentiment', 'analysis,', 'speech'): 1
# ('analysis,', 'speech', 'recognition,'): 1
# ('speech', 'recognition,', 'and'): 1
# ('recognition,', 'and', 'chatbots.'): 1