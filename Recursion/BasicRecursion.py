def func(x,n):
    if n == 0:
        return
    print(x)
    n -= 1
    func(x,n)

func(15,4)