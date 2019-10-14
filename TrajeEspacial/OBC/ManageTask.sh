# Configuración inicial de fábrica, depende del estado del archivo status.txt que indica 
# internamente el estado de la configuración, es decir, si dice NEW quiere decir que se 
# necesita realizar la actualización, encambio, si dice CONFIGURATED, quiere decir que 
# ya se encuentra configurado el dispositvio. Este arcivo se encuentra afuara del proyecto, 
# y se crea antes de subir la imagen a la memoria SD. Adicionalmente, instala Arduino, de 
# manera que se pueda actualizar los periféricos desde la computadora. Nota, es necesario 
# modificar el archivo crontab desde fabrica
#!/bin/bash

sudo echo "2" > /sys/class/gpio/export # Number pin (GPIO2) 
sudo echo "in" > /sys/class/gpio/gpio2/direction # Status pin (in or out)
cd SpaceSuit
python HMI/ScreenSpaceSuit.py
cd
while true; do
	state=$(cat /sys/class/gpio/gpio2/value) # Read state pin, this pin is associated with the button
	if [ "$state" = "0" ];then # Condition of the button state
		cd SpaceSuit
		git pull
        	python HMI/ScreenSpaceSuit.py
		cd
        #Prueba exitosa
	fi
done



# Configuración a WiFi es un archivo con el nombre de WiFi.txt que basicamente contiene
# el nombre de usuario y contraseña, y por medio de una instrucción que accede al archivo 
# que gestiona la conexión a WiFI insertando el usuario y contraseña. Este archivo se encuentra 
# en esta misma carpeta el cual tiene la opción de cambiarse desde repositorio, por lo que si se 
# cambia la configuración del router es necesario cambiar el contenido del archivo y realizar 
# la actualización oprimiendo el botón de actualización del proyecto en el dispositivo, para
# que se configure al nuevo usuario y contraseña. Nota revisar cambiar esté archivo por 
# bluetooth.
