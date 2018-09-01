import pandas as pd
import matplotlib.pyplot as plt
names = ['kamesh','chukka','vamsi','ravi','hari']
births = [10,20,30,40,50]
info = list(zip(names,births))
df = pd.DataFrame(data = info, columns = ['col1','col2'])
print(df)
df = to_csv('builtin.csv')
