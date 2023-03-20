from selenium import webdriver
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles.borders import Border, Side



# Crear un estilo de borde
borde = Border(left=Side(style='thin'),
               right=Side(style='thin'),
               top=Side(style='thin'),
               bottom=Side(style='thin'))

def realizar_busqueda(driver,lenguaje,fecha_desde,fecha_hasta):
    buscador = driver.find_element_by_xpath("//input[@placeholder='Search GitHub']")
    buscador.send_keys(f'{lenguaje} created:{fecha_desde} created:{fecha_hasta}')
    buscador.submit()
    elementos = driver.find_elements_by_xpath(
        "//li[@class='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source']")
    lenguajes = driver.find_elements_by_xpath("//li[@class='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source']//span[@itemprop='programmingLanguage']")
    leng = []
    item = []
    cont_javasc = 0
    cont_type = 0
    cont_dif = 0
    for i in elementos:
        item.append((i.text).split())

    for l in lenguajes:
        if (l.text == 'JavaScript'):
            cont_javasc += 1
        elif (l.text == 'TypeScript'):
            cont_type += 1
        else:
            cont_dif += 1
        leng.append(l.text)

    total = cont_javasc + cont_type+cont_dif
    resultados = [
        lenguaje,
        f'{datetime.now().strftime("%d/%m/%Y")}',
        total,
        total,
        f'Existen {cont_javasc} ({int((cont_javasc / total) * 100)}%) elementos de JavaScript y {cont_type} ({int((cont_type / total) * 100)}%) elementos de TypeScript, lenguajes diferentes {cont_dif} ({int((cont_dif / total) * 100)}%)',
        total
    ]
    return resultados

# Configuración inicial
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://github.com/search')
SEQUELIZE='SEQUELIZE'
BOOKSHELF='BOOKSHELF'
PRISMA='PRISMA'

# Realizar la primera búsqueda
fecha_actual = datetime.now().strftime("%Y-%m-%d")
siguiente = driver.find_elements_by_xpath("//a[@class='next_page']")
siguiente_final = driver.find_elements_by_xpath("//span[@class='next_page disabled']")
driver.implicitly_wait(2)
if (len(siguiente) >= 1):
    resultados_1 = realizar_busqueda(driver, SEQUELIZE, fecha_actual, fecha_actual)
    siguiente[0].click()
    if (len(siguiente_final) == 0):

        driver.implicitly_wait(2)
else:
    print("Salida de condicion, paginado completo")


# Crear el archivo de Excel y escribir los resultados de la primera búsqueda
libro=Workbook()
hoja_activa=libro.active
formato_excel=['ORM','FECHA','USADO POR','COLABORADORES','LENGUAJES','PREGUNTAS']
hoja_activa.append(formato_excel)
hoja_activa.append(resultados_1)

#Abrir una nueva pestaña para la segunda búsqueda
driver.execute_script("window.open('https://github.com/search')")
driver.switch_to.window(driver.window_handles[1])

# Realizar la segunda búsqueda y escribir los resultados en la fila siguiente
resultados_2 = realizar_busqueda(driver, BOOKSHELF, fecha_actual, fecha_actual)
hoja_activa.append(resultados_2)

#Abrir una nueva pestaña para la tercera búsqueda
driver.execute_script("window.open('https://github.com/search')")
driver.switch_to.window(driver.window_handles[2])

# Realizar la tercera búsqueda y escribir los resultados en la fila siguiente
resultados_3 = realizar_busqueda(driver, PRISMA, fecha_actual, fecha_actual)
hoja_activa.append(resultados_3)

# Aplicar el estilo de borde a cada fila
for fila in hoja_activa.iter_rows(min_row=2):
    for celda in fila:
        celda.border = borde

# Guardar el archivo de Excel
libro.save('datos.xlsx')

# Cerrar el navegador
driver.quit()
