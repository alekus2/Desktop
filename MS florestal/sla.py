import pandas as pd

# Exemplo de DataFrame para testes
df = pd.DataFrame({
    'CD_TALHAO': [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    'nm_parcela': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

# Simulação de mapeamento de novas parcelas
mapa_parcelas = {
    1: 1, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5,
    11: 6, 12: 6, 13: 7, 14: 7, 15: 8, 16: 8
}

# Adiciona uma nova coluna no DataFrame para armazenar as parcelas atualizadas
df['nm_parcela_atualizada'] = df['nm_parcela'].map(mapa_parcelas)

# Exibe o DataFrame após a modificação
print("DataFrame após as modificações:")
print(df)

# Salva o arquivo Excel com a atualização
output_file = "Parcelas_atualizado.xlsx"
df.to_excel(output_file, index=False)
print(f"Arquivo salvo com sucesso como: {output_file}")
