from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>This pc</title>
    </head>
    <body>
           <h1>Device specification-25017628</h1>
        <table border="3" cellspacing="5" cellspacing="5">
            <tr>
                <td>S.no</td>
                <td>Device name</td>
                <td>Description</td>
            </tr>
            <tr>
                <td>1</td>
                <td>TMP215-75-G2</td>
                <td>Intel(R)Core(TM)ULTRA 5 125H (1.20GHz)
            </tr>
            <tr>
                <td>2</td>
                <td>RAM</td>
                <td>16.00 GB (15.5 GB usable)</td>
            </tr> 
            <tr>
                <td>2</td>
                <td>RAM</td>
                <td>(16.00 GB usable)</td>
            </tr>   


        </table>

    </body>    
</html>
    
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()