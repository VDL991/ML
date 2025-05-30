x = 5
print(x, id(x))
y = x
print(y, id(y))
x = 'Geeks'
print(x,id(x))
y = 'computer'
print(y, id(y))
z = 10
print(z)
del z
#swapping two variables
a,b =5,10
a,b = b,a 
print(a,b)
# identical operators
c =10
d =20
e = c
print(a,id(c))
print(d,id(d))
print(e, id(e))
print(c is not d)
print(c is e)
print(oct(23)+oct(23))