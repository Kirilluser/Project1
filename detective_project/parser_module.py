import re
import os

def extract_names(text):
    # Регулярное выражение для имён и фамилий (например: Иван Иванов)
    name_pattern = r'\b[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+\b'
    names = re.findall(name_pattern, text)
    unique_names = sorted(set(names))
    save_results(unique_names, 'results/names.txt')
    return unique_names

def extract_dates(text):
    # Формат: 01.01.2023
    numeric_date_pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b'
    # Формат: 5 января 2023
    text_date_pattern = r'\b\d{1,2} (?:января|февраля|марта|апреля|мая|июня|' \
                        r'июля|августа|сентября|октября|ноября|декабря) \d{4}\b'
    dates = re.findall(numeric_date_pattern, text)
    dates += re.findall(text_date_pattern, text)
    unique_dates = sorted(set(dates))
    save_results(unique_dates, 'results/dates.txt')
    return unique_dates

def save_results(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")
