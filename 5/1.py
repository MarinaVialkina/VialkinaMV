def f(n,k):
    """Функция находит все квадраты натуральных чисел, не превосходящие N, в порядке возрастания."""
    while k<=n:
        print(k**2)
        k+=1


n=int(input('Ввод n:'))
k=1
f(n,k)