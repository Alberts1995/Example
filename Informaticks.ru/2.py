def bin_search(arr, target, kind="<="):
    assert kind in ["<=", ">="]

    if kind == "<=":
        comp = lambda a, b: a <= b
    else:
        comp = lambda a, b: a < b
    
    l = 0
    r = len(a) - 1
    
    while l < r - 1:
        m = (l + r) // 2
        if comp(a[m], target):
            l = m
        else:
            r = m
    if kind == "<=":
        return arr[l]
    else:
        return arr[r]

def nearest(arr, target):
    nearest_le = bin_search(arr, target, "<=")
    nearest_ge = bin_search(arr, target, ">=")
    if nearest_ge - target < target - nearest_le:
        return nearest_ge
    else:
        return nearest_le

_ = input()
a = [int(x) for x in input().split()]
a = [float("-Infinity")] + a + [float("+Infinity")]

for target in map(int, input().split()):
    print(nearest(a, target))

