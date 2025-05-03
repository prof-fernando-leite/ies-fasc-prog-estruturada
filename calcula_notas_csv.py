import csv

#ler csv
def ler_csv(path_do_arquivo):
    with open(path_do_arquivo, newline='') as arquivo:
        retorno = []
        reader = csv.reader(arquivo)
        next(reader)
        for linha in reader:
            retorno.append({
                'nome': linha[0],
                'notas': [float(nota) for nota in linha[1:]],
            })
        return retorno

#definir o status do aluno
def status_aluno(media) -> str:
    if media >= 7 :
        retorno = "aprovado"
    elif 7 > media >= 4:
        retorno= "recuperação"
    else:
        retorno = "reprovado"
    return retorno

#calcular média
def calcula_media_alunos(alunos_notas):
    retorno = []
    for aluno_notas in alunos_notas:
        aluno = aluno_notas['nome']
        notas = aluno_notas['notas']
        media = sum(notas) / len(notas)
        retorno.append({
            'nome': aluno,
            'media': media,
            'status': status_aluno(media),
        })
    return retorno

def insere_aluno(lista, aluno_interno):
    lista.append({'nome': aluno_interno['nome'], 'media': aluno_interno['media']})

#agrupar alunos conforme desempenho
def agrupa_alunos_por_status(alunos_notas_status):
    aprovados = []
    recuperacao = []
    reprovados = []
    for aluno_notas in alunos_notas_status:
        if aluno_notas['status'] == 'aprovado':
            insere_aluno(aprovados, aluno_notas)
        elif aluno_notas['status'] == 'reprovado':
            insere_aluno(reprovados, aluno_notas)
        else:
            insere_aluno(recuperacao, aluno_notas)
    return (aprovados, recuperacao, reprovados)

#escrever nos respectivos arquivos
def cria_arquivos_csv(nome_do_arquivo, headers, conteudo):
    with open(nome_do_arquivo, 'w', newline='') as arquivo:
        e = csv.writer(arquivo)
        e.writerow(headers)
        for conteudo in conteudo:
            index = len(headers)
            inicio = 0
            campos = []
            while index > inicio:
                campos.append(conteudo[headers[inicio]])
                inicio += 1
            e.writerow(campos)

#calcular a nota da recuperação
def calcula_nota_recuperacao(alunos_em_recuperacao):
    retorno = []
    for aluno_notas in alunos_em_recuperacao:
        nr = (18 - 2*aluno_notas['media'])
        retorno.append({
            'nome': aluno_notas['nome'],
            'media': aluno_notas['media'],
            'nota_minima': nr
        })
    return retorno

alunos = ler_csv('./material/notas.csv')
alunos_medias = calcula_media_alunos(alunos)
aprovados, recuperacao, reprovados =  agrupa_alunos_por_status(alunos_medias)
cria_arquivos_csv('./material/aprovados.csv', ['nome', 'media'], aprovados)
cria_arquivos_csv('./material/reprovados.csv', ['nome', 'media'], reprovados)
cria_arquivos_csv('./material/recuperacao.csv', ['nome', 'media', 'nota_minima'], calcula_nota_recuperacao(recuperacao))
