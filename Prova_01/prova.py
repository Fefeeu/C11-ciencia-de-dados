# %%
import numpy as np

df = np.loadtxt('shopping_trends.csv',
                delimiter=',',
                dtype=str,
                encoding='utf-8')

#%%======================== EXERCICIO 1 ========================
media_idade = df[np.char.find(df[:,2], 'Male') >= 0][:,1].astype(int).mean()
print(f'A idade média dos homens é {media_idade:.3} anos.')

#%%======================== EXERCICIO 2 ========================
media_gasto = df[1:,5].astype(float).mean()
gastos_acima_media = df[1:,5][df[1:,5].astype(float) > media_gasto]
gastos_acima_media = len(gastos_acima_media)

print(f'\n{gastos_acima_media} pessoas gastaram a cima da média')

#%%======================== EXERCICIO 3 ========================
vendas = np.unique(df[1:,3], return_counts=True)
porcentagem_menos_vendido = (vendas[1].min() / (len(df) - 1)) * 100
print(f'\nO item menos vendido represeta {porcentagem_menos_vendido:.3}% das vendas')

#%%======================== EXERCICIO 4 ========================
porcentagem_desconto = (np.unique(df[:,13], return_counts=True)[1][2] * 100) / (len(df) - 1) 
print(f'\n{porcentagem_desconto}% das compras tiveram algum tipo de desconto')

#%%======================== EXERCICIO 5 ========================
cores_mais_vendida = np.unique(df[np.char.find(df[:,9], 'Summer') >= 0][:,8], return_counts=True)
cor_mais_vendida = cores_mais_vendida[0][cores_mais_vendida[1].argmax()]
print('\nA cor mais vendida nesse verão foi:', cor_mais_vendida)
# %%
