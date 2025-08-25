from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''

<!DOCTYPE html>
<html>
<head>
    <title>College Details</title>
</head>
<body>
    <table border="5" align="center" cellspacing="20" cellpadding="20" bgcolor="red">
        <caption><b>Department Information</b></caption>
        <tr bgcolor="blue">
            <th>S.No</th>
            <th>Name of the layer</th>
            <th>Name of the protocol</th>
        </tr>
        <tr bgcolor="green">
            <td>1</td>
            <td>application layer</td>
            <td>HTTP,FTP,DNS,Telnet,SSH</td>
        </tr>
        <tr bgcolor="yellow">
            <td>2</td>
            <td>Transport Layer</td>
            <td>TCP/UDP</td>
        </tr>
        <tr bgcolor="white">
            <td>3</td>
            <td>Network Layer</td>
            <td>IPV4/IPv6</td>
        </tr>
        <tr bgcolor="pink">
            <td>3</td>
            <td>Link Layer</td>
            <td>Ethernet</td>
        </tr>
    </table>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()