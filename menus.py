import mysql.connector as ms
import json
import pandas as pd
def main_menu():
    print("**************************************************")
    print("           ADMISSION DATABASE                     ")
    print("**************************************************")
    print()
    print("MAIN MENU:")
    print()
    print("1-Student's Registration")
    print("2-Search Student")
    print("3-Issue TC")
    print("4-Display TC")
    print("5-Display Student List")
    print("6-Exit")
    print("**************************************************")
    ch=input("Enter your choice(1,2,3,4,5 or 6)?")
    return ch

def search_stu():
    print("**************************************************")
    print("           ADMISSION DATABASE                     ")
    print("**************************************************")
    print()
    print("STUDENT SEARCH MENU:")
    print()
    print("1-Search by Name")
    print("2-Search by Registration Number")
    print("**************************************************")
    ch=input("Enter your choice(1 or 2)?")
    if ch=='1':
        print("Search by Name")
        #search_by_name()

        f=open("school\\configdb.txt","r")
        info=json.load(f)
        conn=ms.connect(host=info['hostname'], user=info['username'], password=info['password'], database=info['database'])
        if conn.is_connected()==False:
            print("Error! Not connected to Database")
        else:
            cur=conn.cursor()
            nm=input("Enter name of student: ")
            sql="select * from student where name like '%{}%'".format(nm)
            cur.execute(sql)
            rs=cur.fetchall()
            r={"rno":[],"name":[],"address":[]}
            for row in rs:
                r["rno"].append(row[0])
                r["name"].append(row[1])
                r["address"].append(row[2])
            df=pd.DataFrame(r)
            print(df)
            print("Total records: ", cur.rowcount)
            conn.close()
    elif ch=='2':
        print("Search by Registration Number")
        #search_by_reg()
        f=open("school\\configdb.txt","r")
        info=json.load(f)
        conn=ms.connect(host=info['hostname'], user=info['username'], password=info['password'], database=info['database'])
        if conn.is_connected()==False:
            print("Error! Not connected to Database")
        else:
            cur=conn.cursor()
            rno=input("Enter roll number of student: ")
            sql="select * from student where rno={}".format(rno)
            cur.execute(sql)
            rs=cur.fetchall()
            r={"RNO":[],"NAME":[],"ADDRESS":[]}
            for row in rs:
                r["RNO"].append(row[0])
                r["NAME"].append(row[1])
                r["ADDRESS"].append(row[2])
            df=pd.DataFrame(r)
            print(df)
            print("Total records: ", cur.rowcount)
            conn.close()

def registration():
    print("**************************************************")
    print("           ADMISSION DATABASE                     ")
    print("**************************************************")
    print()
    print("STUDENT'S REGISTRATION:")
    f=open("school\\configdb.txt","r")
    info=json.load(f)
    conn=ms.connect(host=info['hostname'], user=info['username'], password=info['password'], database=info['database'])
    if conn.is_connected()==False:
        print("Error! Not connected to Database")
    else:
        cur=conn.cursor()
    while True:
        ch=input("Do you want more(y/n)?")
        if ch!='y':
            break
        rno=input("Enter roll no: ")
        name=input("Enter name: ")
        address=input("Enter address: ")
        sql="insert into student(rno, name, address) "\
            "values('{}','{}','{}')".format(rno, name, address)
        cur.execute(sql)
        
    conn.commit()
    cur.execute("select * from student")
    rs=cur.fetchall()
    r={"RNO":[],"NAME":[],"ADDRESS":[]}
    for row in rs:
        r["RNO"].append(row[0])
        r["NAME"].append(row[1])
        r["ADDRESS"].append(row[2])
    df=pd.DataFrame(r)
    print(df)
    conn.close()


def issue_tc():
    print("**************************************************")
    print("           ADMISSION DATABASE                     ")
    print("**************************************************")
    print()
    print("ISSUE TC:")
    f=open("school\\configdb.txt","r")
    info=json.load(f)
    conn=ms.connect(host=info['hostname'], user=info['username'], password=info['password'], database=info['database'])
    if conn.is_connected()==False:
        print("Error! Not connected to Database")
    else:
        cur=conn.cursor()
        rn=input("Enter roll number to issue TC:")
        sql="select * from student where rno={}".format(rn)
        cur.execute(sql)
        rs=cur.fetchone()
        sql="insert into tc_issued(rno,name,address) values('{}','{}','{}')".format(rs[0],rs[1],rs[2])
        cur.execute(sql)
        sql="delete from student where rno={}".format(rn)
        cur.execute(sql)
        conn.commit()
        print("TC Issued...successfully")

def display():
    print("**************************************************")
    print("           ADMISSION DATABASE                     ")
    print("**************************************************")
    print()
    print("LIST OF STUDENTS:")
    f=open("school\\configdb.txt","r")
    info=json.load(f)
    conn=ms.connect(host=info['hostname'], user=info['username'], password=info['password'], database=info['database'])
    if conn.is_connected()==False:
        print("Error! Not connected to Database")
    else:
        cur=conn.cursor()
        sql="select * from student"
        cur.execute(sql)
        rs=cur.fetchall()
        r={"RNO":[],"NAME":[],"ADDRESS":[]}
        for row in rs:
            r["RNO"].append(row[0])
            r["NAME"].append(row[1])
            r["ADDRESS"].append(row[2])
        df=pd.DataFrame(r)
        print(df)
        print("Total records: ", cur.rowcount)
        conn.close()            


def disp_tc():
    print("**************************************************")
    print("           ADMISSION DATABASE                     ")
    print("**************************************************")
    print()
    print("LIST OF TC ISSUED STUDENTS:")
    f=open("school\\configdb.txt","r")
    info=json.load(f)
    conn=ms.connect(host=info['hostname'], user=info['username'], password=info['password'], database=info['database'])
    if conn.is_connected()==False:
        print("Error! Not connected to Database")
    else:
        cur=conn.cursor()
        sql="select * from tc_issued"
        cur.execute(sql)
        rs=cur.fetchall()
        r={"RNO":[],"NAME":[],"ADDRESS":[]}
        for row in rs:
            r["RNO"].append(row[0])
            r["NAME"].append(row[1])
            r["ADDRESS"].append(row[2])
        df=pd.DataFrame(r)
        print(df)
        print("Total tc issued: ", cur.rowcount)
        conn.close()            
