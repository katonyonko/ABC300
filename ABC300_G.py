import io
import sys

_INPUT = """\
6
36 3
10000000000000000 97
"""

def solve(test):
  from bisect import bisect_right
  N,P=map(int,input().split())
  import math
  def Eratosthenes(n):
    prime=[]
    furui=list(range(2,n+1))
    while furui[0]<math.sqrt(n):
      prime.append(furui[0])
      furui=[i for i in furui if i%furui[0]!=0]
    return prime+furui
  prime=Eratosthenes(P)
  U,V=[1],[1]
  for p in prime:
    if len(U)<len(V): W=U
    else: W=V
    for i in range(len(W)):
      tmp=W[i]
      while tmp*p<=N:
        tmp*=p
        W.append(tmp)
  U.sort()
  V.sort()
  ans=0
  for i in range(len(U)):
    ans+=bisect_right(V,N//U[i])
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