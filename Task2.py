# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность (сдвиг-циклический) на K элементов вправо, K- положительное
# число.

list1=[5, 4, 6, 7, -10]
k = int(input('Введите число: '))
k = k % len(list1)

list_res = []

for i in range(k):
    # функция .append добавляет новое значение, в данном случае которое сдвинулось влево
    list_res.append(list1[len(list1) - 1 -i])
print(list_res)

for j in range(len(list1) - k):
    list_res.append(list1[j])
print(list_res)
