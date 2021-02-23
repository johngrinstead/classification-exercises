## 1. Use the function defined in acquire.py to load the iris data.

import acquire

df = get_iris_data(cached=False)

df.head()


## 2. Drop the species_id and measurement_id columns.

df.drop_duplicates(inplace=True)

cols_to_drop = ['species_id', 'measurement_id']
df = df.drop(columns=cols_to_drop)


## 3. Rename the species_name column to just species.

df = df.rename(columns={'species_name' : 'species'})


## 4. Create dummy variables of the species name.

dummies = pd.get_dummies(df[['species']])

df = pd.concat([df, dummies], axis=1)


## 5. Create a function named prep_iris that accepts the untransformed 
# iris data, and returns the data with the transformations above applied.

def clean_iris():
    df = acquire.get_iris_data()
    df.drop_duplicates(inplace=True)
    cols_to_drop = ['species_id', 'measurement_id']
    df = df.drop(columns=cols_to_drop)
    df = df.rename(columns={'species_name' : 'species'})
    dummies = pd.get_dummies(df[['species']])
    df = pd.concat([df, dummies], axis=1)
    return df


######################################################


def prep_iris():
    df = clean_iris()
    
    train_validate, test = train_test_split(iris, test_size=0.2, random_state=319)
    
    train, validate = train_test_split(train_validate, train_size=0.7, random_state=319)
    
    return train, validate, test

