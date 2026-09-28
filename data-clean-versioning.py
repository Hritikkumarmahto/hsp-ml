import pandas as pd
import boto3
from datetime import date


path="D:\MLops\Mlops_house_predication_raw_data.csv"

data=pd.read_csv(path)

df=pd.DataFrame(data)
df.shape
df.isnull()
df.isnull().sum()
print(f"Shape before:{df.shape}")
print()
# after cleaningd
df_cleaned=df.dropna()
print(df_cleaned.isnull().sum())
print(df_cleaned.shape) 
# saving the celaned file 

clean_path=r"D:\MLops\Mlops_house_predication_v1.csv"
df_cleaned.to_csv(clean_path,index=False)



# upload to s3

s3=boto3.client('s3')
BUCKET="mlops-hsp-b1"
def upload_processed_data(local_path):
  key=f"processed/{date.today()}/processed_cleadned_data_v1.csv"
  s3.upload_file(local_path,BUCKET,key)
  print(f"uploaded to s3://{BUCKET}/{key}")
  return key
upload_processed_data(clean_path)