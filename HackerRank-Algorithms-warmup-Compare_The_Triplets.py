def compareTriplets(a, b):
    Alice = 0
    Bob = 0
    if len(a) == len(b):
        for i in range(0, len(a)):
            if a[i] <= 100 and a[i] >= 1 and b[i] <= 100 and b[i] >= 1: 
                if a[i] > b[i]:
                    Alice += 1
                elif a[i] == b[i]:
                    continue
                elif a[i] < b[i]:
                    Bob += 1
    else:
        print("Length of Array Mismatching.. Error!!!")

    result = []
    result.append(Alice)
    result.append(Bob)

    return result

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = compareTriplets(a, b)
    print(*res, end = ' ')