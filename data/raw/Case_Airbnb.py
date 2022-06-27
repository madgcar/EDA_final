# EDA Airbnb en la ciudad de New York

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

# Cargo los datos
Data_Airbnb = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv')
print(Data_Airbnb)

# Primero veo una muestra de los datos

Data_Airbnb.sample(10)

# Verifico la info para conocer cuantas y los tipos de variables
Data_Airbnb.info()

# Describo los datos y los tipos de datos
Data_Airbnb.describe()


