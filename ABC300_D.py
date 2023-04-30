import io
import sys

_INPUT = """\
6
1000
1000000000000
"""
import math
def Eratosthenes(n):
  prime=[]
  furui=list(range(2,n+1))
  while furui[0]<math.sqrt(n):
    prime.append(furui[0])
    furui=[i for i in furui if i%furui[0]!=0]
  return prime+furui

def solve(test):
  from bisect import bisect_right
  N=int(input())
  prime=Eratosthenes(10**6+1)
  ans=0
  for i in range(len(prime)):
    a=prime[i]
    for j in range(i+1,len(prime)):
      c=prime[j]
      if (a*c)**2>=N: break
      x=N//((a*c)**2)
      y=bisect_right(prime,x)
      if y>i: ans+=min(y-i-1,j-i-1)
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)