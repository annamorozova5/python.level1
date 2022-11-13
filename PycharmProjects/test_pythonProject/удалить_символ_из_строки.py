d = '9 10 159 2000 5698 45'

print(d.translate({ord(i): None for i in '159'})) #удалятся символы 1, 5, 9
