import RPi.GPIO as GPIO
import time

led = 3
pulsador = 7

def led_pulsador(bandera): # funcion que cambia el estado del led al pulsar 1 vez
	estados = GPIO.input(pulsador) 
	# estados para ver si el pulsador fue presionado
	if(estados == GPIO.LOW):
		bandera = not bandera #negamos el estado cuando el pulsador es presionado
		time.sleep(0.04)
	if(bandera == True): # encender led
		GPIO.output(led, GPIO.HIGH)
		print("ON")
	if(bandera == False): # apagar led
		GPIO.output(led, GPIO.LOW)
		print("OFF")
	return bandera