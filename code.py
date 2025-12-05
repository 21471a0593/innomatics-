1. my_string = "Hello, World!"
print(my_string)
output: Hello, World!

2. n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
  output: 7 
          Weird

3.a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
output:  3
 5
8
-2
15

4.a=int(input())
b=int(input())
print(a//b)
print(a/b)
output: 3
 5
0
0.6 

5.def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
year = int(input())
print(is_leap(year))
output: 1990
False

6.n = int(input())
for i in range(1, n + 1):
    print(i, end="")
  output: 3
123

7.n = int(input())
for i in range(n):
    print(i*i)
  output: 5
0
1
4
9
16
