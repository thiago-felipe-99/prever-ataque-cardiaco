# Resolução do teste extra de Álgebra Linear II
Foi feito um script em python para para prever se uma pessoa irá morrer de ataque
cardíaco, o modelo utilizado foi um sistema linear simples e foi resolvido por 
meio de mínimos quadrados.

## Softwares necessários
Para execução do programa é necessário ter Python 3 instalado no computador e as
bibliotecas do Python 3 NumPy e Pandas, exemplo de instalação em um SO baseado
em Debian/Ubuntu:
```shell
sudo apt install python3 pip3
pip3 install numpy pandas
```

## Resolver as constates
Para saber quais são as constates do modelo basta executar:
```shell
python3 main.py
```
Para o cálculo da constates foi usado o método de mínimos quadrados. Para a 
execução do programa é necessário o arquivo `data.csv`, a descrição de como deve 
ser essa tabela está em `carac.pdf`. Ao final do  programa é criado o arquivo 
`constates.csv` que contém os valores das constates.  Os erro são calculados a 
partir do arquivo que é fornecido ao programa, dando uma noção se esse modelo é 
uma boa aproximação.

Exemplo de saída:
```shell
Modelo final:
C0.age + C1.anaemia + C2.creatinine_phosphokinase + C3.diabetes + C4.ejection_fraction
C5.high_blood_pressure + C6.platelets C7.serum_creatinine + C8.serum_sodium + C9.sex
C10.smoking + C11 = Y

se Y >= 0.5:
    Teve ataque cardíaco
se_não: 
    Não teve ataque cardíaco

Tabela Das Constantes
C0   1.55199896601623898995
C1   0.00832658705479653004
C2   0.04759134336328441767
C3   0.00005022874376334789
C4   0.01781739852703222160
C5  -0.01126067537709637620
C6   0.06843936271537995331
C7  -0.00000011079809384730
C8   0.11161827716997319015
C9  -0.01090466805219450497
C10 -0.05208892424252431486
C11  0.01839951775713843940

Tabela De Erros
 Falso Positivo  Falso Negativo  Erro Total
         25.86%          21.55%      22.41%
```

## Prever resultados
Depois de calculado as constates do modelo é possível prever se uma pessoa
morreu de ataque cardíaco com o script `prever.py`:
```shell
python3 prever.py
```
Para a execução desse script é necessário o arquivo `prever.csv`, a descrição
dele é igual do arquivo `data.csv`, e do arquivo `constates.csv` que foi gerado
a partir de `main.py`. No final da execução do programa é criado o arquivo
`resultado.csv` onde tem se a pessoa morreu ou não de ataque cardíaco.

## Exemplo de execução
![Imagem Mostrando Um Exemplo De Execução](/exemplo_execução.png)
