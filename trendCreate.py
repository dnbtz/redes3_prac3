import rrdtool


def createTCP(nom):
    ret2 = rrdtool.create(nom+".rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:TCPload:GAUGE:600:U:U",
                         "RRA:AVERAGE:0.5:1:24")
    if ret2:
        print(rrdtool.error())
