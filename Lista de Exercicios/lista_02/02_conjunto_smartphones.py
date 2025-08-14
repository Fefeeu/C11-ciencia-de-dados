# %%
loja_a = {'iPhone 15', 'Samsung Galaxy S23', 'Xiaomi 13T', 'Motorola Edge 40'}
loja_b = {'iPhone 15', 'Samsung Galaxy S23', 'Google Pixel 8', 'Asus ROG Phone 7'}


uniao_lojas = loja_a.union(loja_b)
print(uniao_lojas)

# %%
intercecao_loja = loja_a.intersection(loja_b)
print(intercecao_loja)