
import os 
from ftplib import FTP
from abc import ABC, abstractmethod
import pandas as pd
from dbc_reader import DbcReader
from datetime import datetime

class DatasusFtpBaseClass(ABC):

   FTP_SERVER = "ftp.datasus.gov.br"
   BASE_REMOTE_PATH = "dissemin/publicos/"
   DBC_FILES_PATH = os.path.join(os.getcwd(),"dbc_files")
   CUR_YEAR = datetime.now().year

   BRAZILIAN_STATES:list[str]  = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
   ]
   CHOOSEN_MONTH_NUM = 12 #Caso os dados estejam de forma mensais e não seja preciso agregar, vamos pegar o mês de dezembro (12) como o mês dos dados

   SPECIFIC_FOLDER_PATH: str  # cada subclasse terá seu próprios valores dessas constantes
   FIRST_2_LETTERS_OF_FILE: str


   #@abstractmethod
   #def extract_processed_collection():
      #pass

   @abstractmethod
   def extract_raw_data()->pd.DataFrame | list[pd.DataFrame]:
      pass

   def download_dbc_file(self,remaining_ftp_path:str,filename:str)->str:
      final_path:str = f"{self.BASE_REMOTE_PATH}/{remaining_ftp_path}/{filename}"
      ftp_username = 'anonymous'
      ftp_password = '' 
      local_filepath = os.path.join(self.DBC_FILES_PATH, filename)

      try:
         ftp = FTP(self.FTP_SERVER)
         ftp.login(user=ftp_username, passwd=ftp_password)
         ftp.cwd(final_path)
         with open(local_filepath, 'wb') as local_file:
            ftp.retrbinary(f"RETR {final_path}", local_file.write)
         ftp.quit()
         return local_filepath
      except Exception as e:
         print(f"falha ao baixar arquivo dbc do datasus, erro {e}")
         return ""

   def download_dbc_and_get_df(self,remaining_ftp_path:str,filename:str)->pd.DataFrame:
      file_path:str = self.download_dbc_file(remaining_ftp_path,filename)
      dbc_reader = DbcReader(file_path)
      df = pd.DataFrame([row for row in dbc_reader])
      return df
   
   def delete_all_dbc_files(self)->bool:
      file_list:list[str] = os.listdir(self.DBC_FILES_PATH)
      for file in file_list:
         if os.path.exists(file) and ".dbc" in file:
            os.remove(file)

   def get_available_time_series(self,list_years:list[int],file_code:str,file_path:str, data_is_monthly:bool = False)->list[int]:
      if not list_years:
         raise IOError("passou lista vazia como argumento")
      file_name = f"{file_code}"
      removed_years:int = 0
      for year in list_years:
         file_name:str = filename.format(year=year) #formata arquivo para ter o ano certo
         download_respose:str = self.download_dbc_file(file_path,file_name) #tenta baixa arquivo
         if not download_respose: #ano não existe na base 
            removed_years+=1
         else: #ano existe na base
            break
      
      oldest_year:int = list_years[-1]
      new_list_years:list[int] = list_years[removed_years:] #remove os anos não disponíveis na base da lista
      
      for i in range(removed_years):
         new_oldest_year:int = oldest_year +1
         file_name:str = filename.format(year=year) #formata arquivo para ter o ano certo
         download_respose:str = self.download_dbc_file(file_path,file_name) #tenta baixa arquivo
         if not download_respose: #não tem anos mais antigos na base
            break
         else:
            new_list_years.append(new_oldest_year)
            oldest_year +=1
      
      return new_list_years



   def get_time_series_monthly_data(self,specific_folder_path:str,first_2_letters_file:str, time_series_len:int = 15)->list[int]:
      list_year_identifiers:list[int] = [x for x in range(self.CUR_YEAR, self.CUR_YEAR-time_series_len,-1)] #gera 
      list_year_identifiers = self.get_available_time_series(list_year_identifiers,,specific_folder_path)
      
      list_file_names:list[str] = list(map()  )

   def get_time_series_years(self,specific_folder_path:str,first_2_letters_file:str, time_series_len:int = 15)->list[int]:
      pass


class DatasusNumMedicalBeds(DatasusFtpBaseClass):
   
   SPECIFIC_FOLDER_PATH: str = "LT" # cada subclasse terá seu próprios valores dessas constantes
   FIRST_2_LETTERS_OF_FILE: str = "CNES/200508_/Dados/LT"

   def extract_raw_data() -> pd.DataFrame | list[pd.DataFrame]:
      pass

if __name__ == "__main__":
   obj = DatasusNumMedicalBeds()
   obj.get_time_series_monthly_data("aaa","aa",7)