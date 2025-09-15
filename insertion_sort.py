'''
Insertion Sort
09/15/2025
time complexity : O(n^2) in worst case, O(n) in optimal case.
'''

def insertion_sort_forloop(a: list) -> list:
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a



def insertion_sort_while(a: list) -> list:
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key: # if array is already sorted, then while loop always false.
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key # key value was overwritten, so a[j+1] = key.
    return a


if __name__ == "__main__":
    li = [8,5,6,2,4]
    res = insertion_sort_while(li)
    print(res)