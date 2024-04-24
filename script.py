import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords corpus
nltk.download('stopwords')
nltk.download('punkt')

def read_text_file(path):
    try:
        with open(path, 'r') as file:
            text = file.read()
        return text
    
    except FileNotFoundError:
        print("Error: File not found")
        return None

def filter_data(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Get English stopwords
    stop_words = set(stopwords.words('english'))

    # get the punctuations
    punctuations = set(string.punctuation)

    # Remove stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words and word not in punctuations]

    # Join the words back into a single string
    filtered_text = ' '.join(filtered_words)
    return filtered_text

def save_filtered_text(text, filepath):
    with open(filepath, 'w') as file:
        file.write(text)


# main
text = read_text_file("paragraphs.txt")
filtered_text = filter_data(text)
save_filtered_text(filtered_text, "filtered_text.txt")