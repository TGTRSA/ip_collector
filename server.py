from wsgiref.simple_server import make_server
from flask import request
from app import app
import jinja2
import keyboard
#import datetime
#import subprocess
#import db_module

#dt = datetime.datetime.now()
#current_date = dt.strftime("%Y-%m-%d %H:%M:%S")
#databaseName = db_module.DatabaseMaker("ip_collector")

def run_server(DEFAULT_IP, port):
    httpd = make_server(DEFAULT_IP, port, app.wsgi_app)
    
    print("Serving web page on invisble port...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Closing server")
    except jinja2.exceptions.TemplateSyntaxError:
        print("Closing server...")
        httpd.close_request()
    
        
        


    
if __name__ == "__main__":
    DEFAULT_IP = '192.168.1.60'
    run_server(DEFAULT_IP, 1835)