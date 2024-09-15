import db_module
import datetime

database = db_module.DatabaseMaker("bug_notes")
#server_data = db_module.DatabaseMaker("server_data")
table_content = "bug TEXT NOT NULL, error_type TEXT,timestamp DATETIME CURRENT_TIMESTAMP"
dt = datetime.datetime.now()
current_date = dt.strftime("%Y-%m-%d %H:%M:%S")
database.create_table("bug_report",table_content)
#insert_content = "12456663", current_date
#database.insert_into_table("ip_info", insert_content)

database.end_connection()