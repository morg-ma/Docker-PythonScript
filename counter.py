from collections import Counter

def count_word(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found")
        return

    # Count the frequency of each word
    word_freq = Counter()

    for line in lines:
        # get the words in each line
        words = line.strip().split()

        # normalize the words
        norm_words = [word.lower() for word in words]

        word_freq.update(norm_words)

    # Display word frequency count
    for word, frequency in word_freq.most_common():
        print(f"{word}: {frequency}")

count_word("filtered_text.txt")