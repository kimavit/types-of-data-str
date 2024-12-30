Practiced string data type.
---------------------------
````Python
a = len(str(input()))
b = len(str(input()))
c = len(str(input()))

if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print("YES")
else:
    print("NO")
````
