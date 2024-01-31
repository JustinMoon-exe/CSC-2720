from json.tool import main

#  recursion stuff


def fibonacci(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def stairclimb(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return (stairclimb(n - 1) + stairclimb(n - 2))
    
def __main__():
    print("________________")

    print(fibonacci(4))
    print(stairclimb(3))

    print("________________")


__main__()