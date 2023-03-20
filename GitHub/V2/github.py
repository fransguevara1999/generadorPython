from selenium import webdriver
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles.borders import Border, Side

driver = webdriver.Chrome('../chromedriver.exe')
driver.get('https://github.com/search')
SEQUELIZE='SEQUELIZE'
BOOKSHELF='BOOKSHELF'
PRISMA='PRISMA'
fecha_actual = datetime.now().strftime("%Y-%m-%d")


def realizar_busqueda(driver,lenguaje,fecha_desde,fecha_hasta):
    cont_javasc = 0
    cont_type = 0
    cont_dif = 0
    leng = []
    #tit=[]
    buscador = driver.find_element_by_xpath("//input[@placeholder='Search GitHub']")
    buscador.send_keys(f'{lenguaje} created:{fecha_desde} created:{fecha_hasta}')
    buscador.submit()
    while True:
        try:
            siguiente = driver.find_elements_by_xpath("//a[@class='next_page']")
            siguiente_final = driver.find_elements_by_xpath("//span[@class='next_page disabled']")
            lenguajes = driver.find_elements_by_xpath(
                "//li[@class='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source']")
            if(len(siguiente[0])>=1):
                siguiente[0].click()
                for l in lenguajes:
                    #titulo=driver.find_element_by_xpath("//div[contains(@class, 'f4 text-normal')]").get
                    lenguajes2=driver.find_element_by_xpath("//span[@itemprop='programmingLanguage']")
                    #tit.append(titulo.text)
                    leng.append(lenguajes2.text)
                    if (lenguajes2.text == 'JavaScript'):
                        cont_javasc += 1
                    elif (lenguajes2.text == 'TypeScript'):
                        cont_type += 1
                    else:
                        cont_dif += 1
        except:
            break
        print(leng)
        print(f'Lenguaje JavaScript: {cont_javasc}, Lenguaje TypeScrit: {cont_type}, Lenguajes Diferentes:{cont_dif}')
        resultados=[lenguaje,
                    f'{datetime.now().strftime("%d/%m/%Y")}',
                    len(leng),
                    len(leng),
                    f'Existen {cont_javasc} ({int((cont_javasc / len(leng)) * 100)}%) elementos de JavaScript y {cont_type} ({int((cont_type / len(leng)) * 100)}%) elementos de TypeScript, lenguajes diferentes {cont_dif} ({int((cont_dif / len(leng)) * 100)}%)',
                    len(leng)]
    return resultados

resultados_1 =realizar_busqueda(driver, SEQUELIZE, fecha_actual, fecha_actual)
print(resultados_1)