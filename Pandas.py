#instal pandas in python
python --version #CMD-IDE-GIT-VSCODE
pip install pandas
import pandas as pd
data ={
    "Nama":["Haris","Alex","Indah"],
    "Usia" :[25,20,21],
    "Kota" :["Jakarta","Bandung","Bogor"],
    "Profit" :[3000000,7000000,9000000]
}
df=pd.DataFrame('/conten/sample_data.cvs.json.excel.API)
print(df)
#SERIES
Usia_series =df["Usia"]
print(Usia_series)
#INDEX
df =pd.DataFrame(data, index=["Orang1", "Orang2", "Orang3"])
print(df)
#READ CSV-EXCEL-JSON (BACA DATASET)
df = pd.read_csv('/content/sample_data/data.csv') #CONTOH DATA
print(df)
#SHAPE PEMGEMBALIAN DATASET
print(df.shape)
print(df.head())
