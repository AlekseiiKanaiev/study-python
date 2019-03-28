#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../Study-python/udemy-course/section6/jupyter'))
	print(os.getcwd())
except:
	pass

#%%
import pandas


#%%
df1 = pandas.DataFrame([[2,3,4], [10,12,14]])


#%%
print(df1)


#%%



