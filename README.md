# EX01 Developing a Simple Webserver
## Date:05/09/2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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

```

## OUTPUT:
![alt text](<Screenshot (22)-1.png>)
![alt text](<Screenshot (23)-1.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
