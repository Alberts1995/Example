from random import randint, choice

def python_quiksort_recursive(lst):
    less = []
    equal = []
    great = []
    pivot = choice(lst)

    pivot = choice(lst)

    for element in lst:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            great.append(element)
        else:
            equal.append(element)

    if len(less) > 1:
        less = python_quiksort_recursive(less)
    if len(great) > 1:
        great = python_quiksort_recursive(great)

    return less + equal + great


def quicksort_recursive(lst, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(lst) - 1

    pivot = choice(lst[left:right+1])

    left_ = left
    right_ = right
    while left_ <= right_:
        while lst[left_] < pivot:
            left += 1
        while lst[right_] > pivot:
            right_ -= 1

        if left_ <= right_:
            lst[left_], lst[right_] = lst[right_], lst[left_]
            left_ += 1
            right_ -= 1

        if left < right_:
            quicksort_recursive(lst, left, right_)
        if left_ < right:
            quicksort_recursive(lst, left_, right)




lst = [randint(1, 10) for x in range(7)]
quicksort_recursive(lst)
print(lst)

