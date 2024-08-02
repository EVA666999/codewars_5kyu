from bs4 import BeautifulSoup
import requests

def get_member_since(username):
    # Форматирование URL с помощью f-строки
    url = f'https://www.codewars.com/users/{username}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    # Найти все элементы с классом 'stat'
    allNews = soup.findAll('div', class_='stat')
    
    # Проверка содержимого каждого элемента
    for data in allNews:
        if 'Member Since:' in data.get_text():
            # Получаем текст после "Member Since:"
            member_since = data.get_text(strip=True).split('Member Since:')[1].strip()
            return member_since

    # Возвращаем None, если элемент не найден
    return None

# Вызов функции и печать результата
print(get_member_since(username='EVA666999'))
