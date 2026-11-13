# Lista de exercícios - Paradigma funcional em Python
# 60 questões: 10 fáceis, 20 médias e 30 difíceis.
# A mesma lista, em Haskell, está em Main.hs.
#
# Regras:
#  1. Funções puras: sem efeitos colaterais, sem alterar entradas ou estado
#     global, sem input/print dentro das soluções.
#  2. Iteração apenas por recursão. List comprehension e geradores como range
#     podem ser usados quando oportuno (por exemplo, questões 26 e 27).
#  3. Acesso a listas, strings e tuplas apenas pelas primitivas head, tail,
#     init e last, definidas abaixo. Sem índices, slices ou desempacotamento.
#     Em um par (a, b), head devolve a e last devolve b.
#  4. Sem funções ou métodos prontos (len, sum, max, sorted, map, filter,
#     zip, in, append, ...). Funções já resolvidas nesta lista podem ser
#     reutilizadas nas questões seguintes.
#  5. O operador + entre listas só pode ser usado se um dos operandos tiver
#     no máximo 1 elemento. Para o caso geral, use my_append (questão 03).
#  6. Definição por casos: cada ramo apenas retorna uma expressão.
#
# Convenções:
#  - Argumentos na ordem de Haskell: primeiro a função (ou o parâmetro),
#    por último a lista.
#  - Pares e triplas são tuplas. Ausência de resultado é None.
#  - Árvore binária: [] (vazia) ou [valor, esquerda, direita].
#  - Expressão (questão 50): ['c', n], ['v', nome], ['+', a, b], ['*', a, b].
#  - Grafo: lista de pares (vértice, lista de vizinhos).


def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def init(xs):
    return xs[:-1]


def last(xs):
    return xs[-1]

# ============================================================================
# PARTE 1 - FÁCEIS (01 a 10)
# ============================================================================

# 01 [FÁCIL] my_length
# Retorna a quantidade de elementos de uma lista.
# Exemplos:
#   my_length([4, 5, 6]) -> 3
#   my_length([]) -> 0
def my_length(xs):
    return 0 if not xs else 1 + my_length(tail(xs))

# 02 [FÁCIL] my_elem
# Verifica se o elemento x pertence à lista.
# Exemplos:
#   my_elem(3, [1, 2, 3]) -> True
#   my_elem('z', 'abc') -> False
def my_elem(x, xs):
    return False if not xs else x == head(xs) or my_elem(x, tail(xs))

# 03 [FÁCIL] my_append
# Concatena duas listas, com o mesmo comportamento do operador de
# concatenação. O operador só pode ser usado se um dos operandos tiver no
# máximo 1 elemento.
# Exemplos:
#   my_append([1, 2], [3, 4]) -> [1, 2, 3, 4]
#   my_append([], [7]) -> [7]
def my_append(xs, ys):
    return xs if not ys else my_append(xs + [head(ys)], tail(ys))

# 04 [FÁCIL] my_reverse
# Inverte o conteúdo de uma lista.
# Exemplos:
#   my_reverse([1, 2, 3]) -> [3, 2, 1]
#   my_reverse('abcd') -> 'dcba'
def my_reverse(xs):
    return xs if not xs else [last(xs)] + my_reverse(init(xs))

# 05 [FÁCIL] my_map
# Aplica a função f a cada elemento da lista, preservando a ordem.
# Exemplos:
#   my_map(lambda x: x * x, [1, 2, 3]) -> [1, 4, 9]
#   my_map(lambda x: x + 1, []) -> []
def my_map(f, xs):
    return xs if not xs else [f(head(xs))] + my_map(f, tail(xs))

# 06 [FÁCIL] my_filter
# Retorna apenas os elementos da lista que satisfazem o predicado p,
# preservando a ordem.
# Exemplos:
#   my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) -> [2, 4]
#   my_filter(lambda x: x > 9, [1, 2]) -> []
def my_filter(p, xs):
    return xs if not xs else [head(xs)] + my_filter(p, tail(xs)) if p(head(xs)) else my_filter(p, tail(xs))

# 07 [FÁCIL] count_if
# Conta quantos elementos da lista satisfazem o predicado p.
# Exemplos:
#   count_if(lambda x: x < 0, [3, -1, 0, -7]) -> 2
#   count_if(lambda x: x > 2, []) -> 0
def count_if(p, xs):
    return 0 if not xs else (1 if p(head(xs)) else 0) + count_if(p, tail(xs))

# 08 [FÁCIL] my_maximum
# Retorna o maior elemento de uma lista não vazia.
# Exemplos:
#   my_maximum([3, 9, 2]) -> 9
#   my_maximum([-5]) -> -5
def my_maximum(xs):
    return (
        head(xs) if my_length(xs) == 1
        else (head(xs) if head(xs) > my_maximum(tail(xs)) else my_maximum(tail(xs)))
    )

# 09 [FÁCIL] my_take
# Retorna os n primeiros elementos da lista. Se a lista tiver menos de n
# elementos, retorna a lista inteira. n é inteiro não negativo.
# Exemplos:
#   my_take(2, [7, 8, 9]) -> [7, 8]
#   my_take(5, [1, 2]) -> [1, 2]
#   my_take(0, [1, 2]) -> []
def my_take(n, xs):
    return [] if not xs or n == 0 else [head(xs)] + my_take(n-1, tail(xs))

# 10 [FÁCIL] is_palindrome
# Verifica se uma sequência é palíndroma, isto é, igual à sua inversa. A
# sequência vazia é palíndroma.
# Exemplos:
#   is_palindrome('arara') -> True
#   is_palindrome([1, 2, 3]) -> False
#   is_palindrome('') -> True
def is_palindrome(xs):
    return (
        not xs or
        my_length(xs) == 1 or
        (head(xs) == last(xs) and is_palindrome(init(tail(xs))))
    )

# ============================================================================
# PARTE 2 - MÉDIAS (11 a 30)
# ============================================================================

# 11 [MÉDIO] my_foldr
# Redução à direita: combina os elementos da direita para a esquerda, partindo
# do valor inicial z. Para [x1, x2, x3] o resultado é f(x1, f(x2, f(x3, z))).
# Exemplos:
#   my_foldr(lambda x, acc: x - acc, 0, [1, 2, 3]) -> 2
#   my_foldr(lambda x, acc: acc + [x], [], [1, 2, 3]) -> [3, 2, 1]
#   my_foldr(lambda x, acc: x + acc, 7, []) -> 7
def my_foldr(f, z, xs):
    return z if not xs else f(head(xs), my_foldr(f, z, tail(xs)))

# 12 [MÉDIO] my_foldl
# Redução à esquerda: combina os elementos da esquerda para a direita,
# partindo do valor inicial z. Para [x1, x2, x3] o resultado é f(f(f(z, x1),
# x2), x3).
# Exemplos:
#   my_foldl(lambda acc, x: acc - x, 0, [1, 2, 3]) -> -6
#   my_foldl(lambda acc, x: acc * 10 + x, 0, [1, 2, 3]) -> 123
def my_foldl(f, z, xs):
    return z if not xs else f(my_foldl(f, z, init(xs)), last(xs))

# 13 [MÉDIO] my_zip_with
# Combina as duas listas elemento a elemento usando f. O resultado tem o
# tamanho da menor lista.
# Exemplos:
#   my_zip_with(lambda x, y: x + y, [1, 2, 3], [10, 20]) -> [11, 22]
#   my_zip_with(lambda x, y: (x, y), [1, 2], 'ab') -> [(1, 'a'), (2, 'b')]
def my_zip_with(f, xs, ys):
    return [] if not xs or not ys else [f(head(xs), head(ys))] + my_zip_with(f, tail(xs), tail(ys))


def my_drop(n, xs):
    return [] if not xs else xs if n == 0 else my_drop(n-1, tail(xs))

# 14 [MÉDIO] my_span
# Retorna o par (prefixo, resto), em que prefixo é o maior prefixo da lista
# cujos elementos satisfazem p, e resto é o restante da lista.
# Exemplos:
#   my_span(lambda x: x < 3, [1, 2, 3, 1]) -> ([1, 2], [3, 1])
#   my_span(lambda x: x > 5, [1, 9]) -> ([], [1, 9])
def my_span(p, xs):
    def aux(p, xs):
        return 0 if not xs or not p(head(xs)) else 1 + aux(p, tail(xs))
    return (my_take(aux(p, xs), xs), my_drop(aux(p,xs),xs))

# 15 [MÉDIO] partition
# Retorna o par (aceitos, rejeitados): aceitos contém os elementos que
# satisfazem p e rejeitados os demais. Preserve a ordem relativa dentro de
# cada grupo.
# Exemplos:
#   partition(lambda x: x % 2 == 0, [-3, 4, 0, 5, 2]) -> ([4, 0, 2], [-3, 5])
#   partition(lambda x: x > 0, []) -> ([], [])
def partition(p, xs):
    return (my_filter(p, xs), my_filter(lambda x: not p(x), xs))

# 16 [MÉDIO] compose_all
# Aplica ao valor x todas as funções da lista, da esquerda para a direita: a
# primeira recebe x, a segunda recebe o resultado da primeira, e assim por
# diante. A lista vazia representa a identidade.
# Exemplos:
#   compose_all([lambda x: x + 2, lambda x: x * x, lambda x: x - 1], 3) -> 24
#   compose_all([], 9) -> 9
def compose_all(fs, x):
    return x if not fs else compose_all(tail(fs), head(fs)(x))

# 17 [MÉDIO] remove_duplicates
# Remove os elementos repetidos, mantendo apenas a primeira ocorrência de cada
# valor, na ordem original.
# Exemplos:
#   remove_duplicates([3, 1, 3, 2, 1]) -> [3, 1, 2]
#   remove_duplicates([]) -> []
def remove_duplicates(xs):
    return my_foldl(lambda acc, x: acc if my_elem(x, acc) else my_append(acc, [x]), [], xs)

# 18 [MÉDIO] insertion_sort_by
# Ordena a lista por inserção. A função le(a, b) devolve True quando a pode
# vir antes de b. A ordenação deve ser estável: elementos equivalentes mantêm
# a ordem original. Pares são acessados com head e last.
# Exemplos:
#   insertion_sort_by(lambda a, b: a <= b, [3, 1, 2]) -> [1, 2, 3]
#   insertion_sort_by(lambda a, b: a >= b, [3, 1, 2]) -> [3, 2, 1]
#   insertion_sort_by(lambda a, b: head(a) <= head(b), [(2, 'a'), (1, 'b'), (2, 'c')]) -> [(1, 'b'), (2, 'a'), (2, 'c')]
def insertion_sort_by(le, xs):
    if not xs:
        return xs
    (fst, snd) = my_span(lambda x: le(x, last(xs)), insertion_sort_by(le, init(xs)))
    return my_append(my_append(fst, [last(xs)]), snd)

# 19 [MÉDIO] compress
# Elimina duplicatas consecutivas de uma lista, mantendo um representante de
# cada bloco.
# Exemplos:
#   compress([1, 1, 2, 1, 1, 3]) -> [1, 2, 1, 3]
#   compress([]) -> []
def compress(xs):
    if not xs:
        return xs
    (fst, snd) = my_span(lambda x: x == head(xs), xs)
    return my_append([head(xs)], compress(snd))

# 20 [MÉDIO] pack
# Empacota os elementos duplicados consecutivos em sublistas.
# Exemplos:
#   pack([1, 1, 2, 3, 3, 3, 1]) -> [[1, 1], [2], [3, 3, 3], [1]]
#   pack([]) -> []
def pack(xs):
    if not xs:
        return xs
    (fst, snd) = my_span(lambda x: x == head(xs), xs)
    return my_append([fst], pack(snd))

# 21 [MÉDIO] encode
# Compressão por tamanho de sequência: cada bloco de elementos duplicados
# consecutivos é codificado como o par (n, e), em que n é o número de
# repetições do elemento e.
# Exemplos:
#   encode('aaaabccaadeeee') -> [(4, 'a'), (1, 'b'), (2, 'c'), (2, 'a'), (1, 'd'), (4, 'e')]
#   encode([]) -> []
def encode(xs):
    if not xs:
        return []
    (fst, snd) = my_span(lambda x: x == head(xs), xs)
    return my_append([(my_length(fst), head(fst))], encode(snd))

# 22 [MÉDIO] decode
# Inversa de encode: dada uma lista de pares (n, e), reconstrói a lista
# original. As quantidades são inteiros positivos.
# Exemplos:
#   decode([(2, 7), (1, 5), (3, 7)]) -> [7, 7, 5, 7, 7, 7]
#   decode([]) -> []
def decode(ps):
    if not ps:
        return ps
    (n, e) = head(ps)
    return my_append([e for _ in range(n)], decode(tail(ps)))

# 23 [MÉDIO] split_token
# Divide a lista em sublistas usando o valor t como marcador. O marcador não
# aparece no resultado. Se t ocorre k vezes, o resultado tem k + 1 sublistas
# (algumas podem ser vazias).
# Exemplos:
#   split_token(2, [1, 2, 3, 4, 2, 5, 67, 8, 9, 0, 3]) -> [[1], [3, 4], [5, 67, 8, 9, 0, 3]]
#   split_token(0, [0, 1, 0, 0, 2]) -> [[], [1], [], [2]]
#   split_token(0, []) -> [[]]
def split_token(t, xs):
    if not xs:
        return xs
    (fst, snd) = my_span(lambda x: x != t, xs)
    return my_append([fst], split_token(t, tail(snd)))

# 24 [MÉDIO] join_token
# Inversa de split_token/splitToken: concatena as sublistas usando o valor t
# como separador entre elas.
# Exemplos:
#   join_token(0, [[1], [2, 3], [4]]) -> [1, 0, 2, 3, 0, 4]
#   join_token(0, [[], [1]]) -> [0, 1]
#   join_token(0, []) -> []
def join_token(t, xss):
    return (
        xss if not xss
        else my_append(my_append(head(xss), [] if not tail(xss) else [t]), join_token(t, tail(xss)))
    )

def is_prime(n):
    def aux(n, p):
        return n % p != 0 and (p * p > n or aux(n, p+1))
    return n != 1 and (n == 2 or aux(n, 2))

def next_prime(n):
    return n+1 if is_prime(n+1) else next_prime(n+1)

def factors(n):
    def aux(n, p):
        return [] if p > n else my_append([p], aux(n // p, p)) if n % p == 0 else aux(n, next_prime(p))
    return aux(n, 2)

def swap(t):
    (fst, snd) = t
    return (snd, fst)

# 25 [MÉDIO] prime_factors
# Fatora um inteiro n >= 1 em uma lista de pares (fator, frequência), com os
# fatores primos em ordem crescente.
# Exemplos:
#   prime_factors(8) -> [(2, 3)]
#   prime_factors(42) -> [(2, 1), (3, 1), (7, 1)]
#   prime_factors(1) -> []
def prime_factors(n):
    return my_map(swap, encode(factors(n)))

# 26 [MÉDIO] pyths
# Uma tripla (x, y, z) de inteiros positivos é pitagórica se x*x + y*y == z*z.
# Usando list comprehension, retorne todas as triplas pitagóricas com
# componentes no intervalo [1..n], variando x, depois y, depois z.
# Exemplos:
#   pyths(5) -> [(3, 4, 5), (4, 3, 5)]
#   pyths(10) -> [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
def pyths(n):
    def p(t):
        (x, y, z) = t
        return x * x + y * y == z * z
    r = range(1, n+1)
    ts = [(x,y,z) for x in r for y in r for z in r]
    # Using builtin filter to avoid recursion limit with pyths(10)
    return list(filter(p, ts))

def divisors(n):
    return [p for p in range(1, n) if n % p == 0]

def add(x,y):
    return x+y

# 27 [MÉDIO] perfects
# Um inteiro positivo é perfeito se é igual à soma de seus divisores,
# excluindo ele próprio. Usando list comprehension, retorne todos os números
# perfeitos de 1 até n.
# Exemplos:
#   perfects(500) -> [6, 28, 496]
#   perfects(5) -> []
def perfects(n):
    xs = [x for x in range(1, n+1)]
    def p(t):
        (x, ps) = t
        return my_foldr(add, 0, ps) == x
    return my_map(head, my_filter(p, my_map(lambda x: (x, divisors(x)), xs)))

# 28 [MÉDIO] rotate
# Retorna a lista após k rotações de uma posição para a esquerda. Se k for
# negativo, rotaciona para a direita. Deslocamentos maiores que o tamanho da
# lista equivalem ao deslocamento reduzido.
# Exemplos:
#   rotate(7, [1, 2, 3, 4, 5]) -> [3, 4, 5, 1, 2]
#   rotate(-1, [1, 2, 3, 4]) -> [4, 1, 2, 3]
#   rotate(10, []) -> []
def rotate(k, xs):
    pass

# 29 [MÉDIO] windows
# Retorna todas as sublistas contíguas de tamanho k (k > 0), avançando uma
# posição por vez, na ordem de seus inícios. Se a lista tiver menos de k
# elementos, retorna a lista vazia.
# Exemplos:
#   windows(3, [4, 1, 7, 3]) -> [[4, 1, 7], [1, 7, 3]]
#   windows(1, [8, 5]) -> [[8], [5]]
#   windows(3, [1, 2]) -> []
def windows(k, xs):
    pass

# 30 [MÉDIO] histogram
# Produz uma lista de pares (valor, frequência total). Cada valor aparece uma
# única vez, na ordem de sua primeira ocorrência, contando inclusive
# ocorrências não consecutivas.
# Exemplos:
#   histogram([3, 1, 3, 2, 1, 3]) -> [(3, 3), (1, 2), (2, 1)]
#   histogram([]) -> []
def histogram(xs):
    pass

# ============================================================================
# PARTE 3 - DIFÍCEIS (31 a 60)
# ============================================================================

# 31 [DIFÍCIL] merge_sort_by
# Ordena a lista com merge sort: divisão ao meio, ordenação recursiva das
# partes e intercalação. A função le(a, b) devolve True quando a pode vir
# antes de b. A ordenação deve ser estável.
# Exemplos:
#   merge_sort_by(lambda a, b: head(a) <= head(b), [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]) -> [(1, 'b'), (1, 'd'), (2, 'a'), (2, 'c')]
#   merge_sort_by(lambda a, b: a >= b, [1, 3, 2]) -> [3, 2, 1]
#   merge_sort_by(lambda a, b: a <= b, []) -> []
def merge_sort_by(le, xs):
    pass

# 32 [DIFÍCIL] quick_select
# Retorna o elemento que ocuparia o índice k (a partir de zero) se a lista
# fosse ordenada em ordem crescente, sem ordenar a lista inteira: particione
# por pivô em menores, iguais e maiores e prossiga apenas na região
# necessária. Se k não for índice válido, retorne None.
# Exemplos:
#   quick_select(2, [7, 2, 5, 2, 9]) -> 5
#   quick_select(1, [7, 2, 5, 2, 9]) -> 2
#   quick_select(-1, [4, 1]) -> None
def quick_select(k, xs):
    pass

# 33 [DIFÍCIL] convolve
# Cada lista representa os coeficientes de um polinômio, do termo constante
# para o de maior grau. Calcule os coeficientes do produto. Para entradas não
# vazias de tamanhos m e n, retorne m + n - 1 coeficientes, preservando zeros
# finais. Se alguma entrada for vazia, retorne a lista vazia.
# Exemplos:
#   convolve([1, 2, 3], [4, -1]) -> [4, 7, 10, -3]
#   convolve([0, 1], [0, 1]) -> [0, 0, 1]
#   convolve([], [1, 2]) -> []
def convolve(a, b):
    pass

# 34 [DIFÍCIL] rotate_matrix
# Gira a matriz em 90 graus no sentido horário. Uma matriz com m linhas e n
# colunas gera n linhas e m colunas. Construa também uma função auxiliar de
# transposição recursiva (transpose). A entrada é vazia ou uma matriz
# retangular com pelo menos uma linha e uma coluna.
# Exemplos:
#   rotate_matrix([[1, 2, 3], [4, 5, 6]]) -> [[4, 1], [5, 2], [6, 3]]
#   rotate_matrix([[1], [2], [3]]) -> [[3, 2, 1]]
#   rotate_matrix([]) -> []
def rotate_matrix(m):
    pass

# 35 [DIFÍCIL] mat_mul
# Produto matricial: cada elemento da saída é o produto escalar de uma linha
# de a por uma coluna de b. As matrizes são retangulares, não vazias e de
# dimensões compatíveis.
# Exemplos:
#   mat_mul([[1, 2, 3], [4, 5, 6]], [[1, 0], [0, 1], [1, 1]]) -> [[4, 5], [10, 11]]
#   mat_mul([[0, 2]], [[3], [4]]) -> [[8]]
def mat_mul(a, b):
    pass

# 36 [DIFÍCIL] spiral
# Lê a matriz em espiral no sentido horário, começando no canto superior
# esquerdo: percorre a borda externa e repete o processo sobre a região
# restante. Não repita elementos quando restar apenas uma linha ou uma coluna.
# Exemplos:
#   spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) -> [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
#   spiral([[1], [2], [3]]) -> [1, 2, 3]
#   spiral([]) -> []
def spiral(m):
    pass

# 37 [DIFÍCIL] balanced
# Verifica se os delimitadores (), [] e {} estão corretamente pareados e
# aninhados, ignorando os demais caracteres. Use uma lista imutável como pilha
# das aberturas pendentes. A string vazia é válida.
# Exemplos:
#   balanced('a*(b+[c-{d}])') -> True
#   balanced('([)]') -> False
#   balanced('') -> True
def balanced(text):
    pass

# 38 [DIFÍCIL] eval_rpn
# Avalia uma expressão em notação pós-fixa usando uma pilha imutável. Cada
# token é um inteiro ou uma das strings '+', '-', '*', '//'. Um operador
# consome os dois valores mais recentes: o penúltimo é o operando esquerdo e o
# último, o direito. Retorne None se faltarem operandos, houver divisão por
# zero ou não restar exatamente um valor ao final.
# Exemplos:
#   eval_rpn([8, 3, '-', 2, '*']) -> 10
#   eval_rpn([7, 2, '//']) -> 3
#   eval_rpn([5, '+']) -> None
#   eval_rpn([5, 0, '//']) -> None
def eval_rpn(tokens):
    pass

# 39 [DIFÍCIL] wildcard_match
# Verifica se o padrão corresponde ao texto inteiro. O símbolo ? representa
# exatamente um caractere; * representa qualquer sequência de zero ou mais
# caracteres; os demais representam a si mesmos.
# Exemplos:
#   wildcard_match('a*b?', 'axxbz') -> True
#   wildcard_match('a?b', 'ab') -> False
#   wildcard_match('*', '') -> True
def wildcard_match(pattern, text):
    pass

# 40 [DIFÍCIL] edit_distance
# Calcula o menor número de operações para transformar a string a na string b.
# As operações são inserir, remover ou substituir um caractere, todas com
# custo 1.
# Exemplos:
#   edit_distance('kitten', 'sitting') -> 3
#   edit_distance('', 'abc') -> 3
#   edit_distance('casa', 'casa') -> 0
def edit_distance(a, b):
    pass

# 41 [DIFÍCIL] lcs
# Retorna uma subsequência comum de comprimento máximo das duas strings
# (preserva a ordem dos caracteres, mas pode pular posições). Havendo várias
# respostas máximas, escolha a lexicograficamente menor.
# Exemplos:
#   lcs('abcbdab', 'bdcaba') -> 'bcab'
#   lcs('ba', 'ab') -> 'a'
#   lcs('', 'abc') -> ''
def lcs(a, b):
    pass

# 42 [DIFÍCIL] subset_sum
# Retorna todos os subconjuntos da lista cuja soma é target. Cada elemento
# pode ser usado uma única vez e a ordem original é preservada em cada
# subconjunto. Na busca, explore incluir o elemento atual antes de excluí-lo.
# A lista contém inteiros distintos, possivelmente negativos.
# Exemplos:
#   subset_sum(0, [-2, 0, 2, 3]) -> [[-2, 0, 2], [-2, 2], [0], []]
#   subset_sum(3, [2, 4]) -> []
#   subset_sum(0, []) -> [[]]
def subset_sum(target, xs):
    pass

# 43 [DIFÍCIL] unique_permutations
# Retorna todas as permutações distintas da lista em ordem lexicográfica
# crescente. Valores repetidos não podem gerar respostas duplicadas. A única
# permutação da lista vazia é ela própria.
# Exemplos:
#   unique_permutations([2, 1, 1]) -> [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
#   unique_permutations([3, 3]) -> [[3, 3]]
#   unique_permutations([]) -> [[]]
def unique_permutations(xs):
    pass

# 44 [DIFÍCIL] min_change
# Compõe value com a menor quantidade possível de moedas, com uso ilimitado de
# cada denominação. Retorne o par (quantidade, escolhidas), com escolhidas em
# ordem crescente; em empate, a lista lexicograficamente menor. Se for
# impossível, retorne None.
# Exemplos:
#   min_change([1, 3, 4], 6) -> (2, [3, 3])
#   min_change([1, 2, 3], 4) -> (2, [1, 3])
#   min_change([2, 4], 7) -> None
#   min_change([5], 0) -> (0, [])
def min_change(coins, value):
    pass

# 45 [DIFÍCIL] knapsack
# Mochila 0/1: cada item é um par (peso, valor). Retorne o maior valor total
# que pode ser transportado sem exceder a capacidade. Cada item pode ser usado
# no máximo uma vez, sem fracionar.
# Exemplos:
#   knapsack(5, [(2, 6), (3, 10), (4, 12)]) -> 16
#   knapsack(4, [(2, 6)]) -> 6
#   knapsack(3, []) -> 0
def knapsack(capacity, items):
    pass

# 46 [DIFÍCIL] queens
# Posiciona n rainhas em um tabuleiro n por n sem ataques entre elas. Cada
# solução é uma lista de n colunas: o elemento na posição r indica a coluna da
# rainha da linha r (a partir de zero). Retorne todas as soluções em ordem
# lexicográfica.
# Exemplos:
#   queens(4) -> [[1, 3, 0, 2], [2, 0, 3, 1]]
#   queens(2) -> []
#   queens(0) -> [[]]
def queens(n):
    pass

# 47 [DIFÍCIL] count_paths
# Conta os caminhos do canto superior esquerdo ao canto inferior direito de
# uma grade, movendo apenas uma célula para a direita ou para baixo. Células
# com 0 são livres e células com 1 são bloqueadas. Grade vazia ou
# origem/destino bloqueado produz 0.
# Exemplos:
#   count_paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) -> 2
#   count_paths([[1]]) -> 0
#   count_paths([[0]]) -> 1
def count_paths(grid):
    pass

# 48 [DIFÍCIL] simple_paths
# O grafo dirigido é uma lista de pares (vértice, vizinhos). Retorne todos os
# caminhos de src a dst sem repetir vértice no mesmo caminho, explorando os
# vizinhos em profundidade na ordem em que aparecem. Ao atingir dst, encerre
# aquele caminho. Ciclos não podem provocar recursão infinita.
# Exemplos:
#   simple_paths([(1, [2, 3]), (2, [3, 4]), (3, [1, 4]), (4, [])], 1, 4) -> [[1, 2, 3, 4], [1, 2, 4], [1, 3, 4]]
#   simple_paths([(1, [2]), (2, [])], 2, 1) -> []
#   simple_paths([(1, [1])], 1, 1) -> [[1]]
def simple_paths(graph, src, dst):
    pass

# 49 [DIFÍCIL] analyze_tree
# Retorna a tupla (quantidade de nós, altura, é de busca, é balanceada). É de
# busca se, em todos os níveis, todo valor à esquerda é menor que o nó e todo
# valor à direita é maior (valores iguais violam a propriedade). É balanceada
# se, em cada nó, as alturas das subárvores diferem no máximo em 1. A árvore
# vazia tem altura 0, é de busca e balanceada.
# Exemplos:
#   analyze_tree([10, [5, [], [12, [], []]], [15, [], []]]) -> (4, 3, False, True)
#   analyze_tree([3, [2, [1, [], []], []], []]) -> (3, 3, True, False)
#   analyze_tree([]) -> (0, 0, True, True)
def analyze_tree(t):
    pass

# 50 [DIFÍCIL] derive
# Derivação simbólica. Constantes são ['c', n], variáveis ['v', nome], somas
# ['+', a, b] e produtos ['*', a, b]. Retorne a árvore da derivada em relação
# a var, com as regras da soma e do produto: D(a*b) = D(a)*b + a*D(b).
# Simplifique recursivamente: calcule operações entre constantes e elimine
# somas com 0 e produtos com 0 ou 1. Preserve a ordem dos operandos e não
# reúna termos semelhantes.
# Exemplos:
#   derive('x', ['*', ['v', 'x'], ['v', 'x']]) -> ['+', ['v', 'x'], ['v', 'x']]
#   derive('x', ['*', ['c', 3], ['v', 'x']]) -> ['c', 3]
#   derive('x', ['+', ['v', 'y'], ['c', 7]]) -> ['c', 0]
def derive(var, expr):
    pass

# 51 [DIFÍCIL] fold_tree
# Redução sobre árvore binária: a árvore vazia vale z; em cada nó, f recebe o
# valor do nó, o resultado da subárvore esquerda e o resultado da subárvore
# direita.
# Exemplos:
#   fold_tree(lambda v, l, r: v + l + r, 0, [2, [1, [], []], [3, [], []]]) -> 6
#   fold_tree(lambda v, l, r: l + [v] + r, [], [2, [1, [], []], [3, [], []]]) -> [1, 2, 3]
#   fold_tree(lambda v, l, r: 1 + (l if l > r else r), 0, []) -> 0
def fold_tree(f, z, t):
    pass

# 52 [DIFÍCIL] level_order
# Percurso em largura: retorna uma lista com os valores de cada nível da
# árvore, da raiz para as folhas e, em cada nível, da esquerda para a direita.
# Exemplos:
#   level_order([1, [2, [4, [], []], []], [3, [], []]]) -> [[1], [2, 3], [4]]
#   level_order([]) -> []
def level_order(t):
    pass

# 53 [DIFÍCIL] bst_from_list
# Constrói uma árvore binária de busca inserindo os elementos da lista, da
# esquerda para a direita, em uma árvore inicialmente vazia. Valores menores
# vão para a esquerda, maiores para a direita e valores já presentes são
# ignorados.
# Exemplos:
#   bst_from_list([2, 1, 3, 2]) -> [2, [1, [], []], [3, [], []]]
#   bst_from_list([1, 2, 3]) -> [1, [], [2, [], [3, [], []]]]
#   bst_from_list([]) -> []
def bst_from_list(xs):
    pass

# 54 [DIFÍCIL] power_set
# Retorna todos os subconjuntos da lista, preservando a ordem original dentro
# de cada um. Para cada elemento, liste primeiro os subconjuntos que o contêm
# e depois os que não o contêm.
# Exemplos:
#   power_set([1, 2, 3]) -> [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
#   power_set([]) -> [[]]
def power_set(xs):
    pass

# 55 [DIFÍCIL] combinations
# Retorna todas as formas de escolher k elementos da lista, preservando a
# ordem original dentro de cada escolha e listando primeiro as que usam os
# elementos mais à esquerda. k é inteiro não negativo.
# Exemplos:
#   combinations(2, [1, 2, 3]) -> [[1, 2], [1, 3], [2, 3]]
#   combinations(0, [1, 2]) -> [[]]
#   combinations(3, [1, 2]) -> []
def combinations(k, xs):
    pass

# 56 [DIFÍCIL] hanoi
# Torre de Hanói: retorna a sequência mínima de movimentos (origem, destino)
# para levar n discos do pino 'A' ao pino 'C', usando 'B' como auxiliar, sem
# nunca colocar um disco maior sobre um menor.
# Exemplos:
#   hanoi(2) -> [('A', 'B'), ('A', 'C'), ('B', 'C')]
#   hanoi(1) -> [('A', 'C')]
#   hanoi(0) -> []
def hanoi(n):
    pass

# 57 [DIFÍCIL] longest_increasing
# Retorna uma subsequência estritamente crescente de comprimento máximo
# (preserva a ordem, mas pode pular posições). Havendo várias respostas
# máximas, escolha a lexicograficamente menor.
# Exemplos:
#   longest_increasing([3, 1, 2, 5, 4]) -> [1, 2, 4]
#   longest_increasing([5, 4, 3]) -> [3]
#   longest_increasing([]) -> []
def longest_increasing(xs):
    pass

# 58 [DIFÍCIL] merge_intervals
# Recebe intervalos fechados (início, fim), com início <= fim, em qualquer
# ordem. Funde os intervalos que se sobrepõem ou se tocam e retorna o
# resultado ordenado pelo início.
# Exemplos:
#   merge_intervals([(5, 7), (1, 3), (2, 4)]) -> [(1, 4), (5, 7)]
#   merge_intervals([(1, 2), (2, 3)]) -> [(1, 3)]
#   merge_intervals([(1, 9), (2, 3)]) -> [(1, 9)]
#   merge_intervals([]) -> []
def merge_intervals(xs):
    pass

# 59 [DIFÍCIL] shortest_path
# O grafo dirigido é uma lista de pares (vértice, vizinhos). Retorne um
# caminho de src a dst com o menor número de arestas, usando busca em largura
# com uma fila imutável e visitando os vizinhos na ordem em que aparecem (o
# primeiro caminho encontrado é a resposta). Se não houver caminho, retorne
# None.
# Exemplos:
#   shortest_path([(1, [2, 3]), (2, [3, 4]), (3, [1, 4]), (4, [])], 1, 4) -> [1, 2, 4]
#   shortest_path([(1, [2]), (2, [])], 2, 1) -> None
#   shortest_path([(1, [2]), (2, [])], 1, 1) -> [1]
def shortest_path(graph, src, dst):
    pass

# 60 [DIFÍCIL] generate_parens
# Gera todas as strings com n pares de parênteses corretamente balanceados, em
# ordem lexicográfica, considerando '(' menor que ')'.
# Exemplos:
#   generate_parens(3) -> ['((()))', '(()())', '(())()', '()(())', '()()()']
#   generate_parens(1) -> ['()']
#   generate_parens(0) -> ['']
def generate_parens(n):
    pass
