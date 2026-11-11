RyRDC

Ingeniería en I.A.

Ingenieria en

## Universidad de Alicante Departamento de Ciencia de la Computación e Inteligencia Artificial Curso 2026/2027

## 1 Práctica 1. Sistemas Expertos

## Descripción general

En esta práctica se pretende elaborar métodos para el control de un robot móvil utilizando un sistema experto. Se va a considerar un robot móvil que puede desplazarse por un plano horizontal mediante comandos de velocidad lineal y velocidad angular. El objetivo del robot será recorrer lo más cercanamente posible un camino a través de su entorno. El entorno está libre de obstáculos y no se tendrán en cuenta los posibles sensores del robot. Conoceremos únicamente su pose, es decir, la posición (x, y) del robot en el plano y la orientación del robot. Se proporcionará un proyecto que realizará la simulación del movimiento del robot y la visualizará. Según el robot vaya alcanzando los objetivos que vaya recibiendo irá obteniendo una puntuación de recompensa de acuerdo a lo bien que se ajuste su trayectoria a los objetivos y el tiempo que emplee

en alcanzarlos.

## Python

Para el desarrollo de la práctica se utilizará Python como lenguaje de programación. Se proporcionará un proyecto Python con el código necesario para lanzar un entorno gráfico que permita visualizar la pose del robot y los datos de los objetivos que marcarán el camino a recorrer por el robot

## Proyecto

El proyecto proporcionado a los alumnos contiene las siguientes 4 clases:

- P1Launcher.py Esta clase se encarga de crear el entorno gráfico y comunicar los distintos objetos implicados en la simulación. También contiene los métodos para pintar los elementos de la simulación en la pantalla.

- Robot.py Esta clase mantiene la representación del robot móvil. Internamente almacena la pose del robot y los comandos de velocidad lineal y angular que reciba. También se encarga de actualizar la pose de acuerdo a las velocidades y a su dinámica interna. Los alumnos no interactúan con objetos de esta clase directamente, aunque recibirán los datos de la pose del robot como entrada al sistema experto

- Objetivo.py. Esta clase representa los objetivos que debe alcanzar el robot. Estos objetivos pueden ser de dos tipos diferentes:

- Objetivo tipo segmento recto entre dos puntos sobre el plano en el que se mueve el robot. Se caracteriza por tener un punto de inicio y un punto de fin. Cuando el objetivo sea de este tipo, la misión del robot será llegar al punto final del segmento. Cuanto más


- cerca se mueva el robot al segmento y cuando menos tiempo tarde en recorrerlo, mayor será la puntuación de recompensa que se obtendrá.

- Objetivo tipo triángulo. Estará formado por un punto de inicio, un punto medio y un punto final que entre los tres forman un plano en el espacio. La finalidad será recorrer el espacio desde el punto de inicio al punto final alrededor del punto medio, pero sin entrar en el triángulo definido por los tres puntos. En este caso la puntuación de recompensa premiará llegar al punto final en el menor tiempo posible pero penalizará entrar dentro del área del triángulo.

- expertSystem.py. En esta clase se implementará el sistema experto que obtendrá los comandos de velocidad lineal y angular que debe ejecutar el robot en cada instante de tiempo para resolver el problema propuesto. Se detalla más adelante

Las clases P1Launcher.py, Robot.py y Objetivo.py (y cualquier clase adicional que, durante el cuatrimestre, se vaya añadiendo al proyecto) no podrán ser modificadas por los alumnos. En caso de que sea necesario modificar alguno de estos ficheros para la corrección de errores o para añadir nuevas funcionalidades será el profesorado quien realice los cambios. En este caso se informará a los alumnos para que actualicen estos ficheros. El alumno modificará únicamente los métodos incluidos en la clase expertSystem. Se podrán

añadir a esta clase las propiedades y métodos adicionales que el alumno estime convenientes.

## Aplicación

Tras ejecutar el proyecto proporcionado dará comienzo una aplicación con un interfaz de usuario (UI) como el que se muestra en la Figura 1. En la ventana simplemente se muestra el segmento que ha de recorrer el robot y la repersentación del robot como un círculo de color rojo. El segmento

tiene marcado el inicio con un punto de color verde y el final con un punto de color rojo.


Figure 1: Ventana de la aplicación

## Puntos Ejercicio 1. Implementar un sistema Experto clásico – 6

En este ejercicio se trata de implementar un sistema experto que gobierne el comportamiento de un robot móvil para trasladarse desde su extremo inicial al punto final del segmento. Se tendrán que crear las reglas de tipo if-then necesarias para que el robot se mueva desde la posición en la que se encuentre inicialmente hasta la posición final del segmento. Se valorará que el movimiento del robot sea lo más ajustado al trazado. El robot se mueve mediante un sistema dinámico diferencial utilizando dos ruedas motrices. Esto quiere decir que cuando la velocidad lineal del robot es cero, los giros se realizan alrededor del punto medio del robot. La velocidad lineal máxima que puede alcanzar el robot es de 3 m/s y la velocidad angular máxima es de 1 rad/s. Además presenta una aceleración y deceleración lineal de 1 m/s2 y una aceleración y deceleración angular de 0.5 rad/s2 El código debe estar preparado para que funcione independientemente de las posiciones del robot y de los puntos de inicio y final del objetivo. La aplicación puede que tenga una lista de objetivos y que vaya asignando nuevos objetivos al sistema experto cuando el robot termina de recorrer cada objetivo.


## Clase ExpertSystem

El alumno incluirá su código únicamente en la clase ExpertSystem (fichero expertSystem.py). Importante: la clase incluye una propiedad llamada nombreAlumno en la que cada alumno deberá poner su nombre y apellidos para que la práctica pueda ser corregida. La implementación del sistema experto se ha de realizar en el fichero proporcionado y de nombre expertSystem.py. Dentro de la clase ExpertSystem, el sistema experto estará implementado en la función tomarDecision. Esta función recibe la pose del robot y según el objetivo a recorrer debe devolver la velocidad angular y la velocidad lineal que el robot deberá tomar para llegar a la posición final del objetivo actual. La información del objetivo que el robot debe recorrer se mantiene en la variable de clase

objetivoActual.

## Ejercicio 1. Documentación

Es obligatorio documentar todo el trabajo realizado. Si alguna parte del trabajo realizado no se documenta se considerará como que no se ha hecho, lo que puede llevar a suspender la práctica. La documentación debe incluir una explicación detallada de todas las reglas implementadas y su justificación, así como de las pruebas que se hayan realizado para comprobar su correcto

funcionamiento.

## Ejercicio 1. Evaluación

El ejercicio 1 se evalúa en dos partes: La ejecución y la documentación La parte de ejecución se puntuará de 0 a 10 puntos. Se realizarán diferentes pruebas y se tendrán en cuenta las puntuaciones obtenidas en cada una. Puntuaciones más altas supondrán notas más altas. La parte de documentación también se puntuará de 0 a 10 puntos teniendo en cuenta la legibilidad del fichero de documentación y que cumpla con los requisitos establecidos en el apartado anterior.

## (Optativo) – 4 Puntos Ejercicio 2. Implementar un Sistema Experto Difuso

El ejercicio 2 consiste en hacer exactamente lo mismo que en el ejercicio 1, pero esta vez en lugar de utilizar un sistema experto basado en reglas de producción de la lógica de primer orden utilizaremos un sistema experto difuso basado en reglas difusas.


En primer lugar, deberemos instalar una librería de python para realizar la inferencia difusa del sistema experto. Esta librería la podemos descargar de https://jdvelasq.github.io/fuzzy-expert/. Con [URL 🔗](https://jdvelasq.github.io/fuzzy-expert/)

ella vamos a poder especificar:

- Las variables difusas de entrada y de salida

- Las reglas difusas de nuestro sistema experto

- El modelo de sistema experto difuso que utilice las variables y las reglas difusas.

Para facilitar el trabajo de los estudiantes, se proporciona un fichero llamado fuzzyExpert.py con la plantilla de lo que debería ser la clase a implementar con el sistema experto difuso. Este fichero ya está preparado para funcionar con el software proporcionado para la resolución del ejercicio

anterior.

## Ejercicio 2. Documentación

Es obligatorio documentar todo el trabajo realizado. Si alguna parte del trabajo realizado no se documenta se considerará como que no se ha hecho, lo que puede llevar a suspender la práctica. La documentación debe incluir una explicación detallada de todas las reglas implementadas y su justificación, así como de las pruebas que se hayan realizado para comprobar su correcto

funcionamiento.

## Ejercicio 2. Evaluación

Similar al ejercicio 1.

## Entrega de la práctica

La fecha límite de entrega de los dos ejercicios de la primera práctica será el día 11 de noviembre. La entrega se realizará a través de una tarea en la página moodle de la asignatura. Los alumnos deberán entregar un fichero comprimido que contenga los ficheros expertSystem.py, fuzzyExpert.py

y el fichero con la documentación en formato PDF.

- ¡¡¡IMPORTANTE!!! Recordad que las prácticas son individuales y NO se pueden hacer en parejas o grupos. Cualquier código copiado supondrá un suspenso de la práctica para todas las personas implicadas en la copia. Se utilizarán herramientas para la detección de copia. Estos hechos serán comunicados a la Escuela Politécnica para que se tomen las medidas disciplinarias oportunas contra los infractores.
