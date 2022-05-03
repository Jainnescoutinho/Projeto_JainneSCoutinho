import pandas as pd
import seaborn as sns; sns.set() #pacote de visualização
import matplotlib.pyplot as plt #pacote de visualização


def consulta_bc(codigo_bcb):
  url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  return df


divida_lq_MA = consulta_bc('15538')

#fatiando dados por ano.
dados_div = divida_lq_MA[divida_lq_MA.index.year >= 2008]
dados_div.plot(figsize = (16,8))
plt.title('Divida líquida do Estado do Maranhão em milhões.', size = 20)
plt.show()

print(dados_div.describe())