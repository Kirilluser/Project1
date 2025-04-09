import string
import os
import csv
from collections import Counter

def load_stopword(filepath = 'stopwords.txt'):
    try:
        with open(filepath,'r',encoding='utf-8') as fil:
            return set(word.strip().lower() for word in fil if word.strip())
    except FileNotFoundError:
        print(f"file: {filepath} is not found")
        return set()
def clean_text(text):
    translator = str.maketrans('','',string.punctuation +  "—«»“”")
    return text.translate(translator).lower()
def get_word_statistics(text):
    stopwords = load_stopword()
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    filtered_words = [word for word in words if word not in stopwords]
    word_counts = Counter(filtered_words)
    top_10 = word_counts.most_common(10)
    os.makedirs("results", exist_ok=True)
    with open("results/frequient_words.csv", "w", encoding='utf-8', newline="") as fi:
        writer = csv.writer(fi)
        writer.writerow(["Слово","Частота"])
        for word, freq in top_10:
            writer.writerow([word, freq])
    lines = text.strip().splitlines()
    total_lines = len(lines)
    total_words = len(words)
    total_chars = len(text)
    total_chars_without_spaces = len(text.replace(" ","").replace("\n",""))


    return{
        "lines": total_lines,
        "words": total_words,
        "chars": total_chars,
        "chars_without_spaces": total_chars_without_spaces,
        "top_10_words": top_10
    }

