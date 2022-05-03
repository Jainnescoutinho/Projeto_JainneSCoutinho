import pandas
dados = sidrapy.get_table(table_code="6472", territorial_level="3", ibge_territorial_code="all", period="all", variable="5929", header="n", format="pandas")
dados.head() #mostra as 5 primeiras linhas do dataframe
dados["V"] = dados["V"].astype(float)#mudando tipo de dados
dados["D1C"] = dados["D1C"].astype(int)#mudando tipo de dados
dados.rename(columns={'D1N': 'Estados'}, inplace = True)#mudando o nome da coluna de D1N para Estados
a=-1#para estrutura de repetição de cada linha
for i in dados["D2C"]{
  a=a+1
  ano = (int((i[:4])))}
  dados.loc[a, 'Ano'] = ano
  var = ["Ano", "D1C", "Estados"]
  dadosmen = dados.groupby(by=var)[["V"]].mean()
  sns.set(style="darkgrid")  # tema do gráfico
  plt.figure(figsize=(10, 5))  # tamanho do gráfico
  plt.xticks(rotation=0)  # rotação dos dados no eixo x
  sns.lineplot(x="Ano", y="V", hue="Estados", data=dadosmen.query("D1C == 21"))  # plotando o gráfico
  plt.title(
      "Rendimento médio nominal de todos os trabalhos, habitualmente recebido por mês,\npelas pessoas de 14 anos ou mais de idade, ocupadas na semana de referência, com rendimento de trabalho",
      fontsize=14)
  plt.xlabel("data")
  plt.ylabel("Valor em reais")

  dados.head()