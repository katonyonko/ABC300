import io
import sys

_INPUT = """\
6
10 1 2
ooxxooooox
5 3 4
oxxox
30 1000000000 9982443530
oxoxooxoxoxooxoxooxxxoxxxooxox
"""

def solve(test):
  N,M,K=map(int,input().split())
  S=input()
  c=S.count('x')
  loop=K//c
  remain=K%c
  def cnt(s,k):
    tmp=[0]
    now=0
    for i in range(len(s)):
      if s[i]=='x':
        now+=1
      tmp.append(now)
    l,r=0,len(s)+1
    while r-l>1:
      mid=(l+r)//2
      if min([tmp[i+mid]-tmp[i] for i in range(len(tmp)-mid)])<=k:l=mid
      else: r=mid
    return l
  if loop==M: ans=N*M
  elif loop==M-1:
    ans=cnt(S,remain)+loop*N
  else:
    ans=cnt(S*2,remain)+loop*N
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