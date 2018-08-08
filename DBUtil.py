import pymysql

def getcon():
    conn=pymysql.Connect("localhost","root","root","pymydql")
    return conn
def execute(sql):
    conn=getcon()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        date=cur.fetchone()
        return date
    except Exception:
        conn.rollback()
    conn.close()
    
