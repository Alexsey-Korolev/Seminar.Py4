# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

from itertools import zip_longest

def delete_pow(string: str):
    string = string[:string.find('^')] + string[string.find('^')+2:]
    if '^' in string:
        return delete_pow(string)
    else:
        return string

def get_coefs_from_poly(string: str):
    string = string.replace('*x', '')
    string = string.replace(' ', '')
    return string.split('+')

with open('task5_1.txt', 'r') as f:
    poly1 = ''.join(f.readlines()).replace(' = 0', '')

with open('task5_2.txt', 'r') as f:
    poly2 = ''.join(f.readlines()).replace(' = 0', '')

k = len(poly1.split(' + ')) - 1

arr = [f'*x^{i} + ' for i in range(k, 1, -1)]
arr.append('*x + ')

coefs1 = list(map(int, get_coefs_from_poly(delete_pow(poly1))))
coefs2 = list(map(int, get_coefs_from_poly(delete_pow(poly2))))
coefs3 = list(map(str, list(map(lambda x, y: x + y, coefs1, coefs2))))
res_arr = [list(i) for i in list(zip_longest(coefs3, arr, fillvalue=''))]

result = ''
for i in res_arr:
    result += ''.join(i)

with open('task5_R.txt', 'w') as f:
    f.write(f'({poly1}) + ({poly2}) = {result}')
print(f'({poly1}) + ({poly2}) = {result}')