from random import sample

from parser_module import extract_name, extract_dates
from analyzer_module import get_word_statistics
import os

def read_file(filepath):
    if not os.path.isfile(filepath):
        print(f"[!] File {filepath} is nor found")
        return None
    with open(filepath,'r',encoding='utf-8') as f:
        return f.read()
def generate_report(names, dates, stats):
    os.makedirs("results", exist_ok=True)
    with open("results/report.txt","w", encoding='utf-8') as file:
        file.write(f"Найденно имен: {len(names)}\n")
        file.write(f"Найдено дат: {len(dates)}\n")
        file.write("Топ 10 слов:\n")
        for word, freq in stats["top_10_words"]:
            file.write(f" - {word}:{freq}\n")
        file.write(f"Всего строk:{stats['lines']}\n")
        file.write(f"Всего слов: {stats['words']}\n")
        file.write(f"Всего символов: {stats['chars']}\n")
        file.write(f"Всего символов без пробелов: {stats['chars_without_spaces']}\n")
def run_analys(filepath ="sample.txt"):
    text = read_file(filepath)
    if text is None:
        return
    print("Analys has started")
    names = extract_name(text)
    dates = extract_dates(text)
    stats = get_word_statistics(text)
    generate_report(names,dates,stats)
    print("Analys finished\nreport saved in report.txt")

def menu():
    while True:
        run_analys()
        choise = input("\n Analys another file? [y/n]: ").lower().strip()
        if choise == 'y':
            filepath = input("Input file dir").strip()
            run_analys(filepath)
        else:
            print("Closing program")
            break
if __name__ == "__main__":
    menu()