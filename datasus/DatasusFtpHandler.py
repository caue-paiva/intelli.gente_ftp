
import os
from ftplib import FTP
from abc import ABC, abstractmethod
import pandas as pd
from dbc_reader import DbcReader

class DatasusFtpBaseClass(ABC):

   FTP_SERVER = "ftp.datasus.gov.br"
   BASE_REMOTE_PATH = "dissemin/publicos/"
   DBC_FILES_PATH = os.path.join(os.getcwd(),"dbc_files")

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
   

class DatasusNumMedicalBeds(DatasusFtpBaseClass):
   
   SPECIFIC_FOLDER_PATH: str =  # cada subclasse terá seu próprios valores dessas constantes
   FIRST_2_LETTERS_OF_FILE: str =

   def extract_raw_data() -> pd.DataFrame | list[pd.DataFrame]:
      pass