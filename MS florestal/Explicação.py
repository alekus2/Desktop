import pandas as pd
import numpy as np

table=pd.DataFrame()

lista='arroz feijao batata beterraba'.split()
table["Alimentos"]=lista

print (table)