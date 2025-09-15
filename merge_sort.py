'''
Merge Sort
09/15/2025
time complexity : O(nlogn) in worst case and optimal case(same).
Recursion part is executed like DFS I think. 
'''


def merge(left, right) -> list:
    
    i,j = 0,0
    sorted_list = list()

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    # extend leftover list
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def merge_sort(a: list) -> list:
    
    # Base case
    if len(a) <= 1:
        return a
    
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)
    return merge(left_li, right_li)


if __name__ == "__main__":
    li = [8,5,6,2,4]
    res = merge_sort(li)
    print(res)