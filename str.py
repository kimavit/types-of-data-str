a = str(input())
b = str(input())
c = str(input())

if len(a) < len(b):
    b, a = a, b
if len(b) < len(c):
    c, b = b, c
if len(a) < len(b):
    b, a = a, b
print(c, a, sep='\n')
