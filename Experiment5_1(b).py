def root(f, a, b):
    if f(a) * f(b) == 0:
        if f(a) == 0:
            return a
        else:
            return b
    if f(a) * f(b) > 0:
        return None
    else:
        if a > b:
            a, b = b, a
            c = (a + b) / 2
            while abs(f(c)) > 1e-6:
                c = (a + b) / 2
                if f(a) > 0 > f(b):
                    if f(c) > 0:
                        a = c
                    else:
                        b = c
                else:
                    if f(c) > 0:
                        b = c
                    else:
                        a = c
            return round(c, 3)
        else:
            c = (a + b) / 2
            while abs(f(c)) > 1e-6:
                c = (a + b) / 2
                if f(a) > 0 > f(b):
                    if f(c) > 0:
                        a = c
                    else:
                        b = c
                else:
                    if f(c) > 0:
                        b = c
                    else:
                        a = c
            return round(c, 3)


def func(x):
    return x ** 2 - x - 30


if __name__ == '__main__':
    print(root(func, -4, 8))
