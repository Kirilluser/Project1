import os
import re

def extract_name(text):
    name_pattern = r'\b[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+\b' #тут паттерн имя фамилия
    names = re.findall(name_pattern, text)
    unique_names = sorted(set(names))
    save_results(unique_names, 'results/names.txt')
    return unique_names
def extract_dates(text):
    num_date_pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b' #тут дата в цифровом формате
    text_date_pattern = r'\b\d{1,2} (?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) \d{4}\b' #тут цифра слово
    dates = re.findall(num_date_pattern, text)
    dates += re.findall(text_date_pattern, text)
    unique_dates = sorted(set(dates))
    save_results(unique_dates, 'results/dates.txt')
    return unique_dates
def save_results(data,filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w',encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")