-- Lista de exercícios - Paradigma funcional em Haskell
-- 60 questões: 10 fáceis, 20 médias e 30 difíceis.
-- A mesma lista, em Python, está em main.py.
--
-- Regras:
--  1. Iteração apenas por recursão. List comprehension e intervalos como
--     [1..n] podem ser usados quando oportuno (por exemplo, questões 26 e 27).
--  2. Acesso a listas pelas primitivas head, tail, init e last do Prelude
--     (o casamento de padrões x:xs equivale a head/tail). Para pares, use
--     fst e snd.
--  3. Sem funções prontas do Prelude ou de Data.List (length, sum, maximum,
--     map, filter, foldr, zip, elem, reverse, ...). Funções já resolvidas
--     nesta lista podem ser reutilizadas nas questões seguintes.
--  4. O operador ++ só pode ser usado se um dos operandos tiver no máximo
--     1 elemento. Para o caso geral, use myAppend (questão 03).
--
-- Convenções:
--  - As assinaturas estão comentadas para que o arquivo compile antes de as
--    funções serem implementadas. Remova o comentário ao resolver a questão.
--  - Argumentos: primeiro a função (ou o parâmetro), por último a lista.
--  - Ausência de resultado é Nothing (tipo Maybe).
--  - Grafo: lista de pares (vértice, lista de vizinhos).
--  - Os tipos abaixo são usados nas questões 38 e 49 a 53.

data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show, Eq)

data Expr = Const Int | Var String | Add Expr Expr | Mul Expr Expr deriving (Show, Eq)

data Token = Val Int | Op String deriving (Show, Eq)

-- ============================================================================
-- PARTE 1 - FÁCEIS (01 a 10)
-- ============================================================================

-- 01 [FÁCIL] myLength
-- Retorna a quantidade de elementos de uma lista.
-- Exemplos:
--   myLength [4, 5, 6] -> 3
--   myLength [] -> 0
-- myLength :: [a] -> Int

-- 02 [FÁCIL] myElem
-- Verifica se o elemento x pertence à lista.
-- Exemplos:
--   myElem 3 [1, 2, 3] -> True
--   myElem 'z' "abc" -> False
-- myElem :: Eq a => a -> [a] -> Bool

-- 03 [FÁCIL] myAppend
-- Concatena duas listas, com o mesmo comportamento do operador de
-- concatenação. O operador só pode ser usado se um dos operandos tiver no
-- máximo 1 elemento.
-- Exemplos:
--   myAppend [1, 2] [3, 4] -> [1, 2, 3, 4]
--   myAppend [] [7] -> [7]
-- myAppend :: [a] -> [a] -> [a]

-- 04 [FÁCIL] myReverse
-- Inverte o conteúdo de uma lista.
-- Exemplos:
--   myReverse [1, 2, 3] -> [3, 2, 1]
--   myReverse "abcd" -> "dcba"
-- myReverse :: [a] -> [a]

-- 05 [FÁCIL] myMap
-- Aplica a função f a cada elemento da lista, preservando a ordem.
-- Exemplos:
--   myMap (\x -> x * x) [1, 2, 3] -> [1, 4, 9]
--   myMap (\x -> x + 1) [] -> []
-- myMap :: (a -> b) -> [a] -> [b]

-- 06 [FÁCIL] myFilter
-- Retorna apenas os elementos da lista que satisfazem o predicado p,
-- preservando a ordem.
-- Exemplos:
--   myFilter (\x -> x `mod` 2 == 0) [1, 2, 3, 4] -> [2, 4]
--   myFilter (\x -> x > 9) [1, 2] -> []
-- myFilter :: (a -> Bool) -> [a] -> [a]

-- 07 [FÁCIL] countIf
-- Conta quantos elementos da lista satisfazem o predicado p.
-- Exemplos:
--   countIf (\x -> x < 0) [3, -1, 0, -7] -> 2
--   countIf (\x -> x > 2) [] -> 0
-- countIf :: (a -> Bool) -> [a] -> Int

-- 08 [FÁCIL] myMaximum
-- Retorna o maior elemento de uma lista não vazia.
-- Exemplos:
--   myMaximum [3, 9, 2] -> 9
--   myMaximum [-5] -> -5
-- myMaximum :: Ord a => [a] -> a

-- 09 [FÁCIL] myTake
-- Retorna os n primeiros elementos da lista. Se a lista tiver menos de n
-- elementos, retorna a lista inteira. n é inteiro não negativo.
-- Exemplos:
--   myTake 2 [7, 8, 9] -> [7, 8]
--   myTake 5 [1, 2] -> [1, 2]
--   myTake 0 [1, 2] -> []
-- myTake :: Int -> [a] -> [a]

-- 10 [FÁCIL] isPalindrome
-- Verifica se uma sequência é palíndroma, isto é, igual à sua inversa. A
-- sequência vazia é palíndroma.
-- Exemplos:
--   isPalindrome "arara" -> True
--   isPalindrome [1, 2, 3] -> False
--   isPalindrome "" -> True
-- isPalindrome :: Eq a => [a] -> Bool

-- ============================================================================
-- PARTE 2 - MÉDIAS (11 a 30)
-- ============================================================================

-- 11 [MÉDIO] myFoldr
-- Redução à direita: combina os elementos da direita para a esquerda, partindo
-- do valor inicial z. Para [x1, x2, x3] o resultado é f(x1, f(x2, f(x3, z))).
-- Exemplos:
--   myFoldr (\x acc -> x - acc) 0 [1, 2, 3] -> 2
--   myFoldr (\x acc -> acc ++ [x]) [] [1, 2, 3] -> [3, 2, 1]
--   myFoldr (\x acc -> x + acc) 7 [] -> 7
-- myFoldr :: (a -> b -> b) -> b -> [a] -> b

-- 12 [MÉDIO] myFoldl
-- Redução à esquerda: combina os elementos da esquerda para a direita,
-- partindo do valor inicial z. Para [x1, x2, x3] o resultado é f(f(f(z, x1),
-- x2), x3).
-- Exemplos:
--   myFoldl (\acc x -> acc - x) 0 [1, 2, 3] -> -6
--   myFoldl (\acc x -> acc * 10 + x) 0 [1, 2, 3] -> 123
-- myFoldl :: (b -> a -> b) -> b -> [a] -> b

-- 13 [MÉDIO] myZipWith
-- Combina as duas listas elemento a elemento usando f. O resultado tem o
-- tamanho da menor lista.
-- Exemplos:
--   myZipWith (\x y -> x + y) [1, 2, 3] [10, 20] -> [11, 22]
--   myZipWith (\x y -> (x, y)) [1, 2] "ab" -> [(1, 'a'), (2, 'b')]
-- myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]

-- 14 [MÉDIO] mySpan
-- Retorna o par (prefixo, resto), em que prefixo é o maior prefixo da lista
-- cujos elementos satisfazem p, e resto é o restante da lista.
-- Exemplos:
--   mySpan (\x -> x < 3) [1, 2, 3, 1] -> ([1, 2], [3, 1])
--   mySpan (\x -> x > 5) [1, 9] -> ([], [1, 9])
-- mySpan :: (a -> Bool) -> [a] -> ([a], [a])

-- 15 [MÉDIO] partition
-- Retorna o par (aceitos, rejeitados): aceitos contém os elementos que
-- satisfazem p e rejeitados os demais. Preserve a ordem relativa dentro de
-- cada grupo.
-- Exemplos:
--   partition (\x -> x `mod` 2 == 0) [-3, 4, 0, 5, 2] -> ([4, 0, 2], [-3, 5])
--   partition (\x -> x > 0) [] -> ([], [])
-- partition :: (a -> Bool) -> [a] -> ([a], [a])

-- 16 [MÉDIO] composeAll
-- Aplica ao valor x todas as funções da lista, da esquerda para a direita: a
-- primeira recebe x, a segunda recebe o resultado da primeira, e assim por
-- diante. A lista vazia representa a identidade.
-- Exemplos:
--   composeAll [\x -> x + 2, \x -> x * x, \x -> x - 1] 3 -> 24
--   composeAll [] 9 -> 9
-- composeAll :: [a -> a] -> a -> a

-- 17 [MÉDIO] removeDuplicates
-- Remove os elementos repetidos, mantendo apenas a primeira ocorrência de cada
-- valor, na ordem original.
-- Exemplos:
--   removeDuplicates [3, 1, 3, 2, 1] -> [3, 1, 2]
--   removeDuplicates [] -> []
-- removeDuplicates :: Eq a => [a] -> [a]

-- 18 [MÉDIO] insertionSortBy
-- Ordena a lista por inserção. A função le a b devolve True quando a pode vir
-- antes de b. A ordenação deve ser estável: elementos equivalentes mantêm a
-- ordem original.
-- Exemplos:
--   insertionSortBy (\a b -> a <= b) [3, 1, 2] -> [1, 2, 3]
--   insertionSortBy (\a b -> a >= b) [3, 1, 2] -> [3, 2, 1]
--   insertionSortBy (\a b -> fst a <= fst b) [(2, 'a'), (1, 'b'), (2, 'c')] -> [(1, 'b'), (2, 'a'), (2, 'c')]
-- insertionSortBy :: (a -> a -> Bool) -> [a] -> [a]

-- 19 [MÉDIO] compress
-- Elimina duplicatas consecutivas de uma lista, mantendo um representante de
-- cada bloco.
-- Exemplos:
--   compress [1, 1, 2, 1, 1, 3] -> [1, 2, 1, 3]
--   compress [] -> []
-- compress :: Eq a => [a] -> [a]

-- 20 [MÉDIO] pack
-- Empacota os elementos duplicados consecutivos em sublistas.
-- Exemplos:
--   pack [1, 1, 2, 3, 3, 3, 1] -> [[1, 1], [2], [3, 3, 3], [1]]
--   pack [] -> []
-- pack :: Eq a => [a] -> [[a]]

-- 21 [MÉDIO] encode
-- Compressão por tamanho de sequência: cada bloco de elementos duplicados
-- consecutivos é codificado como o par (n, e), em que n é o número de
-- repetições do elemento e.
-- Exemplos:
--   encode "aaaabccaadeeee" -> [(4, 'a'), (1, 'b'), (2, 'c'), (2, 'a'), (1, 'd'), (4, 'e')]
--   encode [] -> []
-- encode :: Eq a => [a] -> [(Int, a)]

-- 22 [MÉDIO] decode
-- Inversa de encode: dada uma lista de pares (n, e), reconstrói a lista
-- original. As quantidades são inteiros positivos.
-- Exemplos:
--   decode [(2, 7), (1, 5), (3, 7)] -> [7, 7, 5, 7, 7, 7]
--   decode [] -> []
-- decode :: [(Int, a)] -> [a]

-- 23 [MÉDIO] splitToken
-- Divide a lista em sublistas usando o valor t como marcador. O marcador não
-- aparece no resultado. Se t ocorre k vezes, o resultado tem k + 1 sublistas
-- (algumas podem ser vazias).
-- Exemplos:
--   splitToken 2 [1, 2, 3, 4, 2, 5, 67, 8, 9, 0, 3] -> [[1], [3, 4], [5, 67, 8, 9, 0, 3]]
--   splitToken 0 [0, 1, 0, 0, 2] -> [[], [1], [], [2]]
--   splitToken 0 [] -> [[]]
-- splitToken :: Eq a => a -> [a] -> [[a]]

-- 24 [MÉDIO] joinToken
-- Inversa de split_token/splitToken: concatena as sublistas usando o valor t
-- como separador entre elas.
-- Exemplos:
--   joinToken 0 [[1], [2, 3], [4]] -> [1, 0, 2, 3, 0, 4]
--   joinToken 0 [[], [1]] -> [0, 1]
--   joinToken 0 [] -> []
-- joinToken :: a -> [[a]] -> [a]

-- 25 [MÉDIO] primeFactors
-- Fatora um inteiro n >= 1 em uma lista de pares (fator, frequência), com os
-- fatores primos em ordem crescente.
-- Exemplos:
--   primeFactors 8 -> [(2, 3)]
--   primeFactors 42 -> [(2, 1), (3, 1), (7, 1)]
--   primeFactors 1 -> []
-- primeFactors :: Int -> [(Int, Int)]

-- 26 [MÉDIO] pyths
-- Uma tripla (x, y, z) de inteiros positivos é pitagórica se x*x + y*y == z*z.
-- Usando list comprehension, retorne todas as triplas pitagóricas com
-- componentes no intervalo [1..n], variando x, depois y, depois z.
-- Exemplos:
--   pyths 5 -> [(3, 4, 5), (4, 3, 5)]
--   pyths 10 -> [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
-- pyths :: Int -> [(Int, Int, Int)]

-- 27 [MÉDIO] perfects
-- Um inteiro positivo é perfeito se é igual à soma de seus divisores,
-- excluindo ele próprio. Usando list comprehension, retorne todos os números
-- perfeitos de 1 até n.
-- Exemplos:
--   perfects 500 -> [6, 28, 496]
--   perfects 5 -> []
-- perfects :: Int -> [Int]

-- 28 [MÉDIO] rotate
-- Retorna a lista após k rotações de uma posição para a esquerda. Se k for
-- negativo, rotaciona para a direita. Deslocamentos maiores que o tamanho da
-- lista equivalem ao deslocamento reduzido.
-- Exemplos:
--   rotate 7 [1, 2, 3, 4, 5] -> [3, 4, 5, 1, 2]
--   rotate (-1) [1, 2, 3, 4] -> [4, 1, 2, 3]
--   rotate 10 [] -> []
-- rotate :: Int -> [a] -> [a]

-- 29 [MÉDIO] windows
-- Retorna todas as sublistas contíguas de tamanho k (k > 0), avançando uma
-- posição por vez, na ordem de seus inícios. Se a lista tiver menos de k
-- elementos, retorna a lista vazia.
-- Exemplos:
--   windows 3 [4, 1, 7, 3] -> [[4, 1, 7], [1, 7, 3]]
--   windows 1 [8, 5] -> [[8], [5]]
--   windows 3 [1, 2] -> []
-- windows :: Int -> [a] -> [[a]]

-- 30 [MÉDIO] histogram
-- Produz uma lista de pares (valor, frequência total). Cada valor aparece uma
-- única vez, na ordem de sua primeira ocorrência, contando inclusive
-- ocorrências não consecutivas.
-- Exemplos:
--   histogram [3, 1, 3, 2, 1, 3] -> [(3, 3), (1, 2), (2, 1)]
--   histogram [] -> []
-- histogram :: Eq a => [a] -> [(a, Int)]

-- ============================================================================
-- PARTE 3 - DIFÍCEIS (31 a 60)
-- ============================================================================

-- 31 [DIFÍCIL] mergeSortBy
-- Ordena a lista com merge sort: divisão ao meio, ordenação recursiva das
-- partes e intercalação. A função le a b devolve True quando a pode vir antes
-- de b. A ordenação deve ser estável.
-- Exemplos:
--   mergeSortBy (\a b -> fst a <= fst b) [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')] -> [(1, 'b'), (1, 'd'), (2, 'a'), (2, 'c')]
--   mergeSortBy (\a b -> a >= b) [1, 3, 2] -> [3, 2, 1]
--   mergeSortBy (\a b -> a <= b) [] -> []
-- mergeSortBy :: (a -> a -> Bool) -> [a] -> [a]

-- 32 [DIFÍCIL] quickSelect
-- Retorna Just o elemento que ocuparia o índice k (a partir de zero) se a
-- lista fosse ordenada em ordem crescente, sem ordenar a lista inteira:
-- particione por pivô em menores, iguais e maiores e prossiga apenas na região
-- necessária. Se k não for índice válido, retorne Nothing.
-- Exemplos:
--   quickSelect 2 [7, 2, 5, 2, 9] -> Just 5
--   quickSelect 1 [7, 2, 5, 2, 9] -> Just 2
--   quickSelect (-1) [4, 1] -> Nothing
-- quickSelect :: Ord a => Int -> [a] -> Maybe a

-- 33 [DIFÍCIL] convolve
-- Cada lista representa os coeficientes de um polinômio, do termo constante
-- para o de maior grau. Calcule os coeficientes do produto. Para entradas não
-- vazias de tamanhos m e n, retorne m + n - 1 coeficientes, preservando zeros
-- finais. Se alguma entrada for vazia, retorne a lista vazia.
-- Exemplos:
--   convolve [1, 2, 3] [4, -1] -> [4, 7, 10, -3]
--   convolve [0, 1] [0, 1] -> [0, 0, 1]
--   convolve [] [1, 2] -> []
-- convolve :: [Int] -> [Int] -> [Int]

-- 34 [DIFÍCIL] rotateMatrix
-- Gira a matriz em 90 graus no sentido horário. Uma matriz com m linhas e n
-- colunas gera n linhas e m colunas. Construa também uma função auxiliar de
-- transposição recursiva (transpose). A entrada é vazia ou uma matriz
-- retangular com pelo menos uma linha e uma coluna.
-- Exemplos:
--   rotateMatrix [[1, 2, 3], [4, 5, 6]] -> [[4, 1], [5, 2], [6, 3]]
--   rotateMatrix [[1], [2], [3]] -> [[3, 2, 1]]
--   rotateMatrix [] -> []
-- rotateMatrix :: [[a]] -> [[a]]

-- 35 [DIFÍCIL] matMul
-- Produto matricial: cada elemento da saída é o produto escalar de uma linha
-- de a por uma coluna de b. As matrizes são retangulares, não vazias e de
-- dimensões compatíveis.
-- Exemplos:
--   matMul [[1, 2, 3], [4, 5, 6]] [[1, 0], [0, 1], [1, 1]] -> [[4, 5], [10, 11]]
--   matMul [[0, 2]] [[3], [4]] -> [[8]]
-- matMul :: [[Int]] -> [[Int]] -> [[Int]]

-- 36 [DIFÍCIL] spiral
-- Lê a matriz em espiral no sentido horário, começando no canto superior
-- esquerdo: percorre a borda externa e repete o processo sobre a região
-- restante. Não repita elementos quando restar apenas uma linha ou uma coluna.
-- Exemplos:
--   spiral [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] -> [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
--   spiral [[1], [2], [3]] -> [1, 2, 3]
--   spiral [] -> []
-- spiral :: [[a]] -> [a]

-- 37 [DIFÍCIL] balanced
-- Verifica se os delimitadores (), [] e {} estão corretamente pareados e
-- aninhados, ignorando os demais caracteres. Use uma lista imutável como pilha
-- das aberturas pendentes. A string vazia é válida.
-- Exemplos:
--   balanced "a*(b+[c-{d}])" -> True
--   balanced "([)]" -> False
--   balanced "" -> True
-- balanced :: String -> Bool

-- 38 [DIFÍCIL] evalRPN
-- Avalia uma expressão em notação pós-fixa usando uma pilha imutável. Cada
-- token é Val n ou Op s, com s entre "+", "-", "*", "//" (divisão inteira,
-- div). Um operador consome os dois valores mais recentes: o penúltimo é o
-- operando esquerdo e o último, o direito. Retorne Nothing se faltarem
-- operandos, houver divisão por zero ou não restar exatamente um valor ao
-- final.
-- Exemplos:
--   evalRPN [Val 8, Val 3, Op "-", Val 2, Op "*"] -> Just 10
--   evalRPN [Val 7, Val 2, Op "//"] -> Just 3
--   evalRPN [Val 5, Op "+"] -> Nothing
--   evalRPN [Val 5, Val 0, Op "//"] -> Nothing
-- evalRPN :: [Token] -> Maybe Int

-- 39 [DIFÍCIL] wildcardMatch
-- Verifica se o padrão corresponde ao texto inteiro. O símbolo ? representa
-- exatamente um caractere; * representa qualquer sequência de zero ou mais
-- caracteres; os demais representam a si mesmos.
-- Exemplos:
--   wildcardMatch "a*b?" "axxbz" -> True
--   wildcardMatch "a?b" "ab" -> False
--   wildcardMatch "*" "" -> True
-- wildcardMatch :: String -> String -> Bool

-- 40 [DIFÍCIL] editDistance
-- Calcula o menor número de operações para transformar a string a na string b.
-- As operações são inserir, remover ou substituir um caractere, todas com
-- custo 1.
-- Exemplos:
--   editDistance "kitten" "sitting" -> 3
--   editDistance "" "abc" -> 3
--   editDistance "casa" "casa" -> 0
-- editDistance :: String -> String -> Int

-- 41 [DIFÍCIL] lcs
-- Retorna uma subsequência comum de comprimento máximo das duas strings
-- (preserva a ordem dos caracteres, mas pode pular posições). Havendo várias
-- respostas máximas, escolha a lexicograficamente menor.
-- Exemplos:
--   lcs "abcbdab" "bdcaba" -> "bcab"
--   lcs "ba" "ab" -> "a"
--   lcs "" "abc" -> ""
-- lcs :: String -> String -> String

-- 42 [DIFÍCIL] subsetSum
-- Retorna todos os subconjuntos da lista cuja soma é target. Cada elemento
-- pode ser usado uma única vez e a ordem original é preservada em cada
-- subconjunto. Na busca, explore incluir o elemento atual antes de excluí-lo.
-- A lista contém inteiros distintos, possivelmente negativos.
-- Exemplos:
--   subsetSum 0 [-2, 0, 2, 3] -> [[-2, 0, 2], [-2, 2], [0], []]
--   subsetSum 3 [2, 4] -> []
--   subsetSum 0 [] -> [[]]
-- subsetSum :: Int -> [Int] -> [[Int]]

-- 43 [DIFÍCIL] uniquePermutations
-- Retorna todas as permutações distintas da lista em ordem lexicográfica
-- crescente. Valores repetidos não podem gerar respostas duplicadas. A única
-- permutação da lista vazia é ela própria.
-- Exemplos:
--   uniquePermutations [2, 1, 1] -> [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
--   uniquePermutations [3, 3] -> [[3, 3]]
--   uniquePermutations [] -> [[]]
-- uniquePermutations :: Ord a => [a] -> [[a]]

-- 44 [DIFÍCIL] minChange
-- Compõe value com a menor quantidade possível de moedas, com uso ilimitado de
-- cada denominação. Retorne Just (quantidade, escolhidas), com escolhidas em
-- ordem crescente; em empate, a lista lexicograficamente menor. Se for
-- impossível, retorne Nothing.
-- Exemplos:
--   minChange [1, 3, 4] 6 -> Just (2, [3, 3])
--   minChange [1, 2, 3] 4 -> Just (2, [1, 3])
--   minChange [2, 4] 7 -> Nothing
--   minChange [5] 0 -> Just (0, [])
-- minChange :: [Int] -> Int -> Maybe (Int, [Int])

-- 45 [DIFÍCIL] knapsack
-- Mochila 0/1: cada item é um par (peso, valor). Retorne o maior valor total
-- que pode ser transportado sem exceder a capacidade. Cada item pode ser usado
-- no máximo uma vez, sem fracionar.
-- Exemplos:
--   knapsack 5 [(2, 6), (3, 10), (4, 12)] -> 16
--   knapsack 4 [(2, 6)] -> 6
--   knapsack 3 [] -> 0
-- knapsack :: Int -> [(Int, Int)] -> Int

-- 46 [DIFÍCIL] queens
-- Posiciona n rainhas em um tabuleiro n por n sem ataques entre elas. Cada
-- solução é uma lista de n colunas: o elemento na posição r indica a coluna da
-- rainha da linha r (a partir de zero). Retorne todas as soluções em ordem
-- lexicográfica.
-- Exemplos:
--   queens 4 -> [[1, 3, 0, 2], [2, 0, 3, 1]]
--   queens 2 -> []
--   queens 0 -> [[]]
-- queens :: Int -> [[Int]]

-- 47 [DIFÍCIL] countPaths
-- Conta os caminhos do canto superior esquerdo ao canto inferior direito de
-- uma grade, movendo apenas uma célula para a direita ou para baixo. Células
-- com 0 são livres e células com 1 são bloqueadas. Grade vazia ou
-- origem/destino bloqueado produz 0.
-- Exemplos:
--   countPaths [[0, 0, 0], [0, 1, 0], [0, 0, 0]] -> 2
--   countPaths [[1]] -> 0
--   countPaths [[0]] -> 1
-- countPaths :: [[Int]] -> Int

-- 48 [DIFÍCIL] simplePaths
-- O grafo dirigido é uma lista de pares (vértice, vizinhos). Retorne todos os
-- caminhos de src a dst sem repetir vértice no mesmo caminho, explorando os
-- vizinhos em profundidade na ordem em que aparecem. Ao atingir dst, encerre
-- aquele caminho. Ciclos não podem provocar recursão infinita.
-- Exemplos:
--   simplePaths [(1, [2, 3]), (2, [3, 4]), (3, [1, 4]), (4, [])] 1 4 -> [[1, 2, 3, 4], [1, 2, 4], [1, 3, 4]]
--   simplePaths [(1, [2]), (2, [])] 2 1 -> []
--   simplePaths [(1, [1])] 1 1 -> [[1]]
-- simplePaths :: [(Int, [Int])] -> Int -> Int -> [[Int]]

-- 49 [DIFÍCIL] analyzeTree
-- Retorna a tupla (quantidade de nós, altura, é de busca, é balanceada). É de
-- busca se, em todos os níveis, todo valor à esquerda é menor que o nó e todo
-- valor à direita é maior (valores iguais violam a propriedade). É balanceada
-- se, em cada nó, as alturas das subárvores diferem no máximo em 1. A árvore
-- vazia tem altura 0, é de busca e balanceada.
-- Exemplos:
--   analyzeTree (Node 10 (Node 5 Empty (Node 12 Empty Empty)) (Node 15 Empty Empty)) -> (4, 3, False, True)
--   analyzeTree (Node 3 (Node 2 (Node 1 Empty Empty) Empty) Empty) -> (3, 3, True, False)
--   analyzeTree Empty -> (0, 0, True, True)
-- analyzeTree :: Tree Int -> (Int, Int, Bool, Bool)

-- 50 [DIFÍCIL] derive
-- Derivação simbólica sobre o tipo Expr. Retorne a árvore da derivada em
-- relação a var, com as regras da soma e do produto: D(a*b) = D(a)*b + a*D(b).
-- Simplifique recursivamente: calcule operações entre constantes e elimine
-- somas com 0 e produtos com 0 ou 1. Preserve a ordem dos operandos e não
-- reúna termos semelhantes.
-- Exemplos:
--   derive "x" (Mul (Var "x") (Var "x")) -> Add (Var "x") (Var "x")
--   derive "x" (Mul (Const 3) (Var "x")) -> Const 3
--   derive "x" (Add (Var "y") (Const 7)) -> Const 0
-- derive :: String -> Expr -> Expr

-- 51 [DIFÍCIL] foldTree
-- Redução sobre árvore binária: Empty vale z; em cada nó, f recebe o valor do
-- nó, o resultado da subárvore esquerda e o resultado da subárvore direita.
-- Exemplos:
--   foldTree (\v l r -> v + l + r) 0 (Node 2 (Node 1 Empty Empty) (Node 3 Empty Empty)) -> 6
--   foldTree (\v l r -> l ++ [v] ++ r) [] (Node 2 (Node 1 Empty Empty) (Node 3 Empty Empty)) -> [1, 2, 3]
--   foldTree (\v l r -> 1 + max l r) 0 Empty -> 0
-- foldTree :: (a -> b -> b -> b) -> b -> Tree a -> b

-- 52 [DIFÍCIL] levelOrder
-- Percurso em largura: retorna uma lista com os valores de cada nível da
-- árvore, da raiz para as folhas e, em cada nível, da esquerda para a direita.
-- Exemplos:
--   levelOrder (Node 1 (Node 2 (Node 4 Empty Empty) Empty) (Node 3 Empty Empty)) -> [[1], [2, 3], [4]]
--   levelOrder Empty -> []
-- levelOrder :: Tree a -> [[a]]

-- 53 [DIFÍCIL] bstFromList
-- Constrói uma árvore binária de busca inserindo os elementos da lista, da
-- esquerda para a direita, em uma árvore inicialmente vazia. Valores menores
-- vão para a esquerda, maiores para a direita e valores já presentes são
-- ignorados.
-- Exemplos:
--   bstFromList [2, 1, 3, 2] -> Node 2 (Node 1 Empty Empty) (Node 3 Empty Empty)
--   bstFromList [1, 2, 3] -> Node 1 Empty (Node 2 Empty (Node 3 Empty Empty))
--   bstFromList [] -> Empty
-- bstFromList :: Ord a => [a] -> Tree a

-- 54 [DIFÍCIL] powerSet
-- Retorna todos os subconjuntos da lista, preservando a ordem original dentro
-- de cada um. Para cada elemento, liste primeiro os subconjuntos que o contêm
-- e depois os que não o contêm.
-- Exemplos:
--   powerSet [1, 2, 3] -> [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
--   powerSet [] -> [[]]
-- powerSet :: [a] -> [[a]]

-- 55 [DIFÍCIL] combinations
-- Retorna todas as formas de escolher k elementos da lista, preservando a
-- ordem original dentro de cada escolha e listando primeiro as que usam os
-- elementos mais à esquerda. k é inteiro não negativo.
-- Exemplos:
--   combinations 2 [1, 2, 3] -> [[1, 2], [1, 3], [2, 3]]
--   combinations 0 [1, 2] -> [[]]
--   combinations 3 [1, 2] -> []
-- combinations :: Int -> [a] -> [[a]]

-- 56 [DIFÍCIL] hanoi
-- Torre de Hanói: retorna a sequência mínima de movimentos (origem, destino)
-- para levar n discos do pino 'A' ao pino 'C', usando 'B' como auxiliar, sem
-- nunca colocar um disco maior sobre um menor.
-- Exemplos:
--   hanoi 2 -> [('A', 'B'), ('A', 'C'), ('B', 'C')]
--   hanoi 1 -> [('A', 'C')]
--   hanoi 0 -> []
-- hanoi :: Int -> [(Char, Char)]

-- 57 [DIFÍCIL] longestIncreasing
-- Retorna uma subsequência estritamente crescente de comprimento máximo
-- (preserva a ordem, mas pode pular posições). Havendo várias respostas
-- máximas, escolha a lexicograficamente menor.
-- Exemplos:
--   longestIncreasing [3, 1, 2, 5, 4] -> [1, 2, 4]
--   longestIncreasing [5, 4, 3] -> [3]
--   longestIncreasing [] -> []
-- longestIncreasing :: [Int] -> [Int]

-- 58 [DIFÍCIL] mergeIntervals
-- Recebe intervalos fechados (início, fim), com início <= fim, em qualquer
-- ordem. Funde os intervalos que se sobrepõem ou se tocam e retorna o
-- resultado ordenado pelo início.
-- Exemplos:
--   mergeIntervals [(5, 7), (1, 3), (2, 4)] -> [(1, 4), (5, 7)]
--   mergeIntervals [(1, 2), (2, 3)] -> [(1, 3)]
--   mergeIntervals [(1, 9), (2, 3)] -> [(1, 9)]
--   mergeIntervals [] -> []
-- mergeIntervals :: [(Int, Int)] -> [(Int, Int)]

-- 59 [DIFÍCIL] shortestPath
-- O grafo dirigido é uma lista de pares (vértice, vizinhos). Retorne Just um
-- caminho de src a dst com o menor número de arestas, usando busca em largura
-- com uma fila imutável e visitando os vizinhos na ordem em que aparecem (o
-- primeiro caminho encontrado é a resposta). Se não houver caminho, retorne
-- Nothing.
-- Exemplos:
--   shortestPath [(1, [2, 3]), (2, [3, 4]), (3, [1, 4]), (4, [])] 1 4 -> Just [1, 2, 4]
--   shortestPath [(1, [2]), (2, [])] 2 1 -> Nothing
--   shortestPath [(1, [2]), (2, [])] 1 1 -> Just [1]
-- shortestPath :: [(Int, [Int])] -> Int -> Int -> Maybe [Int]

-- 60 [DIFÍCIL] generateParens
-- Gera todas as strings com n pares de parênteses corretamente balanceados, em
-- ordem lexicográfica, considerando '(' menor que ')'.
-- Exemplos:
--   generateParens 3 -> ["((()))", "(()())", "(())()", "()(())", "()()()"]
--   generateParens 1 -> ["()"]
--   generateParens 0 -> [""]
-- generateParens :: Int -> [String]
