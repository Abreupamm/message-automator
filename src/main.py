from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import csv
import time
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import filedialog


def import_data(path: str):
    if '.csv' in path:
        with open(path) as file:
            archive = csv.DictReader(file, delimiter=',', quotechar='"')
            return list(archive)
    else:
        raise ValueError('Arquivo inválido')

def send_message():
    contacts_list = import_data('src/aqr_exemple.csv')

    mesage = entry_message.get()
    text = urllib.parse.quote(mesage)

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get('https://web.whatsapp.com/')


    while len(driver.find_elements(By.ID, 'side')) < 1:
        time.sleep(2)

    element_group = driver.find_elements(By.CSS_SELECTOR, 'span[title=TESTE]')
    element_group[0].click()

    for phone_number in contacts_list:

        number = phone_number['Telefone']
        # link = f'https://web.whatsapp.com/send?phone=55{number}&text={text}'
        # driver.get(link)
        # while len(driver.find_elements(By.CSS_SELECTOR, '._3E8Fg')) < 1:
        #     time.sleep(1)
        input_mensage = driver.find_elements(By.CLASS_NAME, 'selectable-text copyable-text iq0m558w g0rxnol2')
        input_mensage[0].send_keys(number)
        button_element = driver.find_element(By.CSS_SELECTOR, 'button.tvf2evcx')
        button_element.click()
        time.sleep(5)

    # driver.close()
    print('FIM')

# Interface Gráfica
root = tk.Tk()
root.title('Envio de Mensagens WhatsApp')

# Elementos da Interface
label_message = tk.Label(root, text='Digite sua mensagem:')
entry_message = tk.Entry(root, width=50)
button_send = tk.Button(root, text='Enviar Mensagens', command=send_message)

# Posicionamento dos Elementos
label_message.grid(row=0, column=0, padx=10, pady=10)
entry_message.grid(row=0, column=1, padx=10, pady=10)
button_send.grid(row=2, column=0, columnspan=2, pady=10)

# Execução da Interface
root.mainloop()