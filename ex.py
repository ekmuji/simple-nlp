"""
Text Processing using NLTK and SQLite
------------------------------------------
This script demonstrates:
- Downloading and reading a text corpus (Project Gutenberg)
- Tokenization, stopword removal, stemming, and lemmatization
- POS tagging and POS-based lemmatization
- Storing and retrieving data from a SQLite database
"""

import nltk
from urllib import request
import sqlite3
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# 1. Setup NLTK resources

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("universal_tagset")

# 2. Load a Gutenberg text (Frankenstein by Mary Shelley)

url = "http://www.gutenberg.org/files/84/84-0.txt"
content = request.urlopen(url).read().decode("utf-8", errors="ignore")

print(f"Downloaded Gutenberg text: {len(content)} characters long.")

# Optionally, save it to a local file
with open("document.txt", "w", encoding="utf-8") as f:
    f.write(content)

# 3. Create a SQLite database and insert a sample record

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Corpus (
    documentId TEXT,
    documentContent TEXT,
    documentTopic TEXT
)
""")

cursor.execute(
    'INSERT INTO Corpus VALUES ("doc1", "This is an example document for the corpus.", "Example")'
)

connection.commit()
connection.close()
print("Database 'database.db' created and record inserted.")

# 4. Tokenization and stopword filtering

text = "Artificial intelligence is cool but I am not too keen on Skynet."
tokens = word_tokenize(text)

# Convert to lowercase and filter stopwords
tokens_without_sw = [word.lower() for word in tokens if word.lower() not in stopwords.words("english")]
print("\nTokens after stopword removal:")
print(tokens_without_sw)

filtered_sentence = " ".join(tokens_without_sw)
print("\nFiltered sentence:")
print(filtered_sentence)

# Count word occurrences
text_obj = nltk.Text(tokens_without_sw)
print("\nOccurrences of 'cool':", text_obj.count("cool"))

# 5. Stemming examples

p_stemmer = PorterStemmer()
sb_stemmer = SnowballStemmer("english")

sentence = "This is a test sentence, and I am hoping it doesn't get chopped up too much."
print("\nOriginal sentence (for stemming):")
print(sentence)

print("\nStemmed tokens:")
for token in word_tokenize(sentence):
    print(f"{token:15} | Porter: {p_stemmer.stem(token):10} | Snowball: {sb_stemmer.stem(token):10}")

# 6. Lemmatization examples

lemmatiser = WordNetLemmatizer()
sentence = "I am writing a few words, and I am hoping they don't get chopped up too much."
print("\nOriginal sentence (for lemmatization):")
print(sentence)

print("\nLemmatized tokens:")
for token in word_tokenize(sentence):
    print(lemmatiser.lemmatize(token))

# 7. POS tagging and POS-aware lemmatization

pos_tags = nltk.pos_tag(word_tokenize(sentence), tagset="universal")
print("\nPart-of-speech tags:")
print(pos_tags)

posmap = {
    "ADJ": "a",
    "ADV": "r",
    "NOUN": "n",
    "VERB": "v"
}

print("\nPOS-based lemmatization:")
for word, tag in pos_tags:
    if tag in posmap:
        print(f"{word:15} → {lemmatiser.lemmatize(word, posmap[tag])}")
    else:
        print(f"{word:15} → {lemmatiser.lemmatize(word)}")

# 8. Example: Counting words ending with 'ing'

sentence = "This is a test sentence, and I am hoping it doesn't get chopped up too much."
tokens = word_tokenize(sentence)
ing_count = sum(1 for token in tokens if token.endswith("ing"))

print(f"\nNumber of words ending in 'ing': {ing_count}")
