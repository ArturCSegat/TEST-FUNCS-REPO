arr1 = [46, 57 ,69 , 10 , 13, 76, 18, 180, 5, 75]


#this is iterative
def liniarSearch(arr, t): #normal linear search
    for i in arr:
        if i == t:
            return arr.index(i)


# print(liniarSearch(arr1, 10))

#this is iterative as well
def binarySearch_I(item_list,item): # onluy works in sorted lists add arr.sort() at the started for non srted lists
	#sets the first number of the list
	low = 0
	#sets the highst number on the arr
	high = len(item_list)-1
	while low<=high:
		mid = (low + high)//2 # gets the middle of the sorted array
		if item_list[mid] == item : # if the middle is the target
			return mid
		else:
			if item < item_list[mid]: # sets the higest point to the middle
				high = mid - 1
			else:
				low = mid + 1	#sets the loest point to the middle
	return 'Element not found'
	
# print(binarySearch_I([1,2,3,5,8], 5))

#this function is ment to ecnprit a passwd based on itself
def psswdEncription(psswd):
	#removes blank spaces
	psswd = psswd.replace(" ", "")
	#removes capital letters
	psswd= psswd.lower()
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	#empty list where the encripetd alhabeet will be stored
	enc_al = []

	for l in psswd:
		#this loop puts the psswd in enc_all
		if l not in enc_al:
			enc_al.append(l)
	for l in alphabet:
		#this one puts the rest of the alphabet in there
		if l not in enc_al:
			enc_al.append(l)
			
	for l in psswd:
		#this atualy encripts the psswd
		psswd = psswd.replace(l, enc_al[alphabet.index(l)])

	return psswd
			

p = psswdEncription("kfh oitenta e TRES")
def psswdDecription(psswd):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	enc_al = []
	for l in psswd:
		if l not in enc_al and l != " ":
			enc_al.append(l)
	for l in alphabet:
		if l not in enc_al:
			enc_al.append(l)

	for l in psswd:
		psswd = psswd.replace(l, alphabet[enc_al.index(l)])
	
	return psswd
#THIS FUNCTION WAS SIMPLY TO TEST IF psswEncprition CAN BE DECRIPTED BACK TO THE PASSWORD WHAT IT CANNOT
# print(psswdDecription(p))

#print(p)
