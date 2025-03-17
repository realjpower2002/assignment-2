cipher = "8CD414B9AE99B51B61E9BF886E8953B42DF7E59D3AD2B5EC56968038E30B8F6A2B7FE0BF58E584C6777181FCB296AD45238844E6D8896FF5CA50825F96045BFBA90C40749D3D0E1838F4F1F9F32340FC77447DD13989C33FDF3C5F8875C7CB56FDBC2DBCA14C425FE2AA477FE4DE73B2"

print(len(cipher)/2)

"""
Message 2, 7, and 10 are stream ciphers for message 1 (length 14)

Message 1 and 8 are block ciphers for message 1 (padded to block size of 16)

Message 3, 5, and 9 are stream ciphers for message 2 (length 112)

Message 4 and 6 are block ciphers for message 2 (padded to block size of 16)


Stream Ciphers ? :

2 and 7 start with the same characters (8BDE etc, suggesting that they both
start from the same IV). 10 is a different stream cipher. This implies that
2 and 7 are CFB and OFB, and 10 is CTR

5 and 9 are similar for message 2. 3 is a different stream cipher. This implies
that 5 and 9 are CFB and OFB, and 3 is CTR.



Block Ciphers ? :

1 and 8 - it's a 50/50 shot. not bad odds.

4 and 6

"""

def xor_bytes(bytes_1,bytes_2):
    if(len(bytes_1) != len(bytes_2)):
        raise "Bytes 1 is a different length to Bytes 2"

    xor_bytes = b''

    for a,b in zip(bytes_1,bytes_2):
        xor_bytes += (a ^ b).to_bytes(1,"little")

    return xor_bytes



print("New bytes (Short message) : ",xor_bytes(bytes.fromhex("8BDE08A6E0998853"),b"Hello th"))

print("New bytes (Long  message) : ",xor_bytes(bytes.fromhex("8CD414B9AE99B51B"),b"Oops! I "))


# We can try to produce the next block of ciphertext and see what we get.
#
# Let's see if we can get the value of the encrypted si-1 (the double encrypted
# Initialization Vector)
print("New bytes (Short message, 2) : ",xor_bytes(bytes.fromhex("59EAB40E7B99"),b"ere!!!"))

print("New bytes (Short message, 7) : ",xor_bytes(bytes.fromhex("6EEEA9DD6FDA"),b"ere!!!"))

print("New bytes (Long message,  5) : ",xor_bytes(bytes.fromhex("61E9BF886E8953B4"),b"just rea"))

print("New bytes (Long message,  9) : ",xor_bytes(bytes.fromhex("96255A8DF39C4095"),b"just rea"))








