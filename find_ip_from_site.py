import socket

def app_ip():
    get_app = str(input("enter your site web :"))   
    b = socket.gethostbyname(get_app)
    print(b)
    if get_app == int(1):
        ap = app_ip()
        print(ap)
   
   
app_ip()
