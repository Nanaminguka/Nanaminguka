import requests
from bs4 import BeautifulSoup

def download_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download page: {response.status_code}")

def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Извлечение заголовка страницы
    title = soup.title.text.strip()
    # Извлечение текста описания аниме
    description_element = soup.find('div', class_='full')
    description = description_element.text.strip() if description_element else "Description not found"
    # Извлечение небольшого текстового фрагмента (первый абзац)
    first_paragraph = soup.find('p').text.strip()
    # Добавление отступов с обеих сторон каждой строки текста
    title = add_indent(title)
    description = add_indent(description)
    first_paragraph = add_indent(first_paragraph)
    # Соединение всех частей текста с помощью пустых строк
    return f"{title}\n\n{description}\n\n{first_paragraph}"

def add_indent(text, indent_size=4):
    lines = text.split('\n')
    indented_lines = [f"{' ' * indent_size}{line}" for line in lines]
    return '\n'.join(indented_lines)

def save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def main(url, filename):
    html_content = download_page(url)
    extracted_data = extract_data(html_content)
    save_to_file(extracted_data, filename)

if __name__ == "__main__":
    url = 'https://www.anilibria.tv/release/jujutsu-kaisen.html'
    filename = 'output.txt'
