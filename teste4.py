val = """06158-Médico acupunturista

06133-Médico alergista/imunologista

06114-Médico anatomopatologista

06115-Médico anestesista

06175-Médico angiologista

06116-Médico broncoesofalogista

06117-Médico cardiologista

06159-Médico cancerologista

06120-Médico cirurgião cardiovascular

06146-Médico cirurgião de cabeça e pescoço

06161-Médico cirurgião de mao

06163-Médico cirurgião do aparelho digestivo

06110-Médico cirurgião em geral

06112-Médico cirurgião pediátrico

06180-Médico cirurgião plástico

06154-Médico cirurgião torácico

06118-Médico cirurgião vascular

06153-Médico citopatologista

06113-Médico de perícias médicas

06141-Médico de saúde da família

06119-Médico dermatologista

06122-Médico do trabalho

06125-Médico endocrinologista

06127-Médico endoscopista

06128-Médico fisiatra

06123-Médico gastroenterologista

06143-Médico geneticista clínico

06151-Médico geral comunitário

06134-Médico geriatra

06132-Médico ginecologista

06149-Médico ginecologista/obstetra

06136-Médico hansenologista

06124-Médico hematologista

06135-Médico hemoterapeuta

06148-Médico homeopata

06144-Médico infectologista

06166-Médico intensivista

06137-Médico legista

06139-Médico mastologista

06177-Médico medicina esportiva

06138-Médico nefrologista

06131-Médico neurocirurgião

06142-Médico neurologista

06126-Médico nuclear

06145-Médico obstetra

06147-Médico oftalmologista

06168-Médico oncologista cirúrgico

06129-Médico oncologista clínico

06121-Médico oncologista pediátrico

06150-Médico ortopedista

06152-Médico otorrinolaringologista

06190-Médico outros medicos

06172-Médico patologista clínico

06155-Médico pediatra

06164-Médico plantonista

06157-Médico pneumotisiologista

06160-Médico proctologista

06162-Médico psiquiatra

06165-Médico radiologista

06167-Médico radioterapeuta

06130-Médico reumatologista

06140-Médico sanitarista

06156-Médico ultrassonografista

06170-Médico urologista"""

lines = val.split("\n")
parsed_lines = []

for line in lines:
   if not line or line.isspace():
      continue
   parsed_lines.append(line.strip().replace('\n',""))

with open("professions5.csv","w") as f:
   f.write("codigo,nome_profissao\n")

   for line in parsed_lines:
      index = line.find('-')
      f.write(f"{line[:index]},{line[index+1:]}\n")

print(parsed_lines)