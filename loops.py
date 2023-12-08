''''
for element in range(1,24):
  print(element)
'''


'''
my_dict = {
  'user': 'd1eshi',
  'age': 20,
  'city': 'junin'
}

for key, value in my_dict.items():
  print(f'{key}, {value}')

'''
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
for number in my_list:
  number > 0  and new_list.append(number)

print(new_list)