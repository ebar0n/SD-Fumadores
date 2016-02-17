# SD-Fumadores
Solución al problema clásico *EL FUMADOR DE CIGARROS*.

### Descripción del problema
Considere un sistema con tres procesos fumadores y un proceso agente:

- Cada fumador está continuamente enrollando y fumando cigarrillos.
- Sin embargo, para enrollar y fumar un cigarrillo, el fumador necesita tres ingredientes: tabaco, papel, y fósforos.
- Uno de los procesos fumadores tiene papel, otro tiene el tabaco y el tercero los fósforos.
- El agente tiene una cantidad infinita de los tres materiales.
- El agente coloca dos de los ingredientes sobre la mesa.
- El fumador que tiene el ingrediente restante enrolla un cigarrillo y se lo fuma, avisando al agente cuando termina.
- Entonces, el agente coloca dos de los tres ingredientes y se repite el ciclo.

### Descripción de la solucion
La solución al problema se desarrollo en python, usando conexiones tcp para conectar los diferentes fumadores y agente desde equipos remotos.

Pasos previos:
- Iniciar un proceso agente.
- Iniciar los 3 procesos fumadores

Lógica usada:
- Al momento de un fumador conectarse solicita de una vez los ingredientes necesarios para fumar.
- Una vez el agente detecta todos los fumadores conectados, selecciona aleatoriamente 2 ingredientes, e informa al fumador respectivo.
- Dicho fumador hace uso del recurso y apenas termina le avisa al agente, para que vuelva a servir nuevos ingredientes.
- En caso de que un fumador se desconecte, el agente se entera, pero si algún otro fumador estaba usando el recurso, termina de fumar y espera nuevamente a que todos los fumadores están conectados para dispensar nuevos ingredientes, en caso de que el fumador desconectado sea el que ocupa el recurso, se libera de una vez y espera a que vuelva a conectarse.
- El agente dispensa una cantidad infinita de ingredientes, el proceso termina cuando el agente se desconecta.
