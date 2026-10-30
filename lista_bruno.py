def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def init(xs):
    return xs[0 : len(xs) - 1]


def last(xs):
    return xs[len(xs) - 1]


# Q5


def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


# Q6


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# Q7


def compute_series(n):
    return 1 if n == 0 else 1 / factorial(n) + compute_series(n - 1)


# Q8


def questao8(xs):
    return (
        0
        if head(xs) == 0
        else questao8(tail(xs))
        if head(xs) > 0
        else head(xs) + questao8(tail(xs))
    )


# Q9


def questao9(xs):
    return (
        0
        if xs == []
        else 1 + questao9(tail(xs))
        if head(xs) < 0
        else questao9(tail(xs))
    )


# Q10


def len(xs):
    return 0 if xs == [] else 1 + len(tail(xs))


# Q11


def ehPrimo(x):
    def aux(x, i):
        return (
            x == 2
            if x <= 2
            else False
            if x % i == 0
            else True
            if i * i > x
            else aux(x, i + 1)
        )

    return aux(x, 2)


# Q12


def nPrimos(n):
    def aux(xs, x):
        return (
            xs
            if len(xs) == n
            else aux(xs, x + 1)
            if ehPrimo(x) == False
            else aux(xs + [x], x + 1)
        )

    return aux([], 0)


# Q13


def cat(xs, ys):
    return xs if ys == [] else cat(xs + [head(ys)], tail(ys))


# Q14


def inList(xs, x):
    return False if xs == [] else True if head(xs) == x else inList(tail(xs), x)


# Q15


def union(xs, ys):
    return (
        xs
        if ys == []
        else union(xs, tail(ys))
        if inList(xs, head(ys))
        else union(xs + [head(ys)], tail(ys))
    )


# Q16


def qtdMaiorQue(xs, n):
    return (
        0
        if xs == []
        else 1 + qtdMaiorQue(tail(xs), n)
        if head(xs) > n
        else qtdMaiorQue(tail(xs), n)
    )


# Q17
def questao17(xs, n):
    return (
        []
        if xs == []
        else [head(xs)] + questao17(tail(xs), n)
        if head(xs) > n
        else questao17(tail(xs), n)
    )


# Q18
def invertelista(xs):
    return [] if xs == [] else [last(xs)] + invertelista(tail(init(xs))) + [head(xs)]


# Q19
def geraPalindromo(xs):
    return [] if xs == [] else [head(xs)] + geraPalindromo(tail(xs)) + [head(xs)]


# Q20
def strip(xs, ys):
    return (
        []
        if ys == []
        else strip(xs, tail(ys))
        if inList(xs, head(ys))
        else [head(ys)] + strip(xs, tail(ys))
    )


# Q21
def consoantList(xs, ys):
    return (
        True
        if xs == []
        else False
        if ys == []
        else consoantList(tail(xs), tail(ys))
        if inList(xs, head(ys))
        else consoantList(xs, tail(ys))
    )
