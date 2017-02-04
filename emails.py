import csv
import pandas as pd

columns = ['Email', 'Address']
df = pd.DataFrame(columns=columns) 

def addEmail(email, address):
    df = df.append([email, address])
    print df
    
addEmail("hello", "sdas")