a = [10, 15, 3, 7]
k = 14


def check(a,k):
    for i in range(len(a)):
        if (k - a[i]) in a:
            return True
        else:
            return False


if check(a,k) == True:
    print("true")
else:
    print("false")