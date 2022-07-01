"""
prever.py preve se uma pessoa irá morrer de ataque cardíaco, para esse script
funcionar precisa dos arquivos prever.csv e constantes.csv.

O arquivo prever.csv é descrito em carac.pdf.

Para saber qual modelo é usado e gerar o arquivo constantes.csv veja o arquivo
main.py

Aluno: Thiago Felipe Cruz E Souza
DRE: 119035356
"""
import numpy as np
import pandas as pd

#Carregando as informações da questão
data= pd.DataFrame(pd.read_csv('prever.csv'))
constantes = pd.DataFrame(pd.read_csv("constantes.csv"))

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
constantes = constantes.values.T

#Calculando resultado
resultado = pd.DataFrame([ 1 if y >= 0.5 else 0 for y in matriz_x @ constantes ])
resultado.to_csv("resultado.csv", index=False, header=['DEATH_EVENT'])
print("Resultado salvo em resultado.csv")
