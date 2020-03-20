def binary_search(arr, item):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = int(len(arr) / 2)
        guess = arr[mid]

        if guess == item:
            return arr[mid]
        elif guess < item:
            return binary_search(arr[mid+1:], item)
        else:
            return binary_search(arr[:mid-1], item)

if __name__ == "__main__":
    arr = [1, 2, 4, 8, 12, 22, 43, 101]
    print(binary_search(arr, 8))
    print(binary_search(arr, 43))
    print(binary_search(arr, -1))
