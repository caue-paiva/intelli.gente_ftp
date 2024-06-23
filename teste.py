# The raw data as a string
data = """
06115 2231-04 Médico anestesista
06117 2231-06 Médico cardiologista
06119 2231-17 Médico dermatologista
06122 2231-18 Médico do trabalho
06125 2231-25 Médico endocrinologista
06127 2231-20 Médico endoscopista
06128 2231-26 Médico fisiatra
06132 2231-32 Médico ginecologista
06135 2231-34 Médico hemoterapeuta
06137 2231-37 Médico legista
06138 2231-39 Médico nefrologista
06140 2231-56 Médico sanitarista
06142 2231-42 Médico neurologista
06145 2231-32 Médico obstetra *
06147 2231-44 Médico oftalmologista
06148 2231-35 Médico homeopata
06150 2231-46 Médico ortopedista
06152 2231-47 Médico otorrinolaringologista
06155 2231-49 Médico pediatra
06157 2231-51 Médico pneumotisiologista
06160 2231-52 Médico proctologista
06162 2231-53 Médico psiquiatra
06165 2231-24 Médico radiologista
06167 2231-54 Médico radioterapeuta
"""

# Split the data into lines
lines = data.strip().split("\n")

# Initialize a list to store the results
ocupacao_list = ["Codigo_CBO,Nome_da_Profissao"]

# Iterate over the lines and filter by "Ocupação"
for line in lines:
    parts = line.rsplit(" ", 1)
    if parts[-1] == "Ocupação":
        code_and_name = parts[0]
        ocupacao_list.append(code_and_name)

# Print the results

def parse_to_csv(in_str:str)->str:
    return in_str.replace("-","").replace(" ",",",1)

ocupacao_list = list(
      map(lambda x: x.replace("-","").replace(" ",",",1) ,
      ocupacao_list)
)
ocupacao_list.append("225124,Médico residente")

with open("teste.csv","w") as f:
   for item in ocupacao_list:
      f.write(item+"\n")