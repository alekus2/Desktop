def contagem(talhoes, arquivo_original):
    df = pd.read_csv(arquivo_original)

    # Iterate through the talhões
    for talhao_dict in talhoes:
        talhao = talhao_dict['CD_TALHAO']
        nm_parcela = talhao_dict['nm_parcela']

        # Apply custom logic to update 'nm_parcela'
        if nm_parcela < 3:
            parcela_nova = nm_parcela  # For parcels less than 3, keep the same
        elif nm_parcela % 2 == 0:
            parcela_nova = nm_parcela // 2  # For even parcelas, divide by 2
        else:
            parcela_nova = (nm_parcela + 1) // 2  # For odd parcelas, round up and divide by 2

        # Update the DataFrame for the current talhão
        df.loc[df['CD_TALHAO'] == talhao, 'nm_parcela'] = parcela_nova
    
    # Save the modified DataFrame as an Excel file
    nome_arquivo = os.path.splitext(arquivo_original)[0]
    novo_arquivo = f"{nome_arquivo}_atualizado.xlsx"
    df.to_excel(novo_arquivo, index=False) 
    print(f"Arquivo salvo como: {novo_arquivo}")
    return novo_arquivo
