# Напишите программу, удаляющую из текста все слова, содержащие 'абв'
str = 'Напишите програабвмму, удаляющую иабвз абвтекста всеабв слова, содержащие "абв"'
str = list(filter(lambda x: 'абв' not in x, str.split()))
str = " ".join(str)
print(str)

# print(*filter(lambda x: "абв" not in x, text))