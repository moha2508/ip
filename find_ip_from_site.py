import socket

def app_ip():
    get_app = str(input("enter your site web :"))   
    b = socket.gethostbyname(get_app)
    print("ip for site is :",b)
   
   
app_ip()
