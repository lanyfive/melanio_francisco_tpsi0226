
def calculo_medias(notas):
    media = dict()

    for aluno, lista_nota in notas.items():
        media[aluno] = sum(lista_nota) / len(lista_nota)

    return media


notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

medias = calculo_medias(notas)

for aluno, media in medias.items():
    print(f"{aluno}: {media:.1f}")
