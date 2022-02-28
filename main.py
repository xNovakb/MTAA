import sipfullproxy as svf

svf.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=svf.logging.INFO,datefmt='%H:%M:%S')
svf.logging.info(svf.time.strftime("%a, %d %b %Y %H:%M:%S ", svf.time.localtime()))
svf.ipaddress = svf.sys.argv[1]
svf.recordroute = "Record-Route: <sip:%s:%d;lr>" % (svf.ipaddress,svf.PORT)
svf.topvia = "Via: SIP/2.0/UDP %s:%d" % (svf.ipaddress,svf.PORT)
server = svf.socketserver.UDPServer((svf.HOST, svf.PORT), svf.UDPHandler)
server.serve_forever()