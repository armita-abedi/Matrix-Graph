'''
Write a function to return if two words are exactly "one edit" away, where an edit is:
	Inserting one character anywhere in the word (including at the beginning and end)
	Removing one character
	Replacing exactly one character
'''

def checkOneEdit(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	
	if len1 == len2:
		return editByReplace(str1,str2)
		
	elif len1 - len2 == 1:
		return editByInsert(str1, str2)
		
	elif len2 - len1 == 1:
		return editByInsert(str2, str1)
		
	else:
		return False
		
		
def editByReplace(str1, str2):
	counter = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			counter += 1
			
	if counter == 1:
		return True
	else:
		return False
		
		
def editByInsert(str1, str2):
	index1, index2 = 0, 0
	shift = False
	
	while index1 < len(str1) and index2 < len(str2):
		if str1[index1] != str2[index2]:
			if shift == True:
				return False
			shift = True
			index1 += 1
		else:
			index1 += 1
			index2 += 1
		
	
	return True
		
		
print(checkOneEdit('acer','aker'))
print(checkOneEdit('kcer','acer'))
print(checkOneEdit('acer','ace'))
print(checkOneEdit('acer','cer'))
print(checkOneEdit('acer','aer'))
print(checkOneEdit('acer','axcer'))
print(checkOneEdit('acer','acerk'))
print(checkOneEdit('ab','ba'))
print(checkOneEdit('ab','abcd'))
print(checkOneEdit('ab','cdf'))
print(checkOneEdit('a',''))
print(checkOneEdit('a','b'))









