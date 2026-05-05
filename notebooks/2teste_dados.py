from astroquery.sdss import SDSS
from astropy.coordinates import SkyCoord
import astropy.units as u 
from astropy.table import Table 
import pandas as pd

def get_sdss_spec(ra, dec, radius=3.0):

#buscando espectros no banco de dados do SDSS com base em coordenadas.
#1. converter RA e DEC em um objeto de coordenadas 
    coord = SkyCoord(ra=ra, dec=dec, unit=(u.deg, u.deg))

#2. faz a consulta na região. 'spectro=True' garante que só queremos
#objetos que possuam dados espectroscópicos.
    result = SDSS.query_region(coord, radius=radius*u.arcsec, spectro=True)

#3. se encontrar alguma coisa, retornar a primeira correspondência
    if result is not None:
        return result[0]
    return None

#4. Para conferir se está indo certo
print('Lendo catálogo MPA-JHU... ')
mpa = Table.read('DR17_MPA_JHU.fits', format= 'fits')

#5. Converte para o formato Panda
mpa_df = mpa.to_pandas()


#6.Verificando se deu certo
# ... (seu código anterior até o mpa_df.head())

# 7. Filtrando com os nomes exatos que apareceram no seu terminal
colunas_para_salvar = [
    'PLATEID', 
    'MJD', 
    'FIBERID', 
    'H_ALPHA_FLUX', 
    'H_BETA_FLUX', 
    'OIII_FLUX', 
    'NII_6584_FLUX' 
]

# Nota: Verifique se 'H_ALPHA_FLUX', 'H_BETA_FLUX' e 'NII_6584_FLUX' 
# também estão no catálogo, pois eles não apareceram no print resumido.

try:
    # Criando o DataFrame filtrado
    mpa_filtrado_df = mpa_df[colunas_para_salvar]
    
    # 8. Salvando em CSV
    caminho_csv = 'mpa_jhu_filtrado.csv'
    mpa_filtrado_df.to_csv(caminho_csv, index=False)

    print(f"Sucesso! Tabela salva em: {caminho_csv}")
    print(mpa_filtrado_df.head())

except KeyError as e:
    print(f"Erro: Coluna não encontrada: {e}")
    print("As colunas disponíveis são:")
    print(mpa_df.columns.tolist()) # Isso vai listar tudo para você conferir


print(mpa_filtrado_df.head())