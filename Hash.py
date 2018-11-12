class HashTableNode:
	def __init__(self, word ,vector, next):
		self.word = word
		self.vector = vector
		self.next = next

class HashTable:
	def __init__(self, table_size, alpha_value):
		self.table = [None] * table_size
		self.alpha_value = alpha_value
	
	def insert(self,k,vector, funcselect):
		loc = self.hash_function_switcher( funcselect,k)
		self.table[loc] = HashTableNode(k, vector, self.table[loc])

	def search(self, k, funcselect):
		loc = self.hash_function_switcher( funcselect,k)
		temp = self.table[loc]
		count = 0
		while temp is not None:
			count+=1
			if temp.word == k:
				return temp,count
			temp=temp.next

	def hash_function1(self, k):
		"""the hash function uses only the value
		of the first a-z, 1-26 respectivly making 26 buckets"""
		return self.alpha_value[k[0]] % len(self.table)

	def hash_function2(self, k):
		"""Sums the value of each letter represented 
		alphabetically as 1-26 respectivly, Symbols
		 have a value of 0"""
		b25word = 0
		for i in range(len(k)-1,0,-1):
			if k[i] not in self.alpha_value:
				b25word +=0
			else:
				b25word += self.alpha_value[k[i]]
		return (b25word*len(k)) % len(self.table)

	def hash_function3(self, k):
		"""converts word to numbers by summing the vales of
		each letter as if it was part a of a base 25 number
		then multiplying by the length of the word, values
		of symbols count as 0"""
		b25word = 0
		for i in range(len(k)-1,0,-1):
			if k[i] not in self.alpha_value:
				b25word +=0
			else:
				b25word += self.alpha_value[k[i]]*(i**25)
		return (b25word*len(k)) % len(self.table)
	
	def hash_function_switcher(self,selection, k):
		"""Using a dictionary to switch functions for hashing"""
		switcher = {
			1:self.hash_function1,
			2:self.hash_function2,
			3:self.hash_function3
		}
		func = switcher.get(int(selection) )
		return func(k)
