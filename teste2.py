import pandas as pd

# List of bold professions and their codes
data = [
    {"Codigo_CBO": "223101", "Nome_da_Profissao": "Médico acupunturista"},
    {"Codigo_CBO": "223102", "Nome_da_Profissao": "Médico alergista e imunologista"},
    {"Codigo_CBO": "223104", "Nome_da_Profissao": "Médico anatomopatologista"},
    {"Codigo_CBO": "223105", "Nome_da_Profissao": "Médico anestesiologista"},
    {"Codigo_CBO": "223107", "Nome_da_Profissao": "Médico angiologista"},
    {"Codigo_CBO": "223106", "Nome_da_Profissao": "Médico cardiologista"},
    {"Codigo_CBO": "223108", "Nome_da_Profissao": "Médico cirurgião cardiovascular"},
    {"Codigo_CBO": "223110", "Nome_da_Profissao": "Médico cirurgião de cabeça e pescoço"},
    {"Codigo_CBO": "223111", "Nome_da_Profissao": "Médico cirurgião do aparelho digestivo"},
    {"Codigo_CBO": "223112", "Nome_da_Profissao": "Médico cirurgião geral"},
    {"Codigo_CBO": "223113", "Nome_da_Profissao": "Médico cirurgião pediátrico"},
    {"Codigo_CBO": "223114", "Nome_da_Profissao": "Médico cirurgião plástico"},
    {"Codigo_CBO": "223115", "Nome_da_Profissao": "Médico cirurgião torácico"},
    {"Codigo_CBO": "223116", "Nome_da_Profissao": "Médico citopatologista"},
    {"Codigo_CBO": "223118", "Nome_da_Profissao": "Médico clínico"},
    {"Codigo_CBO": "223120", "Nome_da_Profissao": "Médico da estratégia de saúde da família"},
    {"Codigo_CBO": "223123", "Nome_da_Profissao": "Médico de família e comunidade"},
    {"Codigo_CBO": "223125", "Nome_da_Profissao": "Médico dermatologista"},
    {"Codigo_CBO": "223128", "Nome_da_Profissao": "Médico do trabalho"},
    {"Codigo_CBO": "223131", "Nome_da_Profissao": "Médico em diagnóstico por imagem"},
    {"Codigo_CBO": "223134", "Nome_da_Profissao": "Médico em eletroencefalografia"},
    {"Codigo_CBO": "223136", "Nome_da_Profissao": "Médico em endoscopia"},
    {"Codigo_CBO": "223140", "Nome_da_Profissao": "Médico em medicina de tráfego"},
    {"Codigo_CBO": "223142", "Nome_da_Profissao": "Médico em medicina intensiva"},
    {"Codigo_CBO": "223143", "Nome_da_Profissao": "Médico em medicina nuclear"},
    {"Codigo_CBO": "223145", "Nome_da_Profissao": "Médico endocrinologista e metabologista"},
    {"Codigo_CBO": "223146", "Nome_da_Profissao": "Médico fisiatra"},
    {"Codigo_CBO": "223148", "Nome_da_Profissao": "Médico gastroenterologista"},
    {"Codigo_CBO": "223150", "Nome_da_Profissao": "Médico geneticista"},
    {"Codigo_CBO": "223154", "Nome_da_Profissao": "Médico hematologista"},
    {"Codigo_CBO": "223155", "Nome_da_Profissao": "Médico homeopata"},
    {"Codigo_CBO": "223156", "Nome_da_Profissao": "Médico infectologista"},
    {"Codigo_CBO": "223157", "Nome_da_Profissao": "Médico legista"},
    {"Codigo_CBO": "223158", "Nome_da_Profissao": "Médico mastologista"},
    {"Codigo_CBO": "223159", "Nome_da_Profissao": "Médico nefrologista"},
    {"Codigo_CBO": "223160", "Nome_da_Profissao": "Médico neurocirurgião"},
    {"Codigo_CBO": "223162", "Nome_da_Profissao": "Médico neurofisiologista"},
    {"Codigo_CBO": "223163", "Nome_da_Profissao": "Médico neurologista"},
    {"Codigo_CBO": "223165", "Nome_da_Profissao": "Médico oftalmologista"},
    {"Codigo_CBO": "223167", "Nome_da_Profissao": "Médico oncologista"},
    {"Codigo_CBO": "223170", "Nome_da_Profissao": "Médico ortopedista e traumatologista"},
    {"Codigo_CBO": "223172", "Nome_da_Profissao": "Médico otorrinolaringologista"},
    {"Codigo_CBO": "223174", "Nome_da_Profissao": "Médico patologista"},
    {"Codigo_CBO": "223176", "Nome_da_Profissao": "Médico pediatra"},
    {"Codigo_CBO": "223178", "Nome_da_Profissao": "Médico pneumologista"},
    {"Codigo_CBO": "223180", "Nome_da_Profissao": "Médico psiquiatra"},
    {"Codigo_CBO": "223182", "Nome_da_Profissao": "Médico radiologista intervencionista"},
    {"Codigo_CBO": "223183", "Nome_da_Profissao": "Médico radioterapeuta"},
    {"Codigo_CBO": "223185", "Nome_da_Profissao": "Médico reumatologista"},
    {"Codigo_CBO": "223187", "Nome_da_Profissao": "Médico sanitarista"},
    {"Codigo_CBO": "223190", "Nome_da_Profissao": "Médico urologista"}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('bold_professions.csv', index=False)

# Print the DataFrame
print(df)
