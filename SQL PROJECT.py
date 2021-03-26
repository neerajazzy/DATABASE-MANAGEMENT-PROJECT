import os
import mysql.connector
import datetime

print('''\n\t\t\t--- HEY USER, WELCOME TO i MUSIC INSTITUTE MANAGEMENT SYSTEM ---\n''')
user=input('Enter Your SQL User : ')
pw=input('Enter Your SQL Password : ')

#preparatory processes
def setup_database():
        cmd='create database if not exists iMusic;'
        cursor.execute(cmd)
        print('Database Created...\n')
        
        cmd='use imusic;'
        cursor.execute(cmd)
        print('Database Changed/Selected...\n')
        
        cmd='create table if not exists Learners(sid varchar(4) primary key,sname char(30) not null,genre varchar(30),phone char(10),area varchar(30));'
        cursor.execute(cmd)
        print('Learners Table Created...\n')

        cmd='create table if not exists Staff(staff_id varchar(4),staff_name varchar(30) not null,Designation varchar(30) not null,date_of_join date not null,salary int(5) not null);'
        cursor.execute(cmd)
        print('Staff Table Created...\n')
        
        cmd='create table if not exists ResourcesIssued(sid varchar(4) not null,rname varchar(30) not null,issue_date date,rid varchar(4) not null);'
        cursor.execute(cmd)
        print('ResourcesIssued Table Created...\n')

        cmd='create table if not exists ResourcesAvailable(rid varchar(4) primary key,r_name varchar(30) not null,available int(3) not null,issued int(3) not null);'
        cursor.execute(cmd)
        print('ResourceAvailable Table Created...\n')

        

def raw_insert():
        #learners
        a="insert into learners values('101','Neeraj','HipHop','7008674318','Palam');"
        b="insert into learners values('102','Suraj','Jazz','7908674312','Manglapuri');"
        c="insert into learners values('103','Dhiraj','Rock','8608431765','Dwarka');"
        d="insert into learners values('104','Damini','Rock','9758423316','Shankar Vihar');"
        e="insert into learners values('105','Kamlesh','Classical','9435104652','Dwarka');"
        
        cursor.execute(a)
        cursor.execute(b)
        cursor.execute(c)
        cursor.execute(d)
        cursor.execute(e)

        #staff
        f="insert into staff values('101','Raju','Instructor','2020-02-02',25000);"
        g="insert into staff values('102','Surya','Manager','2018-05-21',45000);"
        h="insert into staff values('103','Dhirendar','Receptionist','2019-07-30',22500);"
        i="insert into staff values('104','Dhamu','Peon','2021-01-31',12000);"
        j="insert into staff values('105','Kaleen','Instructor','2020-06-22',26000);"

        cursor.execute(f)
        cursor.execute(g)
        cursor.execute(h)
        cursor.execute(i)
        cursor.execute(j)
        
        #resourcesissued
        k="insert into ResourcesIssued values('101','Flute','2021-02-01','1');"
        l="insert into ResourcesIssued values('104','Guitar','2021-01-27','2');"
        m="insert into ResourcesIssued values('101','Flute Basics By Jonhard','2021-02-01','3');"
        n="insert into ResourcesIssued values('104','Next Level : Guitarist','2021-01-27','4');"
        o="insert into ResourcesIssued values('103','Mouth-Organ Basics','2020-10-21','5');"

        cursor.execute(k)
        cursor.execute(l)
        cursor.execute(m)
        cursor.execute(n)
        cursor.execute(o)

        #resourcesavailable
        p="insert into ResourcesAvailable values ('1','Flute',26,12)"
        q="insert into ResourcesAvailable values ('2','Guitar',24,2)"
        r="insert into ResourcesAvailable values ('3','Flute Basics By Jonhard',21,31)"
        s="insert into ResourcesAvailable values ('4','Next Level : Guitarist',26,12)"
        t="insert into ResourcesAvailable values ('5','Mouth-Organ Basics',21,7)"
        u="insert into ResourcesAvailable values ('6','Casio Small',21,0)"
        v="insert into ResourcesAvailable values ('7','Veena',25,0)"
        w="insert into ResourcesAvailable values ('8','Harmonium',10,0)"

        cursor.execute(p)
        cursor.execute(q)
        cursor.execute(r)
        cursor.execute(w)
        cursor.execute(s)
        cursor.execute(t)
        cursor.execute(u)
        cursor.execute(v)
        
        
        temp_conn.commit()

#temporary connection to setup database
temp_conn=mysql.connector.connect(host='localhost',user=user,passwd=pw,charset='utf8')
cursor=temp_conn.cursor()
ask=input('Press 1 To Setup Database If Logining First Time Else Press Other Key : ')
if ask=='1':
        setup_database()
        print('Database Is Now Ready To Use')
        raw_insert()
        print('Data Inserted In Respective Tables')
temp_conn.close()


#main
mydb=mysql.connector.connect(host='localhost',user=user,passwd=pw,database='iMusic',charset='utf8')
cursor=mydb.cursor()
check_conn=mydb.is_connected()
try:
        if check_conn==True:
                print('\nConnection Established..')
except Exception as error:
                print(error)
        
def show_tables():
        cmd='show tables;'
        cursor.execute(cmd)
        rec=cursor.fetchall()
        print('Table Inside iMusic Database')
        print('-----------------------------')
        for table in rec:
                print(table[0])
                
def table_schema():
        tablename=int(input('To Know The Structure(Schema), Press\n1. For Learners Table\n2. For ResourcesIssued Tables\n3. For ResourcesAvailable Table\n4. For Staff Tables\nEnter Your Choice : '))

        if tablename==1:
                cmd='desc learners;'
                
        elif tablename==2:
                cmd='desc resourcesissued;'
                
        elif tablename==3:
                cmd='desc resourcesavailable;'

        elif tablename==4:
                cmd='desc staff;'
                
        else:
                print('Invalid Input')
        
        cursor.execute(cmd)
        rec=cursor.fetchall()
        l=['Field',' Type','Null','Key','Default','Extra']
        for i in rec:
                dic={l[0]:i[0],l[1]:i[1],l[1]:i[2],l[3]:i[3],l[4]:i[4],l[5]:i[5]}
                print(dic)
                
def add_learner():
        sid=input('Enter Learner ID : ')
        sname=input('Enter Learner Name : ')
        genre=input('Enter Genre Choosed For Learning : ')
        phone=input('Enter Phone Number : ')
        area=input('Enter Your Locality Name : ')
        
        cmd='insert into learners values("{}","{}","{}","{}","{}")'.format(sid,sname,genre,phone,area)
        cursor.execute(cmd)
        
        mydb.commit()
        print('Data Added..')

def add_staff():
        sid=input('Enter Staff ID : ')
        sname=input('Enter Staff Name : ')
        des=input('Enter Designation : ')
        doj=str(datetime.date.today())
        sal=int(input('Enter Salary : '))
        
        cmd='insert into staff values("{}","{}","{}","{}",{})'.format(sid,sname,des,doj,sal)
        cursor.execute(cmd)
        
        mydb.commit()
        print('Data Added..')

def show_learners():
        while True:
                try:
                        print('1. Single Record Show By Sid\n2. List Learners Name Wise\n3. List Learners Genre Wise\n4. List Learners By Area\n5. Show All\n Another Numeric Key To Back Menu')
                        choose=int(input('Enter Your Choice : '))
                        
                        if choose==1:
                                sid=input('Enter Learner ID To Show Record : ')
                                
                                cmd='select * from learners where sid="{}"'.format(sid)
                                cursor.execute(cmd)
                                
                        elif choose==2:
                                sname=input('Enter Name To Show Record(s) : ')
                                
                                cmd='select * from learners where sname="{}"'.format(sname)
                                cursor.execute(cmd)

                        elif choose==3:
                                genre=input('Enter Genre To Show Record(s)')
                                
                                cmd='select * from learners where genre="{}"'.format(genre)
                                cursor.execute(cmd)

                        elif choose==4:
                                area=input('Enter Area To Show Record(s)')
                                
                                cmd='select * from learners where area="{}"'.format(area)
                                cursor.execute(cmd)

                        elif choose==5:
                                cmd='select * from learners;'
                                cursor.execute(cmd)
                                 
                        else:
                                break
                        
                except Exception as error:
                        print(error)

                rec=cursor.fetchall()
                if rec==[]:
                        print('No result Set')
                else:
                        l=['sid','sname','genre','phone','area']
                        for i in rec:
                                dic={l[0]:i[0],l[1]:i[1],l[2]:i[2],l[3]:i[3],l[4]:i[4]}
                                print(dic)

def show_staff():
        while True:
                try:
                        print('1. Single Record Show By Sid\n2. List Staff Name Wise\n3. List Staff Designation Wise\n4. List Staff Salary Wise\n5. List Staff By Date Of Join\n6. Show All\n Another Numeric Key To Back Menu')
                        choose=int(input('Enter Your Choice : '))
                        
                        if choose==1:
                                s_id=input('Enter Staff ID To Show Record : ')
                                
                                cmd='select * from staff where staff_id="{}"'.format(s_id)
                                cursor.execute(cmd)
                              
                        elif choose==2:
                                s_name=input('Enter Name To Show Record(s) : ')
                                
                                cmd='select * from staff where staff_name="{}"'.format(s_name)
                                cursor.execute(cmd)

                        elif choose==3:
                                des=input('Enter Designation To Show Record(s)')
                                
                                cmd='select * from staff where Designation="{}"'.format(des)
                                cursor.execute(cmd)
                              
                        elif choose==4:
                                sal=int(input('Enter Salary To Show Record(s)'))
                                
                                cmd='select * from staff where salary={}'.format(sal)
                                cursor.execute(cmd)
                                
                        elif choose==5:
                                date=input('Enter Date In Format(YYYY-MM-DD) To Show Record(s)')
                                
                                cmd='select * from staff where Date_of_join="{}"'.format(date)
                                cursor.execute(cmd)
                                
                        elif choose==6:
                                cmd='select * from staff;'
                                cursor.execute(cmd)
                                
                        else:
                                break
                        
                except Exception as error:
                        print(error)
                        
                rec=cursor.fetchall()
                if rec==[]:
                        print('No result Set')
                else:
                        l=['staff_id','staff_name','Designation','date_of_join','salary']
                        for i in rec:
                                dic={l[0]:i[0],l[1]:i[1],l[1]:i[2],l[3]:i[3],l[4]:i[4]}
                                print(dic)
               
def update_learner():
        try:
                sid=input('Enter Learner ID To Update : ')
                sname=input('Enter Learner Name : ')
                genre=input('Enter Genre Choosed For Learning : ')
                phone=input('Enter Phone Number : ')
                area=input('Enter Your Locality Name : ')
                
                cmd='update learners set sname="{}",genre="{}",phone="{}",area="{}" where sid="{}"'.format(sname,genre,phone,area,sid)
                cursor.execute(cmd)
                
                mydb.commit()
                print('Data Updated...')
                
        except Exception as error:
                print(error)

def update_staff():
        try:
                sid=input('Enter Staff ID To Update : ')
                sname=input('Enter Staff Name : ')
                des=input('Enter Designation : ')
                sal=int(input('Enter Salary Number : '))
                doj=input('Enter Date Of Join (YYYY-MM-DD) : ')
                
                cmd='update staff set staff_name="{}",des="{}",sal={},doj="{}" where staff_id="{}"'.format(sname,des,sal,doj,sid)
                cursor.execute(cmd)
                
                mydb.commit()
                print('Data Updated...')
                
        except Exception as error:
                print(error)

def delete_learner():
        
        sid=input('Enter Learner ID To Delete : ')
        cmd='delete from learners where sid="{}"'.format(sid)
        cursor.execute(cmd)
        
        mydb.commit()
        print('Data Deleted...')

def delete_staff():
        sid=input('Enter Staff ID To Delete : ')
        
        cmd='delete from Staff where staff_id="{}"'.format(sid)
        cursor.execute(cmd)
        
        mydb.commit()
        print('Data Deleted...')

def issue_new():
        sid=input('Enter Learner ID : ')
        rname=input('Enter Resource Name : ')
        date=str(datetime.date.today())
        rid=input('Enter Resource ID : ')
        
        check_cmd='select available from resourcesavailable where rid="{}"'.format(rid)
        cursor.execute(check_cmd)
        rec=cursor.fetchall()
        if rec==0:
                print('All Resources Are Issued To Other Learners')
        else:
                cmd='insert into resourcesissued values("{}","{}","{}","{}")'.format(sid,rname,date,rid)
                cursor.execute(cmd)

                cmd='update resourcesavailable set available=available-1,issued=issued+1 where rid="{}"'.format(rid)
                cursor.execute(cmd)
                
        mydb.commit()
        print('Resource Issued..')

def show_given_resources():
        print('This Are The Detail Of Resources Issued & Issuer')
        cmd='select * from resourcesissued;'
        cursor.execute(cmd)
        rec=cursor.fetchall()
        l=['SID','Rname','Date','RID']
        for i in rec:
                print({l[0]:i[0],l[1]:i[1],l[2]:i[2],l[3]:i[3]})

def resources_return():
        sid=input('Enter Learner ID To Collect : ')
        rid=input('Enter RID(Of The Collecting Resource) : ')
        check_cmd='select issued from resourcesavailable where rid="{}"'.format(rid)
        cursor.execute(check_cmd)
        rec=cursor.fetchall()
        if rec==0:
                print('You Can\'t Collect Resources That Are Not Yet Issued OR Not Belong To Institute')
        else:
                cmd='delete from resourcesissued where sid="{}" and rid="{}"'.format(sid,rid)
                cursor.execute(cmd)

                cmd='update resourcesavailable set available=available+1,issued=issued-1 where rid="{}"'.format(rid)
                cursor.execute(cmd)
        
        mydb.commit()
        print('Resource Collected(Submitted)...')

def show_avail_res():
        cmd='Select * from resourcesavailable;'
        cursor.execute(cmd)
        rec=cursor.fetchall()
        l=['RID','Rname','Available','Issued']
        for i in rec:
                print({l[0]:i[0],l[1]:i[1],l[2]:i[2],l[3]:i[3]})
        mydb.commit()

def add_resource():
        rid=input('Enter RID : ')
        res_name=input('Enter Resource Name : ')
        add_qty=int(input('Enter Adding Quantity : '))
        iss_qty=0
        cmd="insert into ResourcesAvailable values ('8','Harmonium',10,0)"
        cursor.execute(cmd)
        mydb.commit()
        print('Resource Added..')

def update_resource():
        while True:
                print('1. Reduce Quantity \n2. Increase Quantity \n3. Remove Old Resources \n4. Any Other Key To Back Menu')
                select=input('Enter Your Choice : ')
                if select=='1':
                        rid=input('Enter RID To Reduction : ')
                        n=int(input('Enter The Reduction Quantity : '))
                        cmd='Select * from resourcesavailable where rid="{}"'.format(rid)
                        cursor.execute(cmd)
                        rec=cursor.fetchall()
                        flag=False
                        for i in range(n):
                                if rec[0][2]==0:
                                        print('Reduction Denied : Available Quantity Reached 0')
                                        break
                                else:
                                        cmd='update resourcesavailable set available=available-1 where rid="{}"'.format(rid)
                                        cursor.execute(cmd)
                                        mydb.commit()
                                        flag=True
                        if flag==True:
                                print('Quantity Reduced')
                                
                elif select=='2':
                        rid=input('Enter RID For Increment : ')
                        n=int(input('Enter Increment Quantity : '))
                        for i in range(n):
                                cmd='update resourcesavailable set available=available+1 where rid="{}"'.format(rid)
                                cursor.execute(cmd)
                                mydb.commit()
                        print('Quantity Increased')

                elif select=='3':
                        rid=input('Enter RID To Delete Resources : ')
                        cmd='delete from resourcesavailable where rid="{}"'.format(rid)
                        cursor.execute(cmd)
                        mydb.commit()
                        print('Record Of old Resource Is Deleted')

                else:
                        break
                
def learners():
        while True:
                print('1. Add New Learner\n2. Show Learners\n3. Update Learner\n4. Delete Learner\n5. Key To Back Menu')
                choose=int(input('Enter Your Choice : '))
                
                if choose==1:
                        add_learner()
                        
                elif choose==2:
                        show_learners()
                        
                elif choose==3:
                        update_learner()
                        
                elif  choose==4:
                        delete_learner()
                        
                elif choose==5:
                        break
                else:
                        print('Choose Valid Option')
def  staff():
        while True:
                print('1. Add New Staff\n2. Show Staff\n3. Update Staff\n4. Delete Staff\n5. To Back Menu')
                choose=int(input('Enter Your Choice : '))
                
                if choose==1:
                        add_staff()
                        
                elif choose==2:
                        show_staff()
                        
                elif choose==3:
                        update_staff()
                        
                elif  choose==4:
                        delete_staff()
                        
                elif choose==5:
                        break

                else:
                        print('Choose Valid Option')

def resources_issued():
        while True:
                print('1. Issue Resource\n2. Show Given Resources\n3. Collect Resource Issued\nAny Other Numeric Key To Back Menu')
                choose=int(input('Enter Your Choice : '))
                
                if choose==1:
                        issue_new()
                        
                elif choose==2:
                        show_given_resources()
                        
                elif choose==3:
                        resources_return()

                else:
                        break

def resources_avail():
        while True:
                print('Press \n1. For Add New Resource\n2. For Update Quantity Of Resource\n3. For Show Available Resources\nAny Other Key To Back Menu')
                select=input('Enter Your Choice : ')
                
                if select=='1':
                        add_resource()
                        
                elif select=='2':
                        update_resource()
                        
                elif select=='3':
                        show_avail_res()
                        
                else:
                        break

def tables():
        while True:
                print('Press Key For Work On Table\n1. Learners\n2. Staff\n3. Resources Issued \n4. Resources Available \nAny Other Key To Back Menu')
                select=input('Enter Your Choice : ')
                
                if select=='1':
                        learners()
                        
                elif select=='2':
                        staff()
                        
                elif select=='3':
                        resources_issued()

                elif select=='4':
                        resources_avail()
                        
                else:
                        break
        
def caller():        
        while True:
                print('\n1. Show Tables Inside Database\n2. Show Schema Of Tables\n3. Work On Tables\n4. To Exit.')

                ask=input('\nEnter Your Choice : ')
                
                if ask=='1':
                        show_tables()
                        
                elif ask=='2':
                        table_schema()
                        
                elif ask=='3':
                        tables()
                        
                elif ask=='4':
                        break

                else:
                        print('Choose Valid Option')
caller()
mydb.close()
