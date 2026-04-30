import pandas as pd 

# 1. Carregar o arquivo que baixei
df = pd.read_csv('data/raw/Pantheon+SH0ES.dat', sep=r'\s+', engine='python', comment='#')

# 2.  Filtros cosmologicos padrão

# Hubble flow local
mask = (df['zCMB'] > 0.01) & (df['zCMB'] < 0.15)

# Qualidade: ajuste de curva de luz
mask &= (df['FITPROB'] > 0.001)

# Filtro de cor
mask &= (df['c'] > -0.3) & (df['c'] < 0.5)

# 3. Máscara para criar a tabela filtrada
df_clean = df[mask].copy()

# 4.o caminho onde o arquivo será salvo
caminho_saida = 'notebooks/pantheon_filtrado.csv'

# 5.  Salvar a tabela
df_clean.to_csv(caminho_saida, index=False)

print(f"Sucesso! A tabela com {len(df_clean)} linhas foi salva em: {caminho_saida}")

print(df_clean.head())