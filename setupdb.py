import mysql.connector as ms
import json
f=open("school\\configdb.txt","r")
info=json.load(f)
conn=ms.connect(host=info['hostname'], user=info['username'], password=info['password'])
if conn.is_connected()==False:
    print("Error! Not connected to Database")
if conn.is_connected()==False:
    print("Can not connect to database")
else:
    try:
        cur=conn.cursor()
        sql="create database "+info['database']
        cur.execute(sql)
        sql="use "+info['database']
        cur.execute(sql)
        sql="""create table student(
                rno int(3) primary key,
                name varchar(30) not null,
                address varchar(30))"""
        cur.execute(sql)
        sql="""create table tc_issued(
                rno int(3) primary key,
                name varchar(30) not null,
                address varchar(30))"""
        cur.execute(sql)
        
        f=open("startapp.bat","w")
        f.write("@echo off\n")
        f.write("cls\n")
        f.write("python school\\main.py")
        f.close()
        print("Database setup is successful...")
        print("Run 'startapp' to start application...")
        input()
    except ms.Error as e:
        print(e)
        print("Quitting.......")
        input()

    finally:
        conn.close()
        
        
