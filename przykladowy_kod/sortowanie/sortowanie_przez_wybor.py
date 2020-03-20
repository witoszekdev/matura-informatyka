def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)): # range typically starts from 0, so we pass 1 as first argument
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    # we create new array to not modify the original one outside the scope of the function
    old_arr = list(arr)
    new_arr = []
    for i in range(len(old_arr)):
        smallest_index = find_smallest(old_arr)
        new_arr.append(old_arr.pop(smallest_index))
    return new_arr


if __name__ == "__main__":
    arr = [1, 4, 9, 3, 2, 14, 3]
    print(selection_sort(arr))
    print(arr)

