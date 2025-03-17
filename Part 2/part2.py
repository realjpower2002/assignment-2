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