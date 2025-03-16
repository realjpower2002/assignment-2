# Padding scheme was PKCS7
# Mode was ECB

k10 = "E8BE80DD7C6215F67567BC5CAFBF2B3A"
k11 = "D64F00A4AA2D1552DF4AA90E70F58234"

ciphertext = ""

with open("ciphertext") as file:
    ciphertext = file.read()

if(ciphertext == ""):
    print("Read Failed!")

print("CIPHERTEXT : ",ciphertext)
print("Key 10 : ",k10)
print("Key 11 : ",k11)

# Let's see if we can find key 10 from key 11 ...

# We need to define key scheduling ...
# Split k10 into four words, w0 w1 w2 w3
# 
# For AES-128, we can split the 128 bit key into four
# 32-bit (8 byte) words



print("Experimenting with manipulating bytes ...")

# We can convert a hex string to bytes simply like this
k10_bytes = bytes.fromhex(k10)
print(k10_bytes)
print(hex(k10_bytes[0]))


# Now let's define xor on these byte objects

apple_bytes = b'apple'
pears_bytes = b'pears'

def xor_bytes(bytes_1,bytes_2):
    if(len(bytes_1) != len(bytes_2)):
        raise "Bytes 1 is a different length to Bytes 2"

    xor_bytes = b''

    for a,b in zip(bytes_1,bytes_2):
        xor_bytes += (a ^ b).to_bytes(1,"little")

    return xor_bytes

print(apple_bytes)
print(pears_bytes)
print(xor_bytes(apple_bytes,pears_bytes))



# Now let's try and actually do the AES math

import AES

# Rotates a 4 byte bytes object word left by one
def rot_word(word):
    return word[1:2]+word[2:3]+word[3:4]+word[0:1]

# Send all bytes of 
def sub_word(word):
    sub_word = AES.sbox[word[0]].to_bytes(1,"little") 
    sub_word += AES.sbox[word[1]].to_bytes(1,"little") 
    sub_word += AES.sbox[word[2]].to_bytes(1,"little") 
    sub_word += AES.sbox[word[3]].to_bytes(1,"little")

    return sub_word

def rcon_word(round):
    return AES.rcon[round].to_bytes(1,"little")+b'\x00'+b'\x00'+b'\x00'

def get_next_key(current_key, round):
    w0 = current_key[0:4]
    w1 = current_key[4:8]
    w2 = current_key[8:12]
    w3 = current_key[12:16]

    # Send w3 through rot, sub, and rcon
    w3_mod = rot_word(w3)
    w3_mod = sub_word(w3_mod)
    w3_mod = xor_bytes(w3_mod, rcon_word(round))

    # Then produce the rest of the xor
    # bytes
    w4 = xor_bytes(w3_mod,w0)
    w5 = xor_bytes(w4,w1)
    w6 = xor_bytes(w5,w2)
    w7 = xor_bytes(w6,w3)

    return w4+w5+w6+w7

next_key = get_next_key(k10_bytes,10)

print("This should equal k11 : ",next_key)
print("K11 : ",bytes.fromhex(k11))

def get_prev_key(current_key, round):
    w4 = current_key[0:4]
    w5 = current_key[4:8]
    w6 = current_key[8:12]
    w7 = current_key[12:16]

    # Get w3, w2, and w1 from their parameters
    # by undoing the xor operations
    w3 = xor_bytes(w7,w6)
    w2 = xor_bytes(w6,w5)
    w1 = xor_bytes(w5,w4)

    # Send w3 through rot, sub, and rcon to get
    # the arguments to w4
    w3_mod = rot_word(w3)
    w3_mod = sub_word(w3_mod)
    w3_mod = xor_bytes(w3_mod, rcon_word(round))

    # w0 can be produced from its arguments w4 and
    # w3_mod
    w0 = xor_bytes(w4,w3_mod)

    return w0+w1+w2+w3

k11_bytes = bytes.fromhex(k11)

print("This should equal k10 : ",get_prev_key(k11_bytes,10))
print("K10 : ",k10_bytes)