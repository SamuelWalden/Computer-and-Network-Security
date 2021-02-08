import string
from sys import stdin

english = [.08167, .01492, .02782, .04253, .12702, .02228, .02015, .06094, .06996, .00153, .00772, .04025, .02406, .06749, .07507, .01929, .00095, .05987, .06327, .09056, .02758, .00978, .02360, .00150, .01974, .00074]


# mean of english
meanOfEnglish = 0;
for i in range (0, 26):
	meanOfEnglish = meanOfEnglish + english[i]
meanOfEnglish = meanOfEnglish / 26
populationSize = 26
#calculate population variance
populationVariance = 0
for k in range(0, 26):
	populationVariance = populationVariance + ((english[k] - meanOfEnglish)**2)
populationSize = 26
populationVariance = populationVariance / populationSize

#Find frequency of input


# variance method
def variance(plaintext):
	count = 0
	lst = [0] * 26
	for  j in range(0, len(plaintext)):
		if (plaintext[count] == 'a'):
			lst[0] = lst[0] + 1
		if (plaintext[count] == 'b'):
			lst[1] = lst[1] + 1
		if (plaintext[count] == 'c'):
			lst[2] = lst[2] + 1
		if (plaintext[count] == 'd'):
			lst[3] = lst[3] + 1
		if (plaintext[count] == 'e'):
			lst[4] = lst[4] + 1
		if (plaintext[count] == 'f'):
			lst[5] = lst[5] + 1
		if (plaintext[count] == 'g'):
			lst[6] = lst[6] + 1
		if (plaintext[count] == 'h'):
			lst[7] = lst[7] + 1
		if (plaintext[count] == 'i'):
			lst[8] = lst[8] + 1
		if (plaintext[count] == 'j'):
			lst[9] = lst[9] + 1
		if (plaintext[count] == 'k'):
			lst[10] = lst[10] + 1
		if (plaintext[count] == 'l'):
			lst[11] = lst[11] + 1
		if (plaintext[count] == 'm'):
			lst[12] = lst[12] + 1
		if (plaintext[count] == 'n'):
			lst[13] = lst[13] + 1
		if (plaintext[count] == 'o'):
			lst[14] = lst[14] + 1
		if (plaintext[count] == 'p'):
			lst[15] = lst[15] + 1
		if (plaintext[count] == 'q'):
			lst[16] = lst[16] + 1
		if (plaintext[count] == 'r'):
			lst[17] = lst[17] + 1
		if (plaintext[count] == 's'):
			lst[18] = lst[18] + 1
		if (plaintext[count] == 't'):
			lst[19] = lst[19] + 1
		if (plaintext[count] == 'u'):
			lst[20] = lst[20] + 1
		if (plaintext[count] == 'v'):
			lst[21] = lst[21] + 1
		if (plaintext[count] == 'w'):
			lst[22] = lst[22] + 1
		if (plaintext[count] == 'x'):
			lst[23] = lst[23] + 1
		if (plaintext[count] == 'y'):
			lst[24] = lst[24] + 1
		if (plaintext[count] == 'z'):
			lst[25] = lst[25] + 1
		count = count + 1
	
	varX = len(plaintext)

	# mean of plaintext
	#meanOfPlainText = 0;
	#for i in range (0, 26):
	#	meanOfPlainText = meanOfPlainText + lst[i]
	#meanOfPlainText = meanOfPlainText / 26
	#populationSize = 26

	#calculate population variance
	populationVariance = 0
	for k in range(0, 26):
		populationVariance = populationVariance + (((english[k]*lst[k]) - meanOfEnglish)**2)

	populationSize = 26
	populationVariance = populationVariance / populationSize
	return(populationVariance)

# method for generating key
def myKey(plaintext, key): 				# I derived lines 157 - 169 from 
	sepKey = list(key) 				# https://www.geeksforgeeks.org/vigenere-cipher/
	for i in range(len(plaintext) - len(key)): 	# to help generate our keys and ciphertext
            sepKey.append(key[i % len(key)]) 		#
	return("" . join(sepKey)) 			# I also referenced Introduction to Cryptography with
							# coding theory, by Wade Trappe and Lawrence C. 
# method for generating ciphertext			# Washington to rerefresh my knowledge of Vigenere
def myCipherText(plaintext, key): 			# ciphers (chapter 2.3 - The Vigenere Cipher)
	workingCipher = [] 				
	for i in range(len(plaintext)): 
		x = (ord(plaintext[i]) + ord(key[i])) % 26
		x += ord('A') 
		workingCipher.append(chr(x)) 
	return("" . join(workingCipher)) 

# mean of the frequency variances of the ciphertext
lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
lst7 = []
lst8 = []
lst9 = []
lst10 = []
lst11 = []
lst12 = []
lst13 = []
lst14 = []
lst15 = []
lst16 = []
lst17 = []
lst18 = []
lst19 = []
lst20 = []
def yzmeanFreq(ciphertext):	
	for j in range(0, len(ciphertext), 2):
		lst1.append(chr(j))
	for k in range(1, len(ciphertext), 2):
		lst2.append(chr(k))
	x = variance(lst1)
	y = variance(lst2)
	mean = (x + y) / 2
	return(mean)

def xyzmeanFreq(ciphertext):	
	for j in range(0, len(ciphertext), 3):
		lst3.append(chr(j))
	for k in range(1, len(ciphertext), 3):
		lst4.append(chr(k))
	for l in range(2, len(ciphertext), 3):
		lst5.append(chr(l))
	a = variance(lst3)
	b = variance(lst4)
	c = variance(lst5)
	mean = (a + b + c) / 3
	return(mean)

def wxyzmeanFreq(ciphertext):	
	for j in range(0, len(ciphertext), 4):
		lst6.append(chr(j))
	for k in range(1, len(ciphertext), 4):
		lst7.append(chr(k))
	for l in range(2, len(ciphertext), 4):
		lst8.append(chr(l))
	for m in range(3, len(ciphertext), 4):
		lst9.append(chr(m))
	a = variance(lst6)
	b = variance(lst7)
	c = variance(lst8)
	d = variance(lst9)
	mean = (a + b + c + d) / 4
	return(mean)

def vwxyzmeanFreq(ciphertext):	
	for j in range(0, len(ciphertext), 5):
		lst10.append(chr(j))
	for k in range(1, len(ciphertext), 5):
		lst11.append(chr(k))
	for l in range(2, len(ciphertext), 5):
		lst12.append(chr(l))
	for m in range(3, len(ciphertext), 5):
		lst13.append(chr(m))
	for n in range(4, len(ciphertext), 5):
		lst14.append(chr(n))
	a = variance(lst10)
	b = variance(lst11)
	c = variance(lst12)
	d = variance(lst13)
	e = variance(lst14)
	mean = (a + b + c + d + e) / 5
	return(mean)

def uvwxyzmeanFreq(ciphertext):	
	for j in range(0, len(ciphertext), 6):
		lst15.append(chr(j))
	for k in range(1, len(ciphertext), 6):
		lst16.append(chr(k))
	for l in range(2, len(ciphertext), 6):
		lst17.append(chr(l))
	for m in range(3, len(ciphertext), 6):
		lst18.append(chr(m))
	for n in range(4, len(ciphertext), 6):
		lst19.append(chr(n))
	for o in range(5, len(ciphertext), 6):
		lst19.append(chr(o))
	a = variance(lst15)
	b = variance(lst16)
	c = variance(lst17)
	d = variance(lst18)
	e = variance(lst19)
	f = variance(lst20)
	mean = (a + b + c + d + e + f) / 6
	return(mean)


if __name__ == "__main__": 
	print("Please provide plain text: ")
	plaintext = stdin.readline()
	var = variance(plaintext)
	print("1: " + str(var) + "\n")
	# key yz
	plaintext = plaintext.upper()
	key = myKey(plaintext, "YZ") 
	ciphertext = myCipherText(plaintext,key)
	lilCiphertext = ciphertext.lower()
	var = variance(lilCiphertext)
	yzCiphertext = lilCiphertext
	print("2_yz: " + str(var))
	# key xyz
	key = myKey(plaintext, "XYZ") 
	ciphertext = myCipherText(plaintext,key)
	var = variance(lilCiphertext)
	xyzCiphertext = lilCiphertext
	print("2_xyz: " + str(var))
	# key wxyz
	key = myKey(plaintext, "WXYZ") 
	ciphertext = myCipherText(plaintext,key)
	lilCiphertext = ciphertext.lower()
	var = variance(lilCiphertext)
	wxyzCiphertext = lilCiphertext
	print("2_wxyz: " + str(var))
	# key vwxyz
	key = myKey(plaintext, "VWXYZ") 
	ciphertext = myCipherText(plaintext,key)
	lilCiphertext = ciphertext.lower()
	var = variance(lilCiphertext)
	vwxyzCiphertext = lilCiphertext
	print("2_vwxyz: " + str(var))
	# Key uvwxyz
	key = myKey(plaintext, "UVWXYZ") 
	ciphertext = myCipherText(plaintext,key)
	lilCiphertext = ciphertext.lower()
	var = variance(lilCiphertext)
	uvwxyzCiphertext = lilCiphertext
	print("2_uvwxyz: " + str(var) + "\n")

	four1 = yzmeanFreq(yzCiphertext)
	print("3_yz: " + str(four1))
	four2 = xyzmeanFreq(xyzCiphertext)
	print("3_xyz: " + str(four2))
	four3 = wxyzmeanFreq(wxyzCiphertext)
	print("3_wxyz: " + str(four3))
	four4 = vwxyzmeanFreq(vwxyzCiphertext)
	print("3_vwxyz: " + str(four4))
	four5 = uvwxyzmeanFreq(uvwxyzCiphertext)
	print("3_uvwxyz: " + str(four5) + "\n")

	five1 = yzmeanFreq(uvwxyzCiphertext)
	print("4_len2: " + str(five1))
	five2 = xyzmeanFreq(uvwxyzCiphertext)
	print("4_len3: " + str(five2))
	five3 = wxyzmeanFreq(uvwxyzCiphertext)
	print("4_len4: " + str(five3))
	five4 = vwxyzmeanFreq(uvwxyzCiphertext)
	print("4_len5: " + str(five4))
	
	


      


	
	
	







