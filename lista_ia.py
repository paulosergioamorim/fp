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


def reduce(xs, f, acc):
    return acc if xs == [] else f(head(xs), acc) + reduce(tail(xs), f, acc)


def sum(x, acc):
    return x + acc


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


def head_k(xs, k):
    return None if xs == [] else head(xs) if k == 0 else head_k(tail(xs), k - 1)


def range(n):
    return [0] if n == 0 else range(n - 1) + [n]


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
        return map(range(k - 1), lambda _: x)

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


def first_k_elements(xs, k):
    return [] if xs == [] or k == 0 else [head(xs)] + first_k_elements(tail(xs), k - 1)


def last_k_elements(xs, k):
    return [] if xs == [] or k == 0 else [last(xs)] + last_k_elements(init(xs), k - 1)


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
    first_part = first_k_elements(regs, mid)
    second_part = last_k_elements(regs, len(regs) - mid)
    return merge(merge_sort(first_part), merge_sort(second_part))


# Questao 12


def selecionar(xs, k):
    if k < 0 or k >= len(xs):
        return None

    def aux(xs, k):
        mid = len(xs) // 2
        pivot = head_k(xs, mid)
        lt = filter(xs, lambda x: x < pivot)
        eq = filter(xs, lambda x: x == pivot)
        gt = filter(xs, lambda x: x > pivot)
        t = len(lt)
        return (
            head(xs)
            if len(xs) == 1 or (lt == [] and gt == [])
            else aux(lt, k)
            if t > k
            else aux(gt, k - t - 1)
            if t < k
            else aux(eq, k - t)
        )

    return aux(xs, k)


# Questao 13


def cartesian_product(a, b):
    return (
        []
        if a == [] or b == []
        else cat(map(a, lambda x: [x, head(b)]), cartesian_product(a, tail(b)))
    )


def convoluir(a, b):
    if a == [] or b == []:
        return []
    m = len(a)
    n = len(b)
    c = m + n - 1

    def aux(a, b, k):
        if k == -1:
            return []
        i = range(m - 1)
        j = range(n - 1)
        p = cartesian_product(i, j)
        p = filter(p, lambda x: reduce(x, sum, 0) == k)
        p = map(p, lambda x: head_k(a, head(x)) * head_k(b, last(x)))
        p = reduce(p, sum, 0)
        return aux(a, b, k - 1) + [p]

    return aux(a, b, c - 1)


# Questao 14


def reverse(xs):
    return [] if xs == [] else [last(xs)] + reverse(init(xs))


def transpose(m):
    return (
        [] if m == [] or head(m) == [] else cat([map(m, head)], transpose(map(m, tail)))
    )


def girar_matriz(m):
    return transpose(reverse(m))


# Questao 15


def pair(a, b):
    return [a, b]


def zip(a, b):
    return [] if a == [] or b == [] else prepend(pair(a, b), zip(tail(a), tail(b)))


def multiplicar_matrizes(A, B):
    B = transpose(B)
    return map(
        A,
        lambda a: map(
            B, lambda b: reduce(map(zip(a, b), lambda x: head(x) * last(x)), sum, 0)
        ),
    )


# Questao 16


def girar_90deg_anti(m):
    if m == [] or head(m) == []:
        return []
    r = map(m, last)
    return cat([r], girar_90deg_anti(map(m, init)))


def espiral(m):
    if m == []:
        return []
    r = head(m)
    rest = tail(m)
    rest = girar_90deg_anti(rest)
    return cat(r, espiral(rest))


# Questao 17


def append(xs, x):
    return xs + [x]


def prepend(x, xs):
    return [x] + xs


def balanceados(text):
    def remove_last_if_equal(xs, x):
        return [] if xs == [] else init(xs) if last(xs) == x else xs

    def aux(chrs, xs):
        if chrs == []:
            return xs == []
        c = head(chrs)
        chrs = tail(chrs)
        if c == "(":
            return aux(chrs, append(xs, ")"))
        if c == "[":
            return aux(chrs, append(xs, "]"))
        if c == "{":
            return aux(chrs, append(xs, "}"))
        if c == ")" or c == "]" or c == "}":
            return (
                False
                if xs == []
                else aux(chrs, init(xs))
                if last(xs) == c
                else aux(chrs, xs)
            )
        return aux(chrs, xs)

    return aux(list(text), [])


# Quick Sort


def quick_sort(xs):
    if xs == []:
        return []
    pivot = selecionar(xs, len(xs) // 2)
    lt = filter(xs, lambda x: x < pivot)
    eq = filter(xs, lambda x: x == pivot)
    gt = filter(xs, lambda x: x > pivot)
    lt = quick_sort(lt)
    gt = quick_sort(gt)
    return cat(lt, cat(eq, gt))
