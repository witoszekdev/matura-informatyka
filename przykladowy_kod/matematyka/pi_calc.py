# Szereg Leibniza
def calculate_pi(max):
    pi = 1
    for i in range(0, max + 1):
        mianownik = i * 2 + 3
        if i % 2 == 0:
            # parzyste
            pi -= 1/mianownik
        else:
            # nieparzyste
            pi += 1/mianownik
    pi *= 4
    return pi


if __name__ == "__main__":
    print(calculate_pi(10000000))
