from flask import Flask, render_template, request
import db_module
import datetime
import sqlite3 as sq
import keyboard
import jinja2.exceptions

dt = datetime.datetime.now()
current_date = dt.strftime("%Y-%m-%d %H:%M:%S")
databaseName = db_module.DatabaseMaker("ip_data")

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return render_template("card_animation.html")
    except jinja2.exceptions.TemplateNotFound:
        return "SORRY ABOUT THIS THERE IS AN ISSUE RN"


@app.before_request
def log_connection():
    # getting the ip address using reques.addr
    ip_address = request.remote_addr
    
    returned_ip = check_for_ip(ip_address)
    if not returned_ip: # if record does not exist
        table_info = (ip_address, current_date)
    else:
        # Insert ip address and timestamp
        databaseName.insert_into_table("ip_info", table_info)
   
        
def check_for_ip(ip_address):
    sql_command = f"FROM * ip_info WHERE column = '{ip_address}';"
    returned_ip = databaseName.check_values(sql_command)
    return returned_ip
    

if __name__ == "__main__":
    app.config.update(
        TEMPLATE_FOLDER ='templates'
    )
    app.run()