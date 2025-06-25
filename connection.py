import pymysql

def connect():
    conn=pymysql.connect(
        host="localhost" , database="ml",user="root",password="shivam123"
    )
    return conn

def verifyMobile(mobile):
    if len(mobile) == 10 and mobile.isdigit():
        if mobile[0] in '6789':
            return 'Valid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'

def verifyEmail(mail):
    if '@'in mail and '.'in mail:
        return 'Valid'
    else:
        return 'Invalid'


