class HashTable(object):

  def __init__(self):
    self.size = 10
    self.keys = [None] * self.size
    self.values = [None] * self.size


  def hashFunction(self, key):
    sum = 0
    for pos in range(len(key)): # проходимся по всему key
      sum += ord(key[pos]) # переводим char в число

    return sum % self.size # мэпим в наш array




