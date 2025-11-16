#Read an integer n, then read n integers separated by spaces.
#Print the second largest number in the list.
if __name__ == '__main__':
    n =int(input())
    list = list(map(int, input().split()))
    list.sort()
    print(list[-2])
    #test