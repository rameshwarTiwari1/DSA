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
        print('*',end='')
    print()

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