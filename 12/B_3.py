def f():
    n = int(input('Ввод числа:'))
    if n == 0:
        return
    else:
        print(n)
        n = int(input('Ввод числа:'))
        if n == 0:
            return
        f()



f()