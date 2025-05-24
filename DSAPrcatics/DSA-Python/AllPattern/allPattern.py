# DSA-Practics
# Pattern 1
"""
*****
*****
*****
*****
"""
for i in range(4):
    for j in range(5):
        print('*',end=' ')
    print()
print("\n")

# Pattern 2
"""
* * * * *
* * * * 
* * * 
* *
*
"""

for i in range(5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
print("\n")

# Pattern 3
"""
*
* *
* * *
* * * *
* * * * * 
"""
for i in range(1, 6):
    for j in range(i):
        print('*',end=' ')
    print()
print("\n") 

# Pattern 4
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range (1, 6):
    for j in range(1, i+1):
        print(j,end=' ')
    print()
print("\n")

# Pattern 5
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
def pattern5(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i,end=' ')
        print()
pattern5(5)
print("\n")

# Pattern 6
'''
12345
1234
123
12
1
'''
def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j,end=' ')
        print()
pattern6(5)

# Pattern 7
'''
      *
     * *
    * * *
   * * * *
  * * * * *
'''
def pattern_space_star_space(n):
    for i in range(1, n + 1, 1):
        # 1. Leading spaces (for centering)
        print(' ' * (n - i), end='')

        # 2. Stars with space after each (i stars)
        for j in range(i):
            print('*', end=' ')

        # 3. Trailing spaces (optional - visual balance)
        print(' ' * (n - i))

pattern_space_star_space(5)
print("\n")