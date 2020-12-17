words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        print(bytes(word, encoding='ASCII'))
    except UnicodeEncodeError:
        print(f'{word} can not bytes encode')