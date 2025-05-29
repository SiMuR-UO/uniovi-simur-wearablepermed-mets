import pandas as pd

url = "http://156.35.152.38:8080/PMP1003/PMP1003_RegistroActividades.xlsx"

df = pd.read_excel(url)

print(df)