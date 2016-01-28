def reverse(text):
    text = str(text)
    rvc = ""
    for i in range(0,len(text)):
        rvc += text[(len(text)-(i+1))]
    return rvc

def easyw(text):
	rvc = ""
	i = len(text) - 1
	while i >= 0:
		rvc += text[i]
	return rvc

def easyr(text):
	return text[::-1]