from time import sleep
from selenium import webdriver

visited_urls = []

driver = webdriver.Chrome() 
# urls = ['https://ru.wikipedia.org/wiki/Кошка'] - !!! в адресе нельзя использовать кириллицу
urls = ['https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0']

while urls:
    url = urls.pop(0) # достаем 0й элемент из списка ссылок
    visited_urls.append(url) # добавляем ссылку в список посещенных ()
    driver.get(url) # переходим по ссылке (запуститься браузер)
    sleep(3) # нужно немного подождать
    ps = driver.find_elements('xpath', '//p')  # находим на сайте все теги <p>
    for p in ps:
        # Для добавления информации используем режим a
        with open('wiki.txt', 'a', encoding='utf-8') as f :
            f.write(p.text)
        print(p.text)
    imgs = driver.find_elements('xpath', '//img') # находим на сайте все теги <img>
    for img in imgs:
        with open('wiki_img.txt', 'a', encoding='utf-8') as f:
            f.write(img.get_attribute('src'))
        print(img.get_attribute('src'))
    elements = driver.find_elements('xpath', '//a') # находим на сайте все теги <a> (ссылки)
    for element in elements:
        href = element.get_attribute('href')
        if href is None: # Если ссылка пустая
            continue
        if '#' in href: # Если есть решетка значит ссылка внутри той же страницы
            continue
        if 'wikipedia' in href and href not in visited_urls:
            urls.append(href)
            urls = list(set(urls))
