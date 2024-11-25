from selenium import webdriver
import time

def medir_tempo_de_carregamento(url):
    """
    Mide o tempo de carregamento de uma página.

    Args:
        url (str): URL da página a ser carregada.

    Returns:
        float: Tempo de carregamento em segundos.
    """

    driver = webdriver.Chrome()  # Substitua por Firefox, Edge, etc. se necessário
    start_time = time.time()
    driver.get(url)
    end_time = time.time()
    driver.quit()
    return end_time - start_time

# URL da página inicial do YouTube
url_youtube = "https://www.youtube.com/"

# Medir o tempo de carregamento e imprimir o resultado
tempo_de_carregamento = medir_tempo_de_carregamento(url_youtube)
print(f"O tempo de carregamento da página inicial do YouTube foi de {tempo_de_carregamento:.2f} segundos.")