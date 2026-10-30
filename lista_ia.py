def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def init(xs):
    return xs[0 : len(xs) - 1]


def last(xs):
    return xs[-1]


def len(xs):
    return 0 if xs == [] else 1 + len(tail(xs))


def cat(xs, ys):
    return xs if ys == [] else cat(xs + [head(ys)], tail(ys))


def find(xs, x):
    return False if xs == [] else True if head(xs) == x else find(tail(xs), x)


def filter(xs, f):
    return xs if xs == [] else ([head(xs)] if f(head(xs)) else []) + filter(tail(xs), f)


def map(xs, f):
    return xs if xs == [] else [f(head(xs))] + map(tail(xs), f)


def count(xs, x):
    return (
        0
        if xs == []
        else 1 + count(tail(xs), x)
        if head(xs) == x
        else count(tail(xs), x)
    )


# ============================================================================ #

# Questão 1


def compactar(xs):
    def count_seq(xs, x):
        return 0 if xs == [] or head(xs) != x else 1 + count_seq(tail(xs), x)

    def tail_k(xs, k):
        return xs if xs == [] or k == 0 else tail_k(tail(xs), k - 1)

    return (
        []
        if xs == []
        else [[head(xs), count_seq(xs, head(xs))]]
        + compactar(tail_k(xs, count_seq(xs, head(xs))))
    )


def expandir(ts):
    def generate(x, k):
        return [] if k == 0 else [x] + generate(x, k - 1)

    return (
        []
        if ts == []
        else cat(generate(head(head(ts)), last(head(ts))), expandir(tail(ts)))
    )


# Questao 2


def rotacionar(xs, k):
    if k == 0 or xs == [] or len(xs) == 1:
        return xs
    return (
        rotacionar([last(xs)] + init(init(xs)) + [last(init(xs))], k + 1)
        if k < 0
        else rotacionar([head(tail(xs))] + tail(tail(xs)) + [head(xs)], k - 1)
    )


# Questao 3


def janelas(xs, k):
    def aux(xs, k):
        return [] if k == 0 else [head(xs)] + aux(tail(xs), k - 1)

    return [] if len(xs) < k else [aux(xs, k)] + janelas(tail(xs), k)


# Questao 4


def particionar(f, xs):
    def aux1(f, xs):
        return (
            [] if xs == [] else ([head(xs)] if f(head(xs)) else []) + aux1(f, tail(xs))
        )

    def aux2(f, xs):
        return (
            []
            if xs == []
            else ([head(xs)] if not f(head(xs)) else []) + aux2(f, tail(xs))
        )

    return [aux1(f, xs), aux2(f, xs)]


# Questao 5


def histograma(xs):
    def filter_x(xs, x):
        return filter(xs, lambda y: y != x)

    return (
        []
        if xs == []
        else [[head(xs), count(xs, head(xs))]] + histograma(filter_x(xs, head(xs)))
    )


# Questao 6


def intersecao_multi(a, b):
    pass
