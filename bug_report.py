import db_module
import datetime

database = db_module.DatabaseMaker("bug_notes")
dt = datetime.datetime.now()
current_date = dt.strftime("%Y-%m-%d %H:%M:%S")
def crete_report(current_date, ):
    bug = input("Bug: ")
    error_type = input("Error: ")
    insert_content = bug, error_type, current_date
    database.insert_into_table("ip_info", insert_content)

if __name__ == "__main__":
    create_report()
    database.end_connection()