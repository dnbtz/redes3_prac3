import rrdtool
from Notify import send_alert_attached


def graphTCP():
    ultima_lectura = int(rrdtool.last("trendTCP.rrd"))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 600

    ret = rrdtool.graphv( "deteccionTCP.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=TCP load",
                        '--lower-limit', '0',
                        '--upper-limit', '2',
                         "DEF:cargaTCP=trendTCP.rrd:TCPload:AVERAGE",

                         "CDEF:umbral30=cargaTCP,1.7,LT,0,cargaTCP,IF",
                         "VDEF:cargaMAX=cargaTCP,MAXIMUM",
                         "VDEF:cargaMIN=cargaTCP,MINIMUM",
                         "VDEF:cargaSTDEV=cargaTCP,STDEV",
                         "VDEF:cargaLAST=cargaTCP,LAST",
                         "AREA:cargaTCP#00FF00:Carga del TCP",
                         "AREA:umbral30#FF9F00:Carga TCP mayor que maxbw",
                         "HRULE:1.7#00FF00:Umbral 1",
                         "PRINT:cargaLAST:%6.2lf %SLAst",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )
