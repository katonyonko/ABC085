from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="085"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,H=map(int,input().split())
  s=[list(map(int,input().split())) for _ in range(N)]
  s.sort(reverse=True)
  t=[]
  a=s[0][0]
  for i in range(N):
    if s[i][1]>a:
      t.append(s[i][1])
  t.sort(reverse=True)
  x=0
  ans=0
  while H>0 and ans<len(t):
    H-=t[ans]
    ans+=1
  if H<=0:
    print(ans)
  else:
    print(ans+(H-1)//a+1)
  """ここから上にコードを記述"""

  print(test_case[__+1])