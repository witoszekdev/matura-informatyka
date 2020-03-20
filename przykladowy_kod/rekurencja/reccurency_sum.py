def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

if __name__ == "__main__":
    print(sum([4, 6, 1]))
