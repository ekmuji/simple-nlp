# simple-nlp
# Text Processing Demo using NLTK and SQLite

This project demonstrates key Natural Language Processing (NLP) techniques in Python using **NLTK** and simple data storage using **SQLite**.  
It includes downloading and processing a real text corpus, tokenization, stopword filtering, stemming, lemmatization, and part-of-speech tagging.


## Overview

This demo performs the following operations:

1. **Downloads a Project Gutenberg text** (Mary Shelley’s *Frankenstein*)  
2. **Stores text in a SQLite database** for simple corpus management  
3. **Tokenizes** text into words  
4. **Removes stopwords** (common words such as “the”, “and”, “is”)  
5. **Applies stemming** using Porter and Snowball stemmers  
6. **Applies lemmatization**, both basic and POS-tag–aware  
7. **Performs POS tagging** with NLTK’s universal tagset  
8. **Counts tokens** with specific suffixes (e.g. words ending in “-ing”)


## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ekmuji/simple-nlp.git
cd simple-nlp
```
### 2. Install dependencies
- nltk
- urllib
- sqlite3

### 3. Run project 
```bash
python simple-nlp.py
```
