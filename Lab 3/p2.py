#python_version == '3.7'

def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    smaller = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    larger = [x for x in a if x > pivot]
    return quicksort(smaller) + equal + quicksort(larger)
