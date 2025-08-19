import pyautogui

from time import sleep # Biblioteca sleep é necessaria para pausar a execução

cont = 0 # Inicio da contagem
for c in range(11): # Tamanho da contagem
    pyautogui.moveTo(x=267, y=109) # Altere para sua posição
    sleep(0.4) # Pausa para garantir que a ação anterior foi concluída
    pyautogui.click(x=267, y=109) # Altere para sua posição
    sleep(0.5) # Pausa para garantir que a ação anterior foi concluída
    pyautogui.write(f"aula_{cont}.py") # PyAutoGUI escreve o nome do arquivo
    pyautogui.press("enter") # PyAutoGUI pressiona a tecla "enter"
