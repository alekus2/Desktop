import pandas as pd
df= pd.DataFrame({})
name = str(input("Nome da coluna: "))  
vl = []  
for x in range(3):
        value = int(input("Adicione valores: "))  
        vl.append(value)  
df[name] = vl
print(df) 
df.to_excel('teste.xlsx')

