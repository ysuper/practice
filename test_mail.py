import socket, ssl, datetime


def check_ssl(hostname, port):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 3 second timeout because Lambda has runtime limitations
    conn.settimeout(3.0)
    conn.connect((hostname, port))
    ssl_info = conn.getpeercert()
    # parse the string from the certificate into a Python datetime object
    expirationDate = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
    now = datetime.datetime.now()
    delta = expirationDate - now
    return delta


print(check_ssl('www.automodules.com', 443))
