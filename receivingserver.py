from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        text_received = post_data.decode('utf-8')
        print(text_received)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"got them text")
    
    def log_message(self, format, *args):
        # Override to suppress default logging
        pass

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f"starting server on port {port}...")
    print("failed messages incoming:")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopping server")
        httpd.server_close()

if __name__ == '__main__':
    run_server()