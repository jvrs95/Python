import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
  i = 1
  textos = []
  texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
  while texto:
    textos.append(texto)
    i += 1
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

  return (textos)

def separa_sentencas(texto):
  '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
  sentencas = re.split(r'[.!?]+', texto)
  if sentencas[-1] == '':
    del sentencas[-1]
  return sentencas

def separa_frases(sentenca):
  '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
  return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
  '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
  return frase.split()

def n_palavras_unicas(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
  freq = dict()
  unicas = 0
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
      if freq[p] == 1:
        unicas -= 1
        freq[p] += 1
    else:
      freq[p] = 1
      unicas += 1

  return unicas

def n_palavras_diferentes(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
  freq = dict()
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
      freq[p] += 1
    else:
      freq[p] = 1

  return len(freq)

def tamanho_medio_palavra(texto):      #PERFEITA
  número_de_caracteres = 0
  lista_palavras = list()
  lista_frases = list()
  lista_sentencas = separa_sentencas(texto)
  for sentenca in lista_sentencas:
    lista_frases = lista_frases + separa_frases(sentenca)
  for frase in lista_frases:
    lista_palavras = lista_palavras + separa_palavras(frase)
  for i in lista_palavras:
    número_de_caracteres = número_de_caracteres + len(i)
  número_de_palavras = len(lista_palavras)
  return(número_de_caracteres/número_de_palavras)

def test1_funcao_tamanho_medio_palavra():
  texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
  if tamanho_medio_palavra(texto) == 5.571428571428571:
    return(print("Sucesso!!! O resultado foi o esperado, ou seja: 5.571428571428571"))
  else:
    return(print("Teste Falhou!!! O resultado foi ", tamanho_medio_palavra(texto), "esperava-se 5.571428571428571"))

def test2_funcao_tamanho_medio_palavra():
  texto = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
  if tamanho_medio_palavra(texto) == 4.507936507936508:
    return(print("Sucesso!!! O resultado foi o esperado, ou seja: 4.507936507936508"))
  else:
    return(print("Teste Falhou!!! O resultado foi ", tamanho_medio_palavra(texto), "esperava-se 4.507"))

def test3_funcao_tamanho_medio_palavra():
  texto = '''Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.'''
  if tamanho_medio_palavra(texto) == 4.409448818897638:
    return(print("Sucesso!!! O resultado foi o esperado, ou seja: 4.409448818897638"))
  else:
    return(print("Teste Falhou!!! O resultado foi ", tamanho_medio_palavra(texto), "esperava-se 4.409"))

  
def type_token(texto):               #PERFEITA
  lista_palavras = list()
  lista_frases = list()
  lista_sentencas = separa_sentencas(texto)
  for sentenca in lista_sentencas:
    lista_frases = lista_frases + separa_frases(sentenca)
  for frase in lista_frases:
    lista_palavras = lista_palavras + separa_palavras(frase)
  número_palavras_diferentes = n_palavras_diferentes(lista_palavras)
  número_de_palavras = len(lista_palavras)
  return(número_palavras_diferentes/número_de_palavras)

def test_funcao_type_token():
  texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
  return(print(type_token(texto)))

def hapax_legomana(texto):               #PERFEITA
  lista_palavras = list()
  lista_frases = list()
  lista_sentencas = separa_sentencas(texto)
  for sentenca in lista_sentencas:
    lista_frases = lista_frases + separa_frases(sentenca)
  for frase in lista_frases:
    lista_palavras = lista_palavras + separa_palavras(frase)
  número_palavras_unicas = n_palavras_unicas(lista_palavras)
  número_de_palavras = len(lista_palavras)
  return(número_palavras_unicas/número_de_palavras)

def test_funcao_hapax_legomana():
  texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
  return(print(hapax_legomana(texto)))
  
def tamanho_medio_sentenca(texto):      #PERFEITA
  soma_caracteres_sentencas = 0
  lista_sentencas = separa_sentencas(texto)
  for sentenca in lista_sentencas:
    soma_caracteres_sentencas = soma_caracteres_sentencas + len(sentenca)    
  quantidade_sentencas = len(lista_sentencas)
  return(soma_caracteres_sentencas/quantidade_sentencas)
  

def test_funcao_tamanho_medio_sentenca():
  texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
  return(print(tamanho_medio_sentenca(texto)))


def complexidade_sentenca(texto):    #PERFEITA
  lista_frases = list()
  lista_sentencas = separa_sentencas(texto)
  for sentenca in lista_sentencas:
    lista_frases = lista_frases + separa_frases(sentenca)
  numero_total_sentencas = len(lista_sentencas)
  numero_total_frases = len(lista_frases)
  return(numero_total_frases/numero_total_sentencas)

def test_funcao_complexidade_sentenca():
  texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
  return(print(complexidade_sentenca(texto)))

def tamanho_medio_frase(texto):   #PERFEITA
  soma_caracteres_frases = 0
  lista_frases = list()
  lista_sentencas = separa_sentencas(texto)
  for sentenca in lista_sentencas:
    lista_frases = lista_frases + separa_frases(sentenca)
  for frases in lista_frases:
    soma_caracteres_frases = soma_caracteres_frases + len(frases)
  número_de_frases = len(lista_frases)
  return(soma_caracteres_frases/número_de_frases)

def test_funcao_tamanho_medio_frase():
  texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
  return(print(tamanho_medio_frase(texto)))

def as_a_e_as_b():
  lista_similaridades = list()
  as_b = le_assinatura()
  textos = le_textos()
  for i in textos:
    as_a = calcula_assinatura(i)
    lista_similaridades.append(compara_assinatura(as_a, as_b))
  ass_cp = lista_similaridades
  return((avalia_textos(textos, ass_cp)))

def calcula_assinatura(texto):               #PERFEITA
  as_a = list()
  as_a.append(tamanho_medio_palavra(texto))
  as_a.append(type_token(texto))
  as_a.append(hapax_legomana(texto))
  as_a.append(tamanho_medio_sentenca(texto))
  as_a.append(complexidade_sentenca(texto))
  as_a.append(tamanho_medio_frase(texto))
  
  return(as_a)
  '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
  pass

def test_calcula_assinatura():            #PERFEITA
  print("Iniciando os testes!!!!!")
  texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
  as_a = calcula_assinatura(texto)
  if as_a == [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]:
    return(print("Sucesso!!! O resultado foi o esperado, ou seja:", as_a))
  else:
    return(print("Teste Falhou!!! O resultado foi ", as_a, "esperava-se [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]"))

def compara_assinatura(as_a, as_b):
  '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
  soma = 0
  grau_de_similaridade = 0
  lista_compara_assinatura = list()
  for i in range(len(as_a)):
    if as_a[i] - as_b[i] > 0:
      lista_compara_assinatura.append(as_a[i] - as_b[i])
    else:
      lista_compara_assinatura.append(-(as_a[i] - as_b[i]))
  for i in lista_compara_assinatura:
    soma = soma + i
  grau_de_similaridade = (soma)/6
  return (grau_de_similaridade)
  pass

def avalia_textos(textos, ass_cp):
  autor = 0
  for i in range(len(textos)):
    if ass_cp[i] == min(ass_cp):
      autor = (i)
  print("O autor do texto", autor, "está infectado com COH-PIAH")
  return (autor)    
  '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
  pass

as_a_e_as_b()
