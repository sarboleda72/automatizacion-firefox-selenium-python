from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

try:
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
except:
    driver = webdriver.Firefox()

#Link de la pagina
url='https://serviceable-riding.000webhostapp.com/dashboard/login.php'

#se abre la URL
driver.get(url)

#Se abre la ventana al máximo
driver.maximize_window()

#Se espera medio segundo despues que terminar cagar la pagina web
driver.implicitly_wait(1)

#-------------------Pagina acceso------------------

#Se capturan  los elementos a interactuar en la pagina
inpUsuario = driver.find_element(by=By.NAME, value="usuario")
inpContrasenia = driver.find_element(by=By.NAME, value="contrasenia")
btnEnviar = driver.find_element(by=By.CSS_SELECTOR, value="button")

#Se ejecutan acciones en los elementos capturados
inpUsuario.send_keys("julia01")
inpContrasenia.send_keys('julia123')
btnEnviar.click()

#Se espera medio segundo despues que terminar cagar la pagina web
driver.implicitly_wait(1)

#-------------------Dashboard------------------

#Se capturan  los elementos a interactuar en la pagina

btnPersona=driver.find_element(by=By.XPATH, value="/html/body/div[1]/ul/li[2]/a")
btnListarPersona=driver.find_element(by=By.XPATH, value="/html/body/div[1]/ul/li[2]/div/div/a")

#Se ejecutan acciones en los elementos capturados
btnPersona.click()
time.sleep(1)
btnListarPersona.click()

time.sleep(1)

#-------------------Modulo persona ------------------

#Se capturan  los elementos a interactuar en la pagina
btnPersona=driver.find_element(by=By.XPATH, value="/html/body/div[1]/ul/li[2]")
btnNuevaPersona=driver.find_element(by=By.XPATH, value="/html/body/div[1]/ul/li[2]/div/div/a")
btnCerrarFormulario=driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div/div[3]/button[1]")


btnPersona.click()
time.sleep(1)
btnNuevaPersona.click()
time.sleep(1)
btnCerrarFormulario.click()
time.sleep(1)


#------------------- Salir ------------------
#Se capturan  los elementos a interactuar en la pagina
btnDesplegar=driver.find_element(by=By.ID, value="userDropdown")
btnSalir=driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/nav/ul/li/div/a[2]")

#Se ejecutan acciones en los elementos capturados
btnDesplegar.click()
btnSalir.click()
