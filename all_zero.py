from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint


iv = b"\x00" * 16

n = 10000
cnt = 0

for i in range(n):
    key = get_random_bytes(32)
    plaintext = "a" * 32

    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8)
    e = cipher.encrypt(plaintext.encode())

    if e == b"\x00" * len(plaintext):
        cnt += 1

print("score: ", cnt)
print("probability: ", cnt/n)
print("1/256: ", 1/256)
