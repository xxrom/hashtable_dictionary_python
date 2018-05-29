class HashTable(object):

  def __init__(self):
    self.size = 10
    self.keys = [None] * self.size
    self.values = [None] * self.size

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




