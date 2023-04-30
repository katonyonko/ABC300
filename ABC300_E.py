import io
import sys

_INPUT = """\
6
6
7
300
979552051200000000
"""

def solve(test):
  from heapq import heappop,heappush
  from collections import defaultdict
  N=int(input())
  mod=998244353
  den=pow(5,mod-2,mod)
  d=defaultdict(int)
  d[-N]=1
  h=[]
  heappush(h,-N)
  s=set([-N])
  while h:
    x=heappop(h)
    # if N==6: print(x,d)
    for nxt in range(2,7):
      if (-x)%nxt==0:
        d[x//nxt]+=d[x]*den
        d[x//nxt]%=mod
        if x//nxt not in s:
          s.add(x//nxt)
          heappush(h,x//nxt)
  if test==0:
    print(d[-1])
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