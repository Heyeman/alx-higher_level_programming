
def uppercase(str):
	str1 = list(str)
	for i in range(len(str1)):
		if ord(str[i]) >= 97 and ord(str[i]) <= 122:
			str1[i] = chr(ord(str[i]) - 32)
	str1 = ''.join(str1)
	print(str1)
