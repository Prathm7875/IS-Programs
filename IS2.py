import math
plaintext="transposition technique using python"
key=8
ciphertext=['']*key
for colum in range(key):
    pointer=colum
    while pointer<len(plaintext):
     ciphertext[colum]+=plaintext[pointer]
     print(ciphertext)
     pointer+=key

cipher=''.join(ciphertext)
print(cipher)
 

numOfColumns = math.ceil(len(cipher) / key)
print(numOfColumns )
numOfRows = key
numOfShadedBoxes = (numOfColumns * numOfRows) - len(cipher)

pt = [''] * numOfColumns
col=0
row=0
for sym in cipher:
   pt[col]+=sym
   col+=1
   if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
       col=0
       row=row+1
       print(pt)

print(''.join(pt))      

#-----------------------------------------------------------------------------------------------------------------------------------

# Output:

# >>> %Run Assignment2_SourceFile.py
# ['t', '', '', '', '', '', '', '']
# ['ti', '', '', '', '', '', '', '']
# ['tic', '', '', '', '', '', '', '']
# ['ticu', '', '', '', '', '', '', '']
# ['ticut', '', '', '', '', '', '', '']
# ['ticut', 'r', '', '', '', '', '', '']
# ['ticut', 'rt', '', '', '', '', '', '']
# ['ticut', 'rth', '', '', '', '', '', '']
# ['ticut', 'rths', '', '', '', '', '', '']
# ['ticut', 'rthsh', '', '', '', '', '', '']
# ['ticut', 'rthsh', 'a', '', '', '', '', '']
# ['ticut', 'rthsh', 'ai', '', '', '', '', '']
# ['ticut', 'rthsh', 'ain', '', '', '', '', '']
# ['ticut', 'rthsh', 'aini', '', '', '', '', '']
# ['ticut', 'rthsh', 'ainio', '', '', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'n', '', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'no', '', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noi', '', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noin', '', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', '', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 's', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'sn', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snq', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', '', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p ', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', '', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'o', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'ot', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'ote', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'otep', '']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'otep', 's']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'otep', 'se']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'otep', 'se ']
# ['ticut', 'rthsh', 'ainio', 'noinn', 'snqg', 'p u ', 'otep', 'se y']
# ticutrthshainionoinnsnqgp u otepse y
# 5
# ['t', 'i', 'c', 'u', 't']
# ['tr', 'it', 'ch', 'us', 'th']
# ['tra', 'iti', 'chn', 'usi', 'tho']
# ['tran', 'itio', 'chni', 'usin', 'thon']
# ['trans', 'ition', 'chniq', 'using', 'thon']
# ['transp', 'ition ', 'chniqu', 'using ', 'thon']
# ['transpo', 'ition t', 'chnique', 'using p', 'thon']
# ['transpos', 'ition te', 'chnique ', 'using py', 'thon']
# transposition technique using python

