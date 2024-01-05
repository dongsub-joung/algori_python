import sys

input= sys.stdin.readline

dictionary= {}
answers= []

n,m =map(int, input().split())

for _ in n+1:
    site, pw= input().split(' ')
    dictionary[site]= pw
for _ in m+1:
    site= input()
    answers.append(dictionary.get(site))

for answer in answers:
    print(answer)