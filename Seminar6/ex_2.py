# Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]


list_in = [12,'sadf',5643] 

list_num = list(filter(lambda el: type(el) == int, list_in))
list_str = list(filter(lambda el: type(el) == str, list_in))

print(list_str, list_num, sep=', ')