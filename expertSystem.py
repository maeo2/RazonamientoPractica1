'''
 Sistema Experto para el guiado de un robot
 Versión primitiva: ir de punto a punto, frenando hasta velocidad 0 en cada uno,
 girar sobre su propio eje hacia el siguiente punto y repetir.
'''

import math
from objetivo import *

class ExpertSystem:
    def __init__(self) -> None:
        self.objetivoActual = None
        self.nombreAlumno = "Martín Echegaray Ojeda"
        self.paso = 0          # índice del punto al que va el robot dentro del objetivo
        self.girando = True    # True mientras gira sobre su eje hacia el punto

    # función setObjetivo
    #   Almacena el objetivo y reinicia el punto al que se dirige el robot
    def setObjetivo(self, objetivo):
        self.objetivoActual = objetivo
        self.paso = 0
        self.girando = True

    # función tomarDecision.
    #   Recibe la pose del robot (x, y, orientación en grados, v actual, w actual)
    #   Devuelve (velocidad lineal, velocidad angular)
    def tomarDecision(self, poseRobot):
        # Lista de puntos a recorrer: la recta tiene 2 y el triángulo 3
        puntos = [self.objetivoActual.getInicio()]
        if self.objetivoActual.getType() == 2:
            puntos.append(self.objetivoActual.getMedio())
        puntos.append(self.objetivoActual.getFin())

        destino = puntos[self.paso]

        # Distancia al punto y error de ángulo (en radianes, entre -pi y pi)
        dx = destino[0] - poseRobot[0]
        dy = destino[1] - poseRobot[1]
        distancia = math.hypot(dx, dy)
        error = math.atan2(dy, dx) - math.radians(poseRobot[2])
        error = math.atan2(math.sin(error), math.cos(error))

        # 1) Hemos llegado al punto: frenar del todo y, cuando v = 0, pasar al siguiente
        if distancia < 0.5:
            if abs(poseRobot[3]) < 0.05 and self.paso < len(puntos) - 1:
                self.paso = self.paso + 1
                self.girando = True
            return (0, 0)

        # 2) Girar sobre su eje (v = 0) hasta mirar hacia el punto
        if self.girando:
            if abs(error) < 0.035:   # unos 2 grados
                self.girando = False
            w = min(1, math.sqrt(0.8 * abs(error)))   # gira rápido y frena al acercarse
            if error < 0:
                w = -w
            return (0, w)

        # 3) Avanzar: velocidad alta lejos del punto, disminuyendo hasta 0 al llegar
        v = math.sqrt(1.8 * max(distancia - 0.45, 0))
        if v > 3:
            v = 3
        w = 2 * error   # pequeña corrección para ir en línea recta
        return (v, w)
