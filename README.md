# SAPCE SUIT
## EEH 
Son las siglas en inglés de (EMU Electrical Harnnesses), es el sistema que se encarga de administrar las funciones de los sensores biomédicos que esta compuesto por: los sensores de temperatura y sensor pulsoximetro; este módulo es controlado por un microcontrolador ATMEGA328P al que se le implementa un bootlader para Arduino, de manera que se pueda desarrollar usando el IDE de Arduino.

Para que se pueda realizar el envío de información de la medición al microcontrolador se realiza mediante los distintos periféricos que lo componen, como se muestra en la siguiente tabla:

| Elemento | Referencia | Periférico |
| -------- | ----------|----------|
|Temperatura||ADCx|
|Pulsoximetría||I2C|


## LSS
Son las siglas en inglés de (Life Support Subsystem), en este apartado se implementa la electrónica asociada a este subsistema el cual se controla tanto los actuadores como son: los ventiladores, la bomba, y la linterna del casco, cómo tambien sensores como es el sensor de presión; este módulo es controlado por un microcontrolador ATMEGA328P al que se le implementa un bootlader para Arduino, de manera que se pueda realizar desarrollos usando el IDE de Arduino.
Para que se pueda realizar el envío de información de la medición y la devida actuación del microcontrolador se realiza mediante los distintos periféricos que lo componen, como se muestra en la siuguiente tabla:    

| Elemento | Referencia | Periférico |
| -------- | ----------|----------|
|Ventilador||PWMx|
|Bomba||PWMx|
|Linterna||PWMx|
|Manómetro||ADCx|

# OBC
Son siglas en inglés de (On Board Computer) este sistema es básicamente la computadora que controla las funciones generales de los periféricos; está desarrollado sobre una placa Raspberry PI 3B que tiene dos funciones principales que son: gestor de periféricos,y gestor de tareas internas.

## Gestor de periféricos
Se encarga de administrar los diferentes módulos por medio de una comunicación USB con los otros microcontroladores, enviando y recibiendo constantemente paquetes de datos en forma de JSON.
### EEH
De este periférico solo recibe información de los sensores biomédicos, la estructura de los paquetes de información estan construidas en forma de JSON de la siguiente forma:
{
    "Pulse": 70,
    "Oxigen":60,
    "Temperature": [37,40,36,38]
}
### LSS
Des este periférico se trasmite (actuadores) y se recibe (Manómetro) datos desde la Raspberry, la estructura de los paquetes de información estan construidas en forma de JSON de la siguiente forma:
Envía:
{
    "Pression":40
}
Recibe:
{
    "Light": 40,
    "Pumps": 70,
    "Fan":[60,80]
}
### HMI
Se encarga de mostar la medida de los sensores, el estado de los actuadores, y de establecer una comunicación con otras entidades, esta dividido en tres paginas principales que son:
#### Página principal

#### Página de interacción con otro traje

#### Página de interacción con Rover

#### Página de interacción con Base
instalaci{on de imagenes en la pantalla >> sudo python setup.py install <<

## Gestor de tareas internas
Se encarga principalmente de administrar las tareas internas de la computadora como la actualización de archivos desde repositorio según el estado del botón de actualización, la configuración inicial de fábrica, la configuración a router