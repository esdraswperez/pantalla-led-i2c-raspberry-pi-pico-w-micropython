from machine import Pin, I2C
from time import sleep
from pico_i2c_lcd import I2cLcd


i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

direccion = i2c.scan()[0]

lcd = I2cLcd(i2c,direccion,2,16)

while True:
    lcd.move_to(0,0)
    lcd.putstr("Bienvenido a:")
    sleep(0.8)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Ingenieria")
    lcd.move_to(0,1)
    lcd.putstr("en Sistemas")
    sleep(0.8)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Universidad")
    lcd.move_to(0,1)
    lcd.putstr("Mariano Galvez")
    sleep(0.8)
    lcd.clear()
    
    

#print("La dirección es: ", direccion)
