for i in range(3):
    T = list(map(int, input().split()))
    if T.count(0) == 1:
        print("A")
    elif T.count(0) == 2:
        print("B")
    elif T.count(0) == 3:
        print("C")   
    elif T.count(0) == 4:
        print("D")
    else:
        print("E")