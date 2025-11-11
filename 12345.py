#Given an integer n, print all numbers from 1 to n consecutively on one line without spaces.
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n +1):
        print (i, end = '')