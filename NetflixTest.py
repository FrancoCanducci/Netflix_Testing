from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializar o WebDriver sem o modo headless
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navegar para a página de login da Netflix
driver.get("https://www.netflix.com/login")

# Aguardar a página carregar completamente
time.sleep(3)

# Localizar os campos de email e senha
email_field = driver.find_element(By.CSS_SELECTOR, 'input[name="userLoginId"]')
password_field = driver.find_element(By.NAME, "password")

# Preencher o email e a senha incorretos
email_field.send_keys("email_falso@example.com")
password_field.send_keys("senha_falsa")

# Submeter o formulário
password_field.send_keys(Keys.RETURN)

# Aguardar a resposta do servidor
time.sleep(3)

# Verificar se uma mensagem de erro é exibida ou se a URL ainda contém "login"
login_blocked = False

try:
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-uia='error-message-container']")
    login_blocked = True
except:
    pass

current_url = driver.current_url
if "login" in current_url:
    login_blocked = True

if login_blocked:
    print("Teste de segurança no login: Acesso não autorizado bloqueado corretamente.")
else:
    print("Teste de segurança no login falhou: Acesso não autorizado não bloqueado.")

# Aguardar um pouco antes de fechar o navegador
time.sleep(5)

# Fechar o navegador
driver.quit()
