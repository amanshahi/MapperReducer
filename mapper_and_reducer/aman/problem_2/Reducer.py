import sys
old, temp = None,0
country, ma = -1, -1
for var in sys.stdin:
	word = var.strip()
	if old and old != word:
		if ma < temp:
			country = old
			ma = temp
		temp = 0
	temp+=1
	old = word
if old != None and ma < temp:
	ma = temp
	country = old
print country, ma