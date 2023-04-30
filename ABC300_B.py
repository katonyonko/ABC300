import io
import sys

_INPUT = """\
6
4 3
..#
...
.#.
...
#..
...
.#.
...
3 2
##
##
#.
..
#.
#.
4 5
#####
.#...
.##..
..##.
...##
#...#
#####
...#.
10 30
..........##########..........
..........####....###.....##..
.....##....##......##...#####.
....####...##..#####...##...##
...##..##..##......##..##....#
#.##....##....##...##..##.....
..##....##.##..#####...##...##
..###..###..............##.##.
.#..####..#..............###..
#..........##.................
................#..........##.
######....................####
....###.....##............####
.....##...#####......##....##.
.#####...##...##....####...##.
.....##..##....#...##..##..##.
##...##..##.....#.##....##....
.#####...##...##..##....##.##.
..........##.##...###..###....
...........###...#..####..#...
"""

def solve(test):
  H,W=map(int,input().split())
  A=[input() for _ in range(H)]
  B=[input() for _ in range(H)]
  A=[[1 if A[i][j]=="#" else 0 for j in range(W)] for i in range(H)]
  B=[[1 if B[i][j]=="#" else 0 for j in range(W)] for i in range(H)]
  def trans(s,t,A):
    return [[A[(i+s)%H][(j+t)%W] for j in range(W)] for i in range(H)]
  ans='No'
  for i in range(H):
    for j in range(W):
      # if i==2 and j==1: print(A,B)
      if trans(i,j,A)==B: ans='Yes'
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