import io
import sys

_INPUT = """\
6
5 9
#.#.#...#
.#...#.#.
#.#...#..
.....#.#.
....#...#
3 3
...
...
...
3 16
#.#.....#.#..#.#
.#.......#....#.
#.#.....#.#..#.#
15 20
#.#..#.............#
.#....#....#.#....#.
#.#....#....#....#..
........#..#.#..#...
#.....#..#.....#....
.#...#....#...#..#.#
..#.#......#.#....#.
...#........#....#.#
..#.#......#.#......
.#...#....#...#.....
#.....#..#.....#....
........#.......#...
#.#....#....#.#..#..
.#....#......#....#.
#.#..#......#.#....#
"""

def solve(test):
  H,W=map(int,input().split())
  C=[input() for _ in range(H)]
  C=[[1 if C[i][j]=="#" else 0 for j in range(W)] for i in range(H)]
  ans=[0]*min(H,W)
  for i in range(H):
    for j in range(W):
      if C[i][j]==1:
        r,c=i,j
        s=0
        while r<H and c<W and C[r][c]==1:
          C[r][c]=0
          r+=1
          c+=1
          s+=1
        for k in range(s):
          C[i+s-1-k][j+k]=0
        ans[s//2-1]+=1
  if test==0:
    print(*ans)
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