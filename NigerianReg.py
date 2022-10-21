import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os 
import netCDF4 as nc
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.colors as mcolors

myData = pd.read_csv("./Data/NigeriaRegressionData.csv") 
print(myData)



#df = myData[['price', 'import', 'prod', 'prev_year_prod', 'year', 'year2']]

lm = smf.ols('price ~ imports + prev_year_imports + prod + prev_year_prod + year + year2 + prev_local_prod', data=myData).fit().summary()
#lm = smf.ols('price ~ + prev_year_imports + year + prev', data=myData).fit().summary()


print(lm)


