def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = int(len(arr) / 2 - 1)
        pivot = arr[pivot_index]
        calculation_arr = arr[:pivot_index] + arr[pivot_index:]
        less = [i for i in calculation_arr if i < pivot]
        more = [i for i in calculation_arr if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)

if __name__ == "__main__":
    arr = [43, 12, 32, 45, 65, 12, 90, 33]
    print(quicksort(arr))
