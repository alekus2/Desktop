import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel (r"G:\aleks\Atividades-SENAC-AGOST\MS florestal\exemplo excel.xlsx")
plt.pie(x['Número'],labels=x['Nome'],autopct=None)
plt.show()