def sbox(block):
    a = (block[0] & block[1]) ^ block[2]
    c = (block[1] | block[2]) ^ block[3]
    d = (a & block[3]) ^ block[0]
    b = (c & block[0]) ^ block[1]
    return [a,b,c,d]
    
if __name__ == "__main__":
  block = input("Give us a block:")
  print(sbox(block))
