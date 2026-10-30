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


def tail_k(xs, k):
    return xs if xs == [] or k == 0 else tail_k(tail(xs), k - 1)


def range(n):
    return [] if n == -1 else range(n - 1) + [n]


# ============================================================================ #

# Questão 1


def compactar(xs):
    def count_seq(xs, x):
        return 0 if xs == [] or head(xs) != x else 1 + count_seq(tail(xs), x)

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
    def remove_first(xs, x):
        return (
            []
            if xs == []
            else [head(xs)] + remove_first(tail(xs), x)
            if head(xs) != x
            else tail(xs)
        )

    return (
        []
        if a == [] or b == []
        else [head(a)] + intersecao_multi(tail(a), remove_first(b, head(a)))
        if find(b, head(a))
        else intersecao_multi(tail(a), b)
    )


# Questao 7


def segmentar_crescentes(xs):
    def aux(xs, prev, count):
        return (
            [count]
            if xs == [] or (prev != None and head(xs) <= prev)
            else [head(xs)] + aux(tail(xs), head(xs), count + 1)
        )

    if xs == []:
        return []

    t = aux(xs, None, 0)
    count = last(t)
    t = init(t)

    return [t] + segmentar_crescentes(tail_k(xs, count))


# Questao 8


def compor(fs, x):
    return x if fs == [] else compor(tail(fs), head(fs)(x))


# Questao 9


def entrelacar(ls):
    ls = filter(ls, lambda l: l != [])
    return [] if ls == [] else cat(map(ls, head), entrelacar(map(ls, tail)))


# Questao 10


def starts_with(sub, xs):
    return sub == [] or (
        xs != [] and head(sub) == head(xs) and starts_with(tail(sub), tail(xs))
    )


def ocorrencias(p, xs):
    if p == []:
        return range(len(xs))

    def aux(p, xs, idx):
        return (
            []
            if xs == []
            else ([idx] if starts_with(p, xs) else []) + aux(p, tail(xs), idx + 1)
        )

    return aux(p, xs, 0)


# Questao 11


def first_k(xs, k):
    return [] if xs == [] or k == 0 else [head(xs)] + first_k(tail(xs), k - 1)


def last_k(xs, k):
    return [] if xs == [] or k == 0 else [last(xs)] + last_k(init(xs), k - 1)


def merge_sort(regs):
    def merge(xs, ys):
        return (
            xs
            if ys == []
            else ys
            if xs == []
            else (
                [head(xs)] + merge(tail(xs), ys)
                if head(head(xs)) <= head(head(ys))
                else [head(ys)] + merge(xs, tail(ys))
            )
        )

    if tail(regs) == []:
        return regs
    mid = len(regs) // 2
    first_part = first_k(regs, mid)
    second_part = last_k(regs, len(regs) - mid)
    return merge(merge_sort(first_part), merge_sort(second_part))
