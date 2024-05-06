str_ = "строка с цифрой 1"

is_substr = "строка" in str_ # True
print("в строке есть слово Строка?", is_substr)

number = 12

condition_1 = mnumber % 2 == 0 # число кратно 2
condition_2 = mnumber % 3 == 0 # число кратно 3

if condition_1 and condition_2:
    print('число кратно 2 и 3')
else:
    print('число не (кратно 2 и 3)')

mounth = 12

# символ \ позволяет визуально разбить команду, для интерпритатора это одна строка
bad_condition = \
    mounth == 12 or \
    mounth == 1 or \
    mounth == 2 # очень плохая запись условия

good_condition = mounth in [12, 1 , 2] # при множественном сравнении лучше использовать in

if good_condition:
    print("зима!!!")

hour = 7

bad_condition = (6 <= hour)
good_condition = 6 <= hour < 12

if good_condition:
    print("утро!!!")

list_ = [5, 6, 7, 8, 9]

result = (4 in list_) and (8 in list)
print(result)

