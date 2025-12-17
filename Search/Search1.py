def bi_search(arr, x, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if l > r:
        return False

    mid = (l + r) // 2

    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        return bi_search(arr, x, l, mid - 1)
    else:
        return bi_search(arr, x, mid + 1, r)


inp = input('Enter Input : ').split('/')
arr = sorted(map(int, inp[0].split()))
k = int(inp[1])

print(bi_search(arr, k))
