import pandas as pd
import seaborn as sns; sns.set()  #  pacote de visualização
import matplotlib.pyplot as plt  #  pacote de visualização


def consulta_bc(codigo_bcb):
  url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_bcb}/dados?formato=json'
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  return df


# 1. Criar uma função de plot, o que vai permitir flexibilidade
# 2. Vincular o gráfico a uma interpretação
# 2a. Outras informaçoes relacionadas à dívida. Transferências do gov. federal
# 2b. Gastos com pessoal.
# 3. Unidade de medida R$ (format axisy


def plot():
  divida_lq_MA = consulta_bc('15538')

  # fig, ax = plt.subplots()
  #fatiando dados por ano.
  dados_div = divida_lq_MA[divida_lq_MA.index.year >= 2008]
  dados_div.plot(figsize = (16,8))

  plt.title('Divida líquida do Estado do Maranhão em milhões.', size = 20)
  plt.savefig('minha_figura.png')
  plt.show()


if __name__ == '__main__':
    # Várias séries
    c1 = '15538'
    d = consulta_bc(c1)
    print(d.describe())
    plot()
