import sys
flag = 0
c=0
for var in sys.stdin:
    if flag == 0:
        flag = 1
    else :
        word = var.split(',')	
	if (len(word) == 7): print word[6],
	elif len(word) > 7: print word[7],
