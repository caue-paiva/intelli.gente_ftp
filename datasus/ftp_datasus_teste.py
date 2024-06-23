from ftplib import FTP
import os
import pandas as pd
from dbc_reader import DbcReader


# FTP connection details
ftp_server = 'ftp.datasus.gov.br'
ftp_username = 'anonymous'
ftp_password = ''  # No password for anonymous access
remote_path = 'dissemin/publicos/SINASC/1996_/Dados/DNRES'
remote_filename = 'DNAL2019.dbc'  # Replace with your .dbc file name
local_path = '/path/to/save'  # Replace with the local path to save the file
local_filename = os.path.join(os.getcwd(), remote_filename)


def download_file():
    # Connect to FTP and download the file
    ftp = FTP(ftp_server)
    ftp.login(user=ftp_username, passwd=ftp_password)
    ftp.cwd(remote_path)
    with open(local_filename, 'wb') as local_file:
        ftp.retrbinary(f"RETR {remote_filename}", local_file.write)
    ftp.quit()


def aggr_all_births(df:pd.DataFrame)->pd.Series:
    grouped = df.groupby("CODMUNNASC")
    return grouped.size()

def aggr_underweight_births(df:pd.DataFrame)->pd.Series:
    CEILING_OF_UNDERWEIGHT_RANGE:int = 2499 
    new_df = df.copy()
    new_df = new_df[ df["PESO"] != '']
    new_df["PESO"] = new_df["PESO"].astype("int")
    new_df = new_df[new_df["PESO"] <= CEILING_OF_UNDERWEIGHT_RANGE] #filta os nascidos de até 2499 gramas

    grouped = new_df.groupby("CODMUNNASC")
    return grouped.size()

def aggr_low_prenatal_births(df:pd.DataFrame)->pd.Series:
    CEILING_OF_LOW_PRENATAL_RANGE:int = 6
    new_df = df.copy()
    new_df =  new_df[new_df["CONSULTAS"] != ''] 
    new_df["CONSULTAS"] = new_df["CONSULTAS"].astype("int")
    new_df = new_df[ new_df["CONSULTAS"] <= CEILING_OF_LOW_PRENATAL_RANGE ] #filta os nascidos que tiveram no máximo 6 pre-natais

    grouped = new_df.groupby("CODMUNNASC")
    return grouped.size()

def get_only_medics(df:pd.DataFrame)->pd.DataFrame:
    profession_code_column: pd.Series = df["CBOUNICO"].copy()

    medic_professions_codes:list[int] = list((pd.read_csv("DatasusMedicProfessionCodes.csv")["codigo"]).astype("string"))
    print((medic_professions_codes))
    #print(type(medic_professions_codes[0]))
    medics_rows: pd.Series = profession_code_column.apply(lambda x: x in medic_professions_codes)
    return df[medics_rows]

def get_only_medics2(df:pd.DataFrame)->pd.DataFrame:
    return df[df["CONSELHO"] == "71"]

def grouby_count_city(df:pd.DataFrame)->pd.Series:
    grouped = df.groupby("CODUFMUN")
    """for name, group in grouped:
        if name == "270010":
            print(f"Group: {name}")
            print(pd.Series(group['NOMEPROF'].values).value_counts())
            print(len(group['NOMEPROF'].values))"""
    return grouped.size()

dbc_reader = DbcReader(remote_filename)
df = pd.DataFrame([row for row in dbc_reader])

Series1 = Series2 = Series3 = pd.Series
Series1 = aggr_all_births(df)
Series2 = aggr_underweight_births(df)
Series2 = Series2.reindex(Series1.index,fill_value=0)
Series3 = aggr_low_prenatal_births(df)

print(Series2.value_counts())

print(Series1)
print(Series2)
print(Series3)


#print(df.info())
#print(df["CODMUNNASC"].value_counts())
#print(df["CBO"].value_counts())
#print(df.info())



"""
print(df.info())
print(df["CONSELHO"].value_counts())
medics_only_df = get_only_medics2(df)

#print(medics_only_df["CODUFMUN"].value_counts())
 
#print(medics_only_df.info())

print(grouby_count_city(medics_only_df))
"""
