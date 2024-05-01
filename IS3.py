from Crypto.Cipher import DES
def pad(text):
 n = len(text) % 8
 print(b"text to encrypt:"+text + (b' ' * n))
 return text + (b' ' * n)
key = b'hello123'
text1 = b'Python is the Best Language!'
des = DES.new(key, DES.MODE_ECB)
padded_text = pad(text1)
encrypted_text = des.encrypt(padded_text)
print(encrypted_text)
print(des.decrypt(encrypted_text))

# ----------------------------------------------------------------------------------------------------

# Output:

# b'text to encrypt:Python is the Best Language!    '
# b'{\x01^\xfe\xd5\xd1\x8fM\x1a\xcc\xd5\xbc\x04\x1c\x0em$,\xc1\xc7w-H1\xe6>\x08%!\xab\xd0X'
# b'Python is the Best Language!    '
