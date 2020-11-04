import numpy as np 

def sbox(u):
  A= u & 0x0001
  B = u>>1 & 0x0001
  C= u >>2& 0x0001
  D = u>>3 & 0x0001
  a = A & B
  a=a^C
  c = B | C
  c=c^D
  d = a&D
  d=d^A
  b = c&A
  b=b^B
  List = [a,b,c,d]
  result = int("".join(str(i) for i in List),2)
  return result
  
def ddt():
  ddtArr = np.zeros((16,16)) 
  max =0
  for u in range(16):
    for v in range(16):
      i = u^v
      o = sbox(u)^sbox(v)
      ddtArr[i][o] = ddtArr[i][o] +1
  print(ddtArr)

if __name__ == "__main__":
  ddt()
