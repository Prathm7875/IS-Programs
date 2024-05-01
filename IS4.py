from Crypto.Cipher import AES

key = b'6487264824evcnvk'
cipher = AES.new(key, AES.MODE_EAX)
data = "Hello welcome to P town".encode()


nonce = cipher.nonce

ciphertext = cipher.encrypt(data)

print("Plain text",data)
print("Cipher text: ",ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

plaintext = cipher.decrypt(ciphertext)
print("Plain text", plaintext)

# -----------------------------------------------------------------------------------------------------

# Output:


# >>> %Run AES7.py
# Plain text b'Hello welcome to P town'
# Cipher text:  b'\xc3\xcb1ms\xea\x15\x84\x12b\x8bc\x18\xd5\xfac\xb2\x14\xba\x9a\xbb\xe2\xef'
# Plain text b'Hello welcome to P town'
