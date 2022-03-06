from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="085"
#問題
problem="c"

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
  N,Y=map(int,input().split())
  ans=0
  for i in range(N+1):
    for j in range(N+1-i):
      if 10000*i+5000*j+1000*(N-i-j)==Y and ans==0:
        print(i,j,N-i-j)
        ans=1
  if ans==0: print(-1,-1,-1)
  """ここから上にコードを記述"""

  print(test_case[__+1])