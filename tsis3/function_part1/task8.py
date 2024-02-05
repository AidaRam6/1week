def spy_game(nums):
    a = []
    for i in nums:
        if int(i) == 0 or int(i) == 7:
            a.append(int(i))
    for i in range(len(a) - 2):
        if a[i] == 0 and a[i+1] == 0 and a[i+2] == 7:
            return True

    return False
x = list(input().split())
print(spy_game(x))