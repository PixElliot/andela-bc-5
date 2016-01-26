def reverse(text):
	#Returns the reverse of a string using slicing
	return text[::-1]

def swap(list_, i, j):
	list_[i], list_[j] = list_[j], list_[i]

def reversex(text):
	text = list(text)
	for i in range(len(text)//2):
		swap(text, text[i], text[len(text)-(i+1)])
		
	return "".join(text)

#Examples
reverse("Pol")
reverse("Andela")