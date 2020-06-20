from gpiozero import LED, Button
import socket

#Configuração inicial para comunicação
ipServidor = '192.168.0.110'
porta = 8080 #Valor ficticio
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipServidor, porta))

#Configuração GPIO
btn = Button(25, pull_up=True)
ld = LED(18)

while True:
    btn.wait_for_press()
    s.send('Pressionado')
    serv_info = s.recv(4096)
    if serv_info == 'led_on':
        ld.on()

    btn.wait_for_release()
    s.send('Solto')
    serv_info = s.recv(4096)
    if serv_info == 'led_off':
        ld.off()
