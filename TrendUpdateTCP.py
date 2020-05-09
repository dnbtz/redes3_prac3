import time
import rrdtool
from getSNMP import consultaSNMP
from trendGraphDetection import graphTCP
import _thread
from Notify import send_alert_attached
maxbw = 0
#1.3.6.1.2.1.6.10.0 entrada
#1.3.6.1.2.1.6.11.0 salida


def TCP(com,ip):
    bandera = 0
    t = 60
    while 1:
        entrada = int(consultaSNMP(com,ip,'1.3.6.1.2.1.6.10.0'))
        #print(entrada)
        salida = int(consultaSNMP(com, ip, '1.3.6.1.2.1.6.11.0'))
        #print(salida)
        maxbw = entrada / salida
        valor = "N:" + str(maxbw)
        print(valor)
        rrdtool.update('trendTCP.rrd', valor)
        rrdtool.dump('trendTCP.rrd','trendTCP.xml')
        graphTCP()
        if bandera == 0:
            if maxbw > 1.7:
                #_thread.start_new_thread(send_alert_attached, ("Sobrepasa Umbral TCP", 'TCP'))
                bandera = 1
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)