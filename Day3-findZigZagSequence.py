
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid-1], a[n-1] = a[n-1], a[mid-1] # wrong index assignment when switching the last number for the middle one

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st-1], a[ed-1] = a[ed-1], a[st-1] # wrong index. We need to switch the number before the last one with the one next to the middle one
        st = st + 1
        ed = ed # Impossible to get n+1 index of the array

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
