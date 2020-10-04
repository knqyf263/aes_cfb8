from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint


iv = b"\x00" * 16

for i in range(10):
    key = get_random_bytes(32)
    plaintext = "a" * 32

    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8)
    e = cipher.encrypt(plaintext.encode())
    
    # lose a single byte
    index = randint(0, len(plaintext)-1)
    e = e[:index] + e[index+1:]

    print(f"=== lost {index}-th byte ===")

    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8)
    d = cipher.decrypt(e)

    # lose only some part of the original message (garbled content), and should be able to continue to 
    # correctly decrypt the rest of the blocks after processing some amount of input data.
    print(f"{len(d[:index])} bytes decrypted correctly: {d[:index].decode()}")
    print(f"{len(d[index:index+len(iv)])} bytes decrypted incorrectly: {d[index:index+len(iv)]}")
    print(f"{len(d[index+len(iv):])} bytes decrypted correctly: {d[index+len(iv):].decode()}\n")

