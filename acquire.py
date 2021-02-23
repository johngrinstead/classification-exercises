import pandas as pd
import numpy as np
import os

# visualize
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(11, 9))
plt.rc('font', size=13)

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

# acquire
from env import host, user, password
from pydataset import data


def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'



## Make a function named get_titanic_data that returns the titanic data 
# from the codeup data science database as a pandas data frame. 
# Obtain your data from the Codeup Data Science Database.



def get_titanic_data():
    # Create SQL query.
    sql_query = 'SELECT * FROM passengers'
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('titanic_db'))
    
    return df


## Make a function named get_iris_data that returns the data from the 
# iris_db on the codeup data science database as a pandas data frame. 
# The returned data frame should include the actual name of the species in
#  addition to the species_ids. 
# Obtain your data from the Codeup Data Science Database.

def get_iris_data():
    # Create SQL query.
    sql_query = '''
    SELECT species_id,
				measurement_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
                FROM measurements
                JOIN species
                USING(species_id);
    '''
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    
    return df



## Once you've got your get_titanic_data and get_iris_data functions 
# written, now it's time to add caching to them. To do this, 
# edit the beginning of the function to check for a local filename like 
# titanic.csv or iris.csv. If they exist, use the .csv file. 
# If the file doesn't exist, then produce the SQL and pandas necessary 
# to create a dataframe, then write the dataframe to a .csv file with the 
# appropriate name.


def get_titanic_data(cached=False):
    
    if cached == False or os.path.isfile('titanic_df.csv') == False:
    
    # Create SQL query.
        sql_query = 'SELECT * FROM passengers'
    
    # Read in DataFrame from Codeup db.
        df = pd.read_sql(sql_query, get_connection('titanic_db'))
    
        df.to_csv('titanic.csv')
    
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    return df



#########################################################################

def get_iris_data(cached=False):
    
    if cached == False or os.path.isfile('iris.csv') == False:
    
    # Create SQL query.
        sql_query = '''
        SELECT species_id,
				measurement_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
                FROM measurements
                JOIN species
                USING(species_id);
        '''
    
    # Read in DataFrame from Codeup db.
        df = pd.read_sql(sql_query, get_connection('iris_db'))
        
        df.to_csv('iris.csv')
        
    else:
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('iris.csv', index_col=0)
    
    return df





