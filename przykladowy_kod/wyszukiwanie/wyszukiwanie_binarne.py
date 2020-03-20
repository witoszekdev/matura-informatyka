def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None

if __name__ == "__main__":
    arr = [1, 2, 4, 8, 12, 22, 43, 101]
    print(binary_search(arr, 8))
    print(binary_search(arr, 43))
    print(binary_search(arr, -1))
