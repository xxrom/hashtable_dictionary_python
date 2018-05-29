# get/put выполняются за O(1), если переполнен массив, то
# O(N) будет худшим вариантом !

class HashTable(object):

  def __init__(self):
    self.size = 10
    self.keys = [None] * self.size
    self.values = [None] * self.size

  # O(1) to O(N) зависит от заполненности values n/m <= 0.66
  def get(self, key):
    index = self.hashFunction(key)

    while self.keys[index] is not None:
      # check if it is the same key
      if self.keys[index] == key:
        return self.values[index]

      # collision => try next index
      index = (index + 1) % self.size

    # this key did not have any value => return None
    return None

  # O(1) to O(N) зависит от заполненности values n/m <= 0.66
  def put(self, key, data):
    # open addressing => find next empty slot and put there
    index = self.hashFunction(key)

    while self.keys[index] is not None:
      if self.keys[index] == key:
        self.values[index] = data # updating data
        return

      # rehash, try to find another empty slot
      index = (index + 1) % self.size

    # insert data in empty slot
    self.keys[index] = key
    self.values[index] = data

  def hashFunction(self, key):
    sum = 0
    for pos in range(len(key)): # проходимся по всему key
      sum += ord(key[pos]) # переводим char в число

    return sum % self.size # мэпим в наш array/ переводим 22%10=2

if __name__ == '__main__':
  table = HashTable()

  table.put('apple', 10)
  table.put('orange', 20)
  table.put('car', 30)
  table.put('table', 40)
  table.put('table2', 40)
  table.put('table3', 40)
  table.put('table4', 40)
  table.put('table5', 40)
  table.put('table6', 460)
  # table.put('table7', 470) # вот тут сломается, так как размер
  # будет больше 10 и коллиция не найдет просто места

  print(table.get('car')) # 30
  print(table.get('cara')) # None
  print(table.get('table')) # 40
  # print(table.get('table7')) # 460 # вот тут сломается,нет места


