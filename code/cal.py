def calresult(x):
    out = x**4 - 5*x**3 - 6*x**2 -4*x + 8
    return out

if __name__ == '__main__':
    sequence = [-1, 1, -2, 2, -4, 4, -8, 8]
    for i in range(len(sequence)):
        print(calresult(sequence[i]))

