def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'



## Make a function named get_titanic_data that returns the titanic data 
# from the codeup data science database as a pandas data frame. 
# Obtain your data from the Codeup Data Science Database.



def get_titanic_data(cached=False):
    df_titanic = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

    