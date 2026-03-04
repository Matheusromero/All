print("\nQuantas matérias você favoritou? (apenas o numero)")
materias = int(input())
print("Me diga seu login do eniac")
login = str("111202022")
print("Me diga sua senha do eniac (ninguém terá ela ao final do codigo)")
senha = str("Matheusrr01@")
for f in range(materias):
    import pyautogui
    import time
    pyautogui.PAUSE = 1
    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("enter")
    pyautogui.write("https://eniac-edu.grupoa.education/plataforma/auth/signin")
    pyautogui.press("enter")
    time.sleep(7)
    pyautogui.press("tab")
    pyautogui.write(login)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.click(x=189, y=397) #Descubra utilizando sleep e printando o local do click
    time.sleep(5)
    pyautogui.click(x=674, y=961) #Descubra utilizando sleep e printando o local do click
    time.sleep(7)
    pyautogui.scroll(-140)#Chute até conseguir
    time.sleep(2)
    pyautogui.click()
time.sleep(2) #Descubra utilizando sleep e printando o local do click
pyautogui.scroll(-140)
pyautogui.click(x=331, y=994) #Entrei na atividade
time.sleep(3)
pyautogui.click(x=1874, y=282)
time.sleep(2)#1 clique
pyautogui.click(x=289, y=350)
pyautogui.click(x=1874, y=282)
time.sleep(1) #Descubra utilizando sleep e printando o local do click
pyautogui.scroll(70)
pyautogui.click(x=1156, y=239) #Click no botão
time.sleep(5) #2 clique
pyautogui.click(x=289, y=450)
pyautogui.click(x=1874, y=282)
time.sleep(1) #Descubra utilizando sleep e printando o local do click
pyautogui.scroll(70)
pyautogui.click(x=1156, y=239) #Click no botão

time.sleep(5) #4 clique
pyautogui.click(x=289, y=650)
pyautogui.click(x=1874, y=282)
time.sleep(1) #Descubra utilizando sleep e printando o local do click
pyautogui.scroll(70)
pyautogui.click(x=1156, y=239) #Click no botão

time.sleep(5) #5 clique
pyautogui.click(x=289, y=750)
pyautogui.click(x=1874, y=282)
time.sleep(1) #Descubra utilizando sleep e printando o local do click
pyautogui.scroll(70)
pyautogui.click(x=1156, y=239) #Click no botão

time.sleep(5) #6 clique
pyautogui.click(x=289, y=850)
pyautogui.click(x=1874, y=282)
time.sleep(1) #Descubra utilizando sleep e printando o local do click
pyautogui.scroll(70)
pyautogui.click(x=1156, y=239) #Click no botão

time.sleep(5) #7 clique
pyautogui.click(x=289, y=950)
pyautogui.click(x=1874, y=282)
time.sleep(1) #Descubra utilizando sleep e printando o local do click
pyautogui.scroll(100)
pyautogui.click(x=1156, y=239) #Click no botão

time.sleep(5) #8 clique
pyautogui.click(x=1874, y=282)
pyautogui.scroll(-9999)
pyautogui.click(x=1134, y=910)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=1767, y=978)