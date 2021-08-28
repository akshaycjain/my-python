s=input()
ns=s.split(' ')
s1=ns[0:3]
ns[0]=0
ns[4]=0
print("sliced list = ",s1)
s1.reverse()
print("reversed sliced list = ",s1)
s1[0]=0
s1[2]=0
print("replaced list-1 = ",ns)
ns.reverse()
print("reversed list-1 = ",ns)
print("replaced list-1 = ",s1)
