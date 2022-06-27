
import pandas as pd 
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()

# your code here
# cada vez que se extraiga la info el data set quedara cargado y limpio para los departamentos
Data = os.environ.get('url')


# Cargo los datos
Data_Airbnb = pd.read_csv(Data)
print(Data_Airbnb)

# Limpio las variables
# Cambio el tipo de dato de 'last_review' porque es un dato de tiempo

Data_Airbnb['last_review'] = Data_Airbnb['last_review'].astype('datetime64')
Data_Airbnb['neighbourhood_group']= pd.Categorical(Data_Airbnb['neighbourhood_group'])
Data_Airbnb['neighbourhood']= pd.Categorical(Data_Airbnb['neighbourhood'])
Data_Airbnb['name']= pd.Categorical(Data_Airbnb['name'])
Data_Airbnb['room_type']= pd.Categorical(Data_Airbnb['room_type'])

# Veo los datos

Data_Airbnb.info()

# Guardo la BD para que pueda ser trabajada por los equipos


Data_Airbnb.to_csv("Analisis_exploratorio_work.csv")


