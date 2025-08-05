import pandas as pd
import re

# Carregar os dados
df = pd.read_csv("respostas.csv")

# Nome da coluna que precisa ser uniformizada
coluna_instituicao = "Se você estuda, onde você estuda? (ex: ufpb, unipe, ufpe, uepb...)"

# Função para uniformizar as instituições
def uniformizar_instituicao(valor):
    import unicodedata
    if pd.isna(valor) or valor == "":
        return valor
    # Converter para string e remover espaços extras
    valor_limpo = str(valor).strip()
    # Converter para maiúsculas
    valor_maiusculo = valor_limpo.upper()
    # Remover acentos
    valor_sem_acento = ''.join(
        c for c in unicodedata.normalize('NFKD', valor_maiusculo)
        if not unicodedata.combining(c)
    )
    # Remover espaços extras entre palavras
    valor_sem_espaco = re.sub(r'\s+', ' ', valor_sem_acento).strip()
    # Remover ponto final isolado ao final
    valor_final = re.sub(r'\.$', '', valor_sem_espaco)
    return valor_final

# Aplicar a uniformização
df[coluna_instituicao] = df[coluna_instituicao].apply(uniformizar_instituicao)

# Mostrar os valores únicos antes e depois da uniformização
print("=== VALORES ÚNICOS APÓS UNIFORMIZAÇÃO ===")
valores_unicos = df[coluna_instituicao].dropna().unique()
for valor in sorted(valores_unicos):
    print(f"'{valor}'")

print(f"\nTotal de valores únicos: {len(valores_unicos)}")

# Salvar o arquivo uniformizado
df.to_csv("respostas_uniformizadas.csv", index=False)
print("\nArquivo 'respostas_uniformizadas.csv' salvo com sucesso!")

# Mostrar algumas estatísticas
print(f"\n=== ESTATÍSTICAS ===")
print(f"Total de registros: {len(df)}")
print(f"Registros com instituição preenchida: {df[coluna_instituicao].notna().sum()}")
print(f"Registros sem instituição: {df[coluna_instituicao].isna().sum()}") 