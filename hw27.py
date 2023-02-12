def generator(val, q, n):
    prev = val
    for i in range(1, n):
        curr = prev*q
        print(curr)
        prev = curr
    yield "That`s it"


a = generator(1, 7, 5)
print(next(a))