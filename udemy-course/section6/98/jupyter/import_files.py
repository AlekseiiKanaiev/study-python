#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../Study-python/udemy-course/section6/98/jupyter'))
	print(os.getcwd())
except:
	pass

#%%
import os
os.listdir('../')


#%%
import pandas


#%%
df1 = pandas.read_csv('../supermarkets.csv')


#%%
df1


#%%
df2 = pandas.read_json('../supermarkets.json')

df2


#%%
df3 = pandas.read_excel('../supermarkets.xlsx')
df3


