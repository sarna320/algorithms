import time


def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1


# 1531021
# 1531 021
# 15 31 02 1
# 1 5 3 1 0 2 1
# 15 13 02 1
# 1135 012
# 0111235
