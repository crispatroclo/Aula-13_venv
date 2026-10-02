# usar arquivo funcionario
# criar uma variavel para cada serie qualitativa

import pandas as pd

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
print(df)
print('\n')

# quantitativas: id, nome, departamento, ativo, data de nascimento

df_id = df['id'] # int64
print(df_id)
print('\n')

df_nome = df['nome'] # str
print(df_nome)
print('\n')

df_departamento = df['departamento'] # str
print(df_departamento)
print('\n')

df_ativo = df['ativo'] # bool
print(df_ativo)
print('\n')

df_nascimento = df['data de nascimento'] # str
print(df_nascimento)
print('\n')

df_qualitativas = df[['id', 'nome', 'departamento', 'ativo', 'data de nascimento']]
print(df_qualitativas)
