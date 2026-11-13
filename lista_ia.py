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


def index_of(xs, x):
    def aux(xs, x, idx):
        return None if xs == [] else idx if head(xs) == x else aux(tail(xs), x, idx + 1)

    return aux(xs, x, 0)


def filter(xs, f):
    return xs if xs == [] else ([head(xs)] if f(head(xs)) else []) + filter(tail(xs), f)


def map(xs, f):
    return xs if xs == [] else [f(head(xs))] + map(tail(xs), f)


def reduce(xs, f, acc):
    return acc if xs == [] else f(head(xs), reduce(tail(xs), f, acc))


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

# ============================================================================ #

# Questão 1


def compactar(xs):
    def count_seq(xs, x):
        return 0 if xs == [] or head(xs) != x else 1 + count_seq(tail(xs), x)

    if xs == []:
        return []

    c = count_seq(xs, head(xs))
    return prepend(pair(head(xs), c), compactar(tail_k(xs, c)))


def expandir(ts):
    def generate(x, k):
        xs = [x for x in range(0, k)]
        return map(xs, lambda _: x)

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
        xs = [x for x in range(len(xs)+1)]
        return xs

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
    mid = len(xs) // 2
    pivot = head_k(xs, mid)
    lt = filter(xs, lambda x: x < pivot)
    eq = filter(xs, lambda x: x == pivot)
    gt = filter(xs, lambda x: x > pivot)
    return (
        selecionar(lt, k)
        if k < len(lt)
        else pivot
        if k < len(lt) + len(eq)
        else
        selecionar(gt, k - len(lt) - len(gt))
    )


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
        i = [x for x in range(m)]
        j = [x for x in range(n)]
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
    return (
        []
        if a == [] or b == []
        else prepend(pair(head(a), head(b)), zip(tail(a), tail(b)))
    )


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


# Questao 18


def avaliar_posfixa(tokens):
    def is_operator(t):
        return t == "+" or t == "-" or t == "*" or t == "//"

    def evaluate(x, y, t):
        if x == None or y == None:
            return None
        if t == "+":
            return x + y
        if t == "-":
            return x - y
        if t == "*":
            return x * y
        if t == "//":
            return None if y == 0 else x // y

    if filter(tokens, is_operator) == []:
        return head(tokens) if len(tokens) == 1 else None

    def aux(tokens, xs):
        if tokens == []:
            return None if len(xs) != 1 else last(xs)
        t = head(tokens)
        if is_operator(t):
            if len(xs) < 2:
                return None
            left = last(init(xs))
            right = last(xs)
            x = evaluate(left, right, t)
            xs = init(init(xs))
            xs = append(xs, x)
            return aux(tail(tokens), xs)
        xs = append(xs, t)
        return aux(tail(tokens), xs)

    return aux(tokens, [])


# Questao 19


def corresponde(pattern, text):
    def aux(pattern, text):
        if pattern == []:
            return text == []
        p = head(pattern)
        if p != "*" and text == []:
            return False
        if p == "*":
            if tail(pattern) == []:
                return True
            pp = head(tail(pattern))
            if pp == "?" or pp == "*":
                return corresponde(tail(pattern), text)
            k = index_of(text, pp)
            return False if k == None else corresponde(tail(pattern), tail_k(text, k))
        t = head(text)
        return (
            False
            if (p == "?" and text == []) or (p != "?" and t != p)
            else corresponde(tail(pattern), tail(text))
        )

    return aux(list(pattern), list(text))


# 20 Distância de edição


def min(xs):
    def aux(xs, x):
        return (
            x
            if xs == []
            else aux(tail(xs), head(xs))
            if (x == None or head(xs) < x)
            else aux(tail(xs), x)
        )

    return aux(xs, None)


def max(xs):
    def aux(xs, x):
        return (
            x
            if xs == []
            else aux(tail(xs), head(xs))
            if (x == None or head(xs) > x)
            else aux(tail(xs), x)
        )

    return aux(xs, None)


def distancia(a, b):
    def aux(a, b):
        if a == []:
            return len(b)
        if b == []:
            return len(a)
        if head(a) == head(b):
            return aux(tail(a), tail(b))
        if len(a) == len(b):
            return 1 + aux(tail(a), tail(b))
        return min(
            [1 + aux(tail(a), b), 1 + aux(tail(a), tail(b)), 1 + aux(a, init(b))]
        )

    return aux(list(a), list(b))


# 21 Maior subsequência comum com desempate


def scm(a, b):
    def aux(a, b):
        return (
            []
            if a == [] or b == []
            else aux(a, tail(b))
            if head(a) != head(b)
            else prepend(head(a), aux(tail(a), tail(b)))
        )

    if a == "":
        return a
    if b == "":
        return b
    x = aux(list(a), list(b))
    y = scm(tail(a), b)
    return x if len(x) > len(y) else y if len(x) < len(y) else x if x < y else y


# 22 Todos os subconjuntos com soma-alvo


def set(xs):
    return reduce(xs, lambda x, acc: acc if find(acc, x) else prepend(x, acc), [])


def powerset(xs):
    ys = map(xs, lambda x: filter(xs, lambda y: x != y))
    return set([[]] if ys == [] else [xs] + reduce(map(ys, powerset), cat, []))


def subconjuntos_soma(xs, target):
    ps = powerset(xs)
    ps = filter(ps, lambda p: reduce(p, sum, 0) == target)
    return ps


# 26 Todas as soluções de n rainhas

def rainhas(n):
    def abs(x): return x if x >= 0 else -x
    def safe(c, qs, d=1): return qs == [] or (c != head(qs) and abs(c-head(qs)) != d and safe(c, tail(qs), d+1))
    def go(k):
        return [[]] if k == 0 else [[c] + qs for qs in go(k-1) for c in range(n) if safe(c,qs)]
    return go(n)
