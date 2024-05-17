#Este codigo foi feito baseado nas instrucoes presentes na prova

from collections import deque
import argparse
from src.movClass import Movimento
import rclpy


# Criação de um deque vazio
dq = deque()
parser = argparse.ArgumentParser(description="Mover a tartaruga")
parser.add_argument("--vx", help="Velocidade em x", type=float)
parser.add_argument("--vy", help="Velocidade em 7", type=float)
parser.add_argument("--vtheta", help="Velocidade angular", type=float)
parser.add_argument("--tempo_em_ms", help="Tempo de movimento", type=float)
args = parser.parse_args()
rclpy.init()
dq.append(Movimento(args.vx,args.vy,args.vtheta,args.tempo_em_ms))
mov = dq.popleft()
mov.start()

while True:
    if mov.exec() and len(dq) != 0:
        mov = dq.popleft()
        mov.start()
    print("Qual o proximo movimento?")
    argumento = input("Colocar os valores em ordem (vx vy vtheta tempo_em_ms): ")
    listArg = argumento.split(" ")
    if len(listArg) != 4 and "" not in listArg:
        print("Comando invalido. O comando deve ter vx, vy, vtheta e tempo_em_ms seprarados por ' '")
    else:
        listArg = [float(listArg[i]) for i in range(len(listArg))]
        dq.append(Movimento(listArg[0],listArg[1],listArg[2],listArg[3]))



