import pandas as pd
import boto3 
from io import StringIO
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import root_mean_squared_error, root_mean_squared_error,r2_score

s3=boto3.client('s3')
BUCKET="mlops-hsp-b1"
KEY="processed/2026-09-25/processed_cleadned_data_v1.csv"

def fetch_data():
  obj=s3.get_object(Bucket=BUCKET,Key=KEY)
  df=pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))
  return df 

df=fetch_data()
print(f"fetch shape: {df.shape}")


X=df[['soft','bedrooms','bathrooms','age_years','garage','location_score']]
y=df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

mlflow.set_experiments("mlops-house-prediction")

