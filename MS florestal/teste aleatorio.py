import pandas as pd
import numpy as np

col='Caderno ProvaMensal ProvaBimestral Simulado'.split()
lin='Ana Paula Joana Joao Gabriel'.split()
notas=np.random.randint(1,10,36).reshape(4,5)
dados= pd.DataFrame(data=notas, index=lin, columns=col)

print(dados)