from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Criar os dois graficos com numero de colunas e suas posições
fig = make_subplots(rows=1, cols=2)

#Aqui é onde colocamos os valores para o primeiro grafico!
fig.add_trace(go.Bar(x=["janeiro", "fevereiro", "março"], y=[5, 6, 7]), row=1, col=1)

#Aqui é onde colocamos os valores para o segundo grafico de dispersão
fig.add_trace(go.Scatter(x=["janeiro", "fevereiro", "março"], y=[5, 6, 7]), row=1, col=2)

# Mostrar a figura (os dois graficos)
fig.show()
