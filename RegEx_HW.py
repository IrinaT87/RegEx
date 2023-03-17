from pprint import pprint
import csv
import re
from collections import OrderedDict

with open('phonebook_raw.csv', 'rt', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


title=contacts_list[0]
del contacts_list[0]

for contact in contacts_list:
  lastname = contact[0]
  firstname = contact[1]
  surname = contact[2]
  
  count=0
  name=contact[0].split()
  for partname in lastname.split():
    contact[count] =partname
    count+=1
  if count < 3:
    for partname in firstname.split():
      contact[count] =partname
      count+=1
  if count < 3:
    for partname in surname.split():
      contact[count] =partname
      count+=1
  contact[5] = re.sub(r"(\+7|8) ?\(?(\d{3})\)?[ -]?(\d{3})-?(\d{2})-?(\d{2})(?:[ (]*(доб\.)? (\d{4})\)?)?", 
  r"+7(\2)\3-\4-\5 \6\7", contact[5]).strip()

contacts_list_ok=[]

for i in range(len(contacts_list)-1): 
  if contacts_list[i][0].strip()!=contacts_list[i+1][0].strip() and contacts_list[i][1].strip()!=contacts_list[i+1][1].strip():
    contacts_list_ok.append(contacts_list[i])
  if contacts_list[i][0].strip()==contacts_list[i+1][0].strip():
    contacts_list_ok.append(list(OrderedDict.fromkeys(contacts_list[i]+contacts_list[i+1])))
    
# print(contacts_list_ok)
  
with open("phonebook.csv", "w", encoding='utf-8',newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  
  datawriter.writerow(title)
  datawriter.writerows(contacts_list_ok)



      
      