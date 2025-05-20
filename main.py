from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# lendo login e senha do arquivo
login = ""
senha = ""
telefone = ""
desc = ""
with open("auth.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    login = lines[0].strip()
    senha = lines[1].strip()
    telefone = lines[2].strip()

with open("inputs.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    desc = lines[random.randint(0, 2)].strip()


# Configuração do navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acessar o site do 1746
driver.get("https://www.1746.rio/")

# Espera até o botão de "Nova Solicitação" estar disponível
wait = WebDriverWait(driver, 20)
nova_solicitacao = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section[1]/div/div[1]/nav/div/ol[1]/li[19]/a")))
nova_solicitacao.click()

# Encontrar o elemento <select>
select_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div/div/div[2]/div/select")))
select = Select(select_element)
# selecionar serviço de perturbação do sossego
select.select_by_visible_text("Perturbação do Sossego")

time.sleep(2)

# Encontrar o elemento <select>
select_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div/div/div[2]/div/div/select")))
select = Select(select_element)
# selecionar serviço de fiscalização ...
select.select_by_visible_text("Fiscalização de perturbação do sossego")

# Iniciar solicitação
iniciar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Selecionar')]")))
iniciar.click()

time.sleep(4)

# informando login e senha
campo_email = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div[1]/div[2]/div[2]/article/footer/section/div/div/div[1]/form/div[1]/input")))
campo_senha = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div[1]/div[2]/div[2]/article/footer/section/div/div/div[1]/form/div[2]/input")))
driver.execute_script("arguments[0].scrollIntoView(true);", campo_email)

campo_email.send_keys(login)
campo_senha.send_keys(senha)

# entrando ...
log_in = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div[1]/div[2]/div[2]/article/footer/section/div/div/div[1]/form/div[3]/div/div[2]/button")))
driver.execute_script("arguments[0].scrollIntoView(true);", log_in)
driver.execute_script("arguments[0].focus();", log_in)
log_in.location_once_scrolled_into_view
time.sleep(0.5)
log_in.click()

# informando dados da solicitação
campo_nome_estabelecimento = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[7]/input")))
campo_nome_estabelecimento.send_keys("Posto Bom Pastor")

dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[10]/a")))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(1)  # aguarda renderização
driver.execute_script("arguments[0].click();", dropdown)
time.sleep(1)

# Espera a lista abrir e clica na opção desejada
opcao = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Menos de 20 pessoas')]")))
opcao.click()

dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[14]/a")))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(1)  # aguarda renderização
driver.execute_script("arguments[0].click();", dropdown)
time.sleep(1)

# Espera a lista abrir e clica na opção desejada
opcao = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Outros')]")))
opcao.click()

dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[15]/a")))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(1)  # aguarda renderização
driver.execute_script("arguments[0].click();", dropdown)
time.sleep(1)

# Espera a lista abrir e clica na opção desejada
opcao = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Outros')]")))
opcao.click()

campo_dias = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[17]/input")))
campo_dias.send_keys("Todos os dias até 17 hs")

dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[18]/a")))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(1)  # aguarda renderização
driver.execute_script("arguments[0].click();", dropdown)
time.sleep(1)

# Espera a lista abrir e clica na opção desejada
opcao = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Não')]")))
opcao.click()

dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[19]/a")))
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(1)  # aguarda renderização
driver.execute_script("arguments[0].click();", dropdown)
time.sleep(1)

# Espera a lista abrir e clica na opção desejada
opcao = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Outros')]")))
opcao.click()

campo_telefone = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[20]/input")))
campo_telefone.send_keys(telefone)

campo_endereco = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[21]/div[1]/input")))
campo_endereco.send_keys("Rua Bom Pastor")
driver.execute_script("arguments[0].scrollIntoView(true);", campo_endereco)
time.sleep(1)  # aguarda renderização
driver.execute_script("arguments[0].click();", campo_endereco)
time.sleep(1)

opcao_tijuca = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ul/li[1]")))
driver.execute_script("arguments[0].focus();", opcao_tijuca)
opcao_tijuca.location_once_scrolled_into_view
time.sleep(0.5)
opcao_tijuca.click()

campo_numero = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[21]/div[2]/input")))
campo_numero.send_keys("296")

campo_ponto_referencia = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[21]/div[7]/input")))
campo_ponto_referencia.send_keys("Posto Shell")

campo_desc = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/div[35]/textarea")))
campo_desc.send_keys(desc)

enviar = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div/div/div/div/form/footer/input")))
driver.execute_script("arguments[0].scrollIntoView(true);", enviar)
driver.execute_script("arguments[0].click();", enviar)

time.sleep(40)

numero_protocolo = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div[1]")))
print(numero_protocolo.text)

with open("outputs.txt", "a", encoding="utf-8") as f:
    f.write(numero_protocolo.text + " - " + login +"\n")

driver.quit() # fechar navegador