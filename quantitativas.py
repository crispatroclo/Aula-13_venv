# usar arquivo funcionario
# criar uma variavel para cada serie quantitativa

import pandas as pd

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
print(df)
print('\n')

# quantitativas: salario, lucro

df_salario = df['salario'] # float64
print(df_salario)
print('\n')

df_lucro = df['lucro'] # float64
print(df_lucro)
print('\n')

df_quantitativas = df[['salario', 'lucro']]
print(df_quantitativas)