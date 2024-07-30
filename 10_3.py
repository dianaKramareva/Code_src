q=set(range(1,97))
res1=98
res2=res1+36
w=set(range(res1,res2))
unite=(q|w)
next_num=set(range(1,23))
d=unite-next_num
print(len(d))