# Пользователь вводит строку. Необходимо написать программу, которая
# определяет, существует ли у этой строки перестановка, при которой она станет
# палиндромом. Затем она должна выводить соответствующее сообщение.

text = input('Введите текст: ')
char_dict = dict()
count = 0

for i in text:
    char_dict[i] = char_dict.get(i,0) + 1

for j in char_dict.values():
    if j % 2 != 0:
        count += 1







# # Позиционное форматирование
# name = 'Семен'
# mid_name = 'Cеменович'
# balance = 32.56
# text = """Дорогой {0} {1}, баланс вашего лицевого счета составляет {2} руб.""".format(name,mid_name,balance)
# print(text)
# Возможно также именованное форматирование, в таком случае после .format идет присваивание
# шаблонам: .format(n = name, m=mid_name,b=balance)
# text = """Дорогой {n} {m},баланс вашего лицевого счета составляет {b}"""
# название и размер шаблонов можно задавать прроизвольно, главное-задать присваивание
# переменным


