import numpy as np
import func as obj

def decrypt(m, k, NR=12):
    m = list(bytearray.fromhex(m))
    k = list(bytearray.fromhex(k))

    # spliting message in blocks 
    m = np.array([m[i*4:(i+1)*4] for i in range(4)])
    k = np.array([k[i*4:(i+1)*4] for i in range(4)])

    cpt = obj.InvMysterion128(m, k, NR)

    h_cpt = ""
    for i in cpt:
        h_cpt += ''.join('{:02x}'.format(x) for x in i)
    
    return h_cpt

if __name__ == "__main__":
    ct = input("Ciphertext (32 Hex digits) : ")
    key = input("Key (32 Hex digits) : ")

    cpt = decrypt(ct, key)

    print("Encryption\n\n")
    print("Ciphertext : " + ct)
    print("Computed plaintext : " + cpt)