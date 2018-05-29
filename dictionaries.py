# главный недостаток словарей, они не поддерживают порядок
# порядок может быть другой и массив values будет разбросанный

dictionary = {
  'Joe': 14,
  'Adam': 26,
  'Emily': 56
}

print('%s ' % dictionary['Joe']) # O(1)

dictionary['Joe'] = 15

print(dictionary['Joe'])

# dictionary.clear() # remove all data inside

# del dictionary # delete whole item dictionary

print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())

