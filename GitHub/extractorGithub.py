import random
from time import sleep
from selenium import webdriver
from datetime import datetime
from openpyxl import Workbook

now = datetime.now()
año=now.year
mes=now.month
dia=now.day
fecha = now.strftime("%Y-%m-%d")
driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://github.com/search')
buscador=driver.find_element_by_xpath("//input[@placeholder='Search GitHub']")
lenguaje='SEQUELIZE'
buscador.send_keys(f'{lenguaje} created:{fecha} created:{fecha}')
driver.find_element_by_xpath("//button[@type='submit']").click()
elementos=driver.find_elements_by_xpath("//li[@class='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source']")
lenguajes=driver.find_elements_by_xpath("//span[@itemprop='programmingLanguage']")
leng=[]
item=[]
cont_javasc=0
cont_type=0
cont_dif=0

for i in elementos:
    print(i.text)
    item.append( (i.text).split() )
    print('\n')

for l in lenguajes:
    if(l.text=='JavaScript'):
        cont_javasc+=1
    elif (l.text=='TypeScript'):
        cont_type+=1
    else:
        cont_dif+=1
    leng.append(l.text)

total=cont_javasc+cont_type
"""Crear Excel y Llenar Datos"""
libro=Workbook()
"""Seleccionar hoja"""
hoja_activa=libro.active
arr=[]
formato_excel=['ORM','FECHA','USADO POR','COLABORADORES','LENGUAJES','PREGUNTAS']
fila_excel=[lenguaje,f'{now.strftime("%d/%m/%Y")}',total,total,f'Existen {cont_javasc} ({int((cont_javasc/total)*100)}%) elementos de JavaScript y {cont_type} ({int((cont_type/total)*100)}%) elementos de TypeScript',total]
arr.append(formato_excel)
arr.append(fila_excel)
for elem in arr:
    hoja_activa.append(elem)
libro.save('datos.xlsx')
"""
print(f'Fecha Actual: {now}')
print(f'Existen {cont_javasc} ({int((cont_javasc/total)*100)}%) elementos de JavaScript y {cont_type} ({int((cont_type/total)*100)}%) elementos de TypeScript')
print(leng)"""
print(fecha)
