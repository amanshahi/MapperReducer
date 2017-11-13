import sys
old, temp = None,0
for var in sys.stdin:
	word = var.strip()
	if old and old != word:
		print old,temp
		temp = 0
	temp+=1
	old = word
if old != None:
	print old, temp
