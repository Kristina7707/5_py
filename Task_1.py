# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел:\n")
s = txt.split()
print(s)
result = filter(lambda x: 'а' not in x or 'б' not in x or 'в' not in x, s)
print(*result)

