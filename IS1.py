#Assignment 1:
#program to store string "helloworld" and performs logical operations
#like AND,OR XOR 
#between each character of string and 127.

str1="Helloworld"
for ch in str1:
    s1=(ord(ch)&127)
    s2=(ord(ch)|127)
    s3=(ord(ch)^127)
    
    print(ch+" & 127 :"+chr(s1)+'\t'+
          ch+" | 127 :"+chr(s2)+'\t'+
          ch+" ^ 127 :"+chr(s3)+'\t')


-------------------------------------------------------------------------
# Output:

# H & 127 :H	H | 127 :	H ^ 127 :7	
# e & 127 :e	e | 127 :	e ^ 127 :	
# l & 127 :l	l | 127 :	l ^ 127 :	
# l & 127 :l	l | 127 :	l ^ 127 :	
# o & 127 :o	o | 127 :	o ^ 127 :	
# w & 127 :w	w | 127 :	w ^ 127 	
# o & 127 :o	o | 127 :	o ^ 127 :	
# 	 & 127 :r	r | 127 :	r ^ 127 :
# l & 127 :l	l | 127 :	l ^ 127 :	
# d & 127 :d	d | 127 :	d ^ 127 :
