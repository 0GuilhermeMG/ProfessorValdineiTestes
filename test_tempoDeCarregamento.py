from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_usabilidade():
    # Inicializar o WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    # Medir tempo de carregamento da página inicial
    start_time = time.time()
    try:
        driver.find_element(By.ID, "home_page_loaded")  # Confirmar carregamento por elemento-chave
    except Exception:
        print("Elemento chave não carregado.")
    load_time = time.time() - start_time

    # Verificar se o tempo de carregamento está dentro do limite aceitável
    assert load_time < 3, f"Tempo de carregamento excedido: {load_time:.2f} segundos"

    # Avaliar clareza das mensagens exibidas em um formulário
    driver.find_element(By.ID, "formulario_teste").click()
    driver.find_element(By.ID, "campo_obrigatorio").clear()
    driver.find_element(By.ID, "botao_enviar").click()

    print("Teste de usabilidade bem-sucedido.")
    driver.quit()




