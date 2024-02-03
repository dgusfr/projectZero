from http.server import BaseHTTPRequestHandler, HTTPServer
import json

usuarios = {
    "diego": "123",
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head><title>Servidor Python</title></head><body><h1>Servidor Python em execução!</h1></body></html>'.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Endpoint não encontrado'.encode('utf-8'))

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            if data['username'] in usuarios and usuarios[data['username']] == data['password']:
                token = 'token_de_autenticacao_gerado_pelo_servidor'
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'token': token}).encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Credenciais inválidas'}).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Endpoint não encontrado'.encode('utf-8'))

def run():
    print('Iniciando servidor...')
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Servidor rodando na porta 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
