import numpy as np
import func as obj

# e.g.
# inpt = "01010000B2C3D4E5F60718293A4B5C6D"
# key = "0205060752F3E1F2132435465B6C7D88"

def encrypt(m, k, NR=12):
    m = list(bytearray.fromhex(m))
    k = list(bytearray.fromhex(k))

    # spliting message in blocks 
    m = np.array([m[i*4:(i+1)*4] for i in range(4)])
    k = np.array([k[i*4:(i+1)*4] for i in range(4)])

    ct = obj.Mysterion128(k, m, NR)
    
    h_ct = ""
    for i in ct:
        h_ct += ''.join('{:02x}'.format(x) for x in i)

    return h_ct

if __name__ == "__main__":
    pt = input("Plaintext (32 Hex digits) : ")
    key = input("Key (32 Hex digits) :")

    ct = encrypt(pt, key)

    print("Encryption\n\n")
    print("Plaintext : " + pt)
    print("Ciphertext : " + ct)