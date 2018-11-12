"""
@author Rocorral
ID: 80416750
Instructor: David Aguirre
TA: Saha, Manoj Pravakar
Assignment:Lab 4-A -Hash Table, word Embeddings
Last Modification: 11/11/2018
Program Purpose: The purpose of this program is to practice and note the
difference in computation times of insertion and retrieval froma  Hash Table,
we aree provided with a word embeding file and are required to insert each 
word and its embeding vector into a table. After the insertions we must 
retrieved words based on pairs read from another file and compute the similarity.
during the search operation we will compute average comparisons per search.
"""
from string import ascii_lowercase
import Hash
import math
import io


def read_f_into_Hash_table(file, h_func):
	insertions = 0
	words = Hash.HashTable((400000),alpha_value)
	forHash = io.open(file ,'r+', encoding = "UTF-8")
	for line in forHash:
		a = line.split()
		#Direguards "words" in file that do not begin witch characters from the alphabet
		if (a[0] >= 'A' and a[0] <= 'Z') or (a[0] >='a' and a[0] <= 'z'):
			insertions+=1
			words.insert(a[0] , a[1:len(a)] , h_func)
	print("load factor :",len(words.table)*.75)
	return words


def computeSimilarity(hash_table,file2,h_func):
	comparisons=0
	searches=0
	forComparison = io.open(file2, 'r+', encoding="UTF-8")
	for line in forComparison:
		dotProduct = 0
		denoma = 0
		denomb = 0
		b = line.split()
		w0,c1 = hash_table.search(b[0] ,h_func)#word 1 from pair
		w1,c2 = hash_table.search(b[1] ,h_func)#word 2
		comparisons+=(c1+c2)
		searches+=2
		for i in range(len(w0.vector)):
			dotProduct = dotProduct + (float(w0.vector[i])*float(w1.vector[i]))
			denoma = denoma + float(w0.vector[i])*float(w0.vector[i])
			denomb = denomb + float(w1.vector[i])*float(w1.vector[i])
		denom = math.sqrt(denoma)*math.sqrt(denomb)
		similarity = dotProduct/denom
		print (w0.word," ",w1.word, "    similarity: " , similarity )
		print(w0.word," and ", w1.word ,"take ",c1," and ", c2," comparisons to find respectivly")
	print("Average number of comparisons per search :",comparisons/searches)





#----------Main-----------

"""this folowing code is used to supply the
hash table with a refrence for letter values"""
alpha_value = {}
i = 0
for i in range(len(ascii_lowercase)):
	alpha_value[ascii_lowercase[i]] = i+1

for i in range(1,4):
	print("\n","Using hash function #:",i)
	words =read_f_into_Hash_table("glove.6B.50d.txt",i)
	computeSimilarity(words,"Apendix-word-List.txt",i)

