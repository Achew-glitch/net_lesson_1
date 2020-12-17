words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    print(word)
    word = word.encode('utf-8')
    print(f'{word} encode in UTF-8')
    word = word.decode('utf-8')
    print(f'{word} decode from UTF-8')