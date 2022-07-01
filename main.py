"""
Resolução do teste extra de álgebra linear II

O modelo usado foi um linear simples:
    AX = Y
    Onde A é uma matriz com os dados da morte e uma coluna com uns
    X são as constantes do modelo
    Y é um vetor prevendo se a pessoa morreu de ataque cardíaco, se esse número
    for maior ou igual a 0.5 ela fala que a pessoa irá morrer de ataque cardíaco

Para executar esse programa é necessário ter o arquivo data.csv, o modelo de
como ele deve ser é falado em carac.pdf.

No final da execução do programa ele irá mostrar o modelo completo, as suas
constantes e os seus erros. As constantes também serão salvos no arquivo
constantes.csv.

Aluno: Thiago Felipe Cruz E Souza
DRE: 119035356
"""
import numpy as np
import pandas as pd

#Carregando as informações da questão
data= pd.DataFrame(pd.read_csv('data.csv'))

#Definindo a matriz com os dados que podem ter causado a morte
colunas_matriz_x = [
    'age',
    'anaemia',
    'creatinine_phosphokinase',
    'diabetes',
    'ejection_fraction',
    'high_blood_pressure',
    'platelets',
    'serum_creatinine',
    'serum_sodium',
    'sex',
    'smoking'
]
matriz_x = np.insert(data[colunas_matriz_x].values, 0, 1, axis=1)

#Definido o vetor de eventos da morte
coluna_vetor_ỹ = ['DEATH_EVENT']
vetor_ỹ = data[coluna_vetor_ỹ].values

#Definindo a matriz e o vetor de mínimos quadrados
matriz_A = matriz_x.transpose() @ matriz_x
vetor_y = matriz_x.transpose() @ vetor_ỹ

#Calculando quais são as constantes do modelo por mínimos quadrados.
vetor_resultante = np.linalg.lstsq(matriz_A, vetor_y, rcond=None)[0]

#Prevendo quem morreria segundo o modelo
mortes_previstas = [ 1 if x >= 0.5 else 0 for x in matriz_x @ vetor_resultante ]

#Calculando o erro de falso positivo
qt_falso_positivos = [ [x,y] for (x, y) in zip(mortes_previstas, vetor_ỹ) if x == 1 ]
qt_falso_positivos = [ 0 if x == y else 1 for(x, y) in qt_falso_positivos ]
falso_positivo = np.sum(qt_falso_positivos)/len(qt_falso_positivos) * 100

#Calculando o erro de falso negativo
qt_falso_negativos = [ [x,y] for (x, y) in zip(mortes_previstas, vetor_ỹ) if x == 0 ]
qt_falso_negativos = [ 0 if x == y else 1 for(x, y) in qt_falso_negativos ]
falso_negativo = np.sum(qt_falso_negativos)/len(qt_falso_negativos) * 100

#Calculando o erro total do modelo
qt_erros = np.sum([ 0 if x == y else 1 for (x, y) in zip(mortes_previstas, vetor_ỹ) ])
erro_total = qt_erros/len(vetor_ỹ)*100

#Fazendo os resultados serem impressos no terminal e escrito no arquivo
#constantes.csv
tabela_de_constantes = pd.DataFrame({
    'C0': vetor_resultante[0],
    'C1': vetor_resultante[1],
    'C2': vetor_resultante[2],
    'C3': vetor_resultante[3],
    'C4': vetor_resultante[4],
    'C5': vetor_resultante[5],
    'C6': vetor_resultante[6],
    'C7': vetor_resultante[7],
    'C8': vetor_resultante[8],
    'C9': vetor_resultante[9],
    'C10': vetor_resultante[10],
    'C11': vetor_resultante[11]
})

tabela_de_erros = pd.DataFrame({
    'Falso Positivo': [ falso_positivo ],
    'Falso Negativo': [ falso_negativo ],
    'Erro Total': [ erro_total ]
})

print("Modelo final:")
print("""C0.age + C1.anaemia + C2.creatinine_phosphokinase + C3.diabetes + C4.ejection_fraction
C5.high_blood_pressure + C6.platelets C7.serum_creatinine + C8.serum_sodium + C9.sex
C10.smoking + C11 = Y

se Y >= 0.5:
    Teve ataque cardíaco
se_não:
    Não teve ataque cardíaco
""")

pd.set_option('display.float_format', '{:.20f}'.format)
print("Tabela Das Constantes")
print(tabela_de_constantes.T.to_string(header=False))
print()

pd.set_option('display.float_format', '{:05.2f}%'.format)
print("Tabela De Erros")
print(tabela_de_erros.to_string(index=False))

tabela_de_constantes.to_csv("constantes.csv", index=False, float_format="%.20f")
