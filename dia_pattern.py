s=input()
l=len(s)
a=s[:l//2]
b=s[l//2+1:]
t=l
for i in range(len(a)):
    print((" "*i)+(a[i])+(" "*(t-2))+(b[-1*(i+1)])+(" "*i))
    t-=2
print((" "*len(a))+(s[l//2])+(" "*len(a)))
t=1
for i in range(len(b)):
    print((" "*(len(b)-i-1))+(a[-1*(i+1)])+(" "*t)+(b[i])+(" "*(len(b)-i-1)))
    t+=2

print("*&$"*10)

a=s[:l//2]
b=s[l//2+1:]
t=l
for i in range(len(a)):
    print((" "*i)+(a[i])+(" "*(t-2))+(a[i])+(" "*i))
    t-=2
print((" "*len(a))+(s[l//2])+(" "*len(a)))
t=1
for i in range(len(b)):
    print((" "*(len(b)-i-1))+(b[i])+(" "*t)+(b[i])+(" "*(len(b)-i-1)))
    t+=2

"""
programming
p         g
 r       n 
  o     i  
   g   m   
    r m    
     a     
    r m    
   g   m   
  o     i  
 r       n 
p         g
p         p
 r       r 
  o     o  
   g   g   
    r r    
     a     
    m m    
   m   m   
  i     i  
 n       n 
g         g
>>> """
