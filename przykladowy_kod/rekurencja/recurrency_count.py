def count(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + count(list[1:])

if __name__ == "__main__":
    print(count(["a", "b", "c"]))
