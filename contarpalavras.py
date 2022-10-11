#GUSTAVO SOARES
#RA 00231374
from collections import Counter

with open('song1.txt') as f:
    p_vezes = Counter(f.read().split())

with open('song2.txt') as f:
    s_vezes = Counter(f.read().split())

with open('song3.txt') as f:
    t_vezes = Counter(f.read().split())



#qual arquivo tem mais palavras?
print('song1 tem mais palavras'
    if sum(p_vezes.values()) > sum(s_vezes.values()) and sum(p_vezes.values()) > sum(t_vezes.values()) 
else 'song2 tem mais palavras'
    if sum(s_vezes.values()) > sum(p_vezes.values()) and sum(s_vezes.values()) > sum(t_vezes.values()) 
else 'song3 tem mais palavras')

#qual arquivo tem mais palavras diferentes?
print('song1 tem mais palavras diferentes'
    if len(p_vezes) > len(s_vezes) and len(p_vezes) > len(t_vezes) 
else 'song2 tem mais palavras diferentes'
    if len(s_vezes) > len(p_vezes) and len(s_vezes) > len(t_vezes) 
else 'song3 tem mais palavras diferentes')

#qual arquivo tem as maiores palavras?

print('song1 tem as maiores palavras'
    if max(p_vezes, key=len) > max(s_vezes, key=len) and max(p_vezes, key=len) > max(t_vezes, key=len) 
else 'song2 tem as maiores palavras'
    if max(s_vezes, key=len) > max(p_vezes, key=len) and max(s_vezes, key=len) > max(t_vezes, key=len) 
else 'song3 tem as maiores palavras')
   