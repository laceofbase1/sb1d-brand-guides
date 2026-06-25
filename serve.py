import http.server, os, socketserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer(("", 4178), http.server.SimpleHTTPRequestHandler).serve_forever()
