from mysql.connector import connect

class AssesPro:
    def __init__(self,user=None,password=None):
        self.connection = connect(
            user=user,
            password=password,
            host="localhost",
            database="assesment_db"
        )
        self.cursor = self.connection.cursor()
    
    def post(self,**kwargs):
        keys=[k for k in kwargs.keys()]
        place_holder=",".join(keys)
        query = f"""
                insert into assesment ({place_holder}) values (%s,%s,%s,%s)
                """
        values = [v for v in kwargs.values()]
        
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record added")
        
    def put(self,id=None,**kwargs):
        place_holder=""
        
        for k in kwargs.keys():
            place_holder+=k+"=%s,"
            
        place_holder = place_holder.rstrip(",")
            
        query=  f"""
                update assesment set {place_holder} where id=%s
                """
        
        values = [v for v in kwargs.values()]
        
        values.append(id)
        
        self.cursor.execute(query,values)
        
        self.connection.commit()
        print("record updated successfully")
        
    def get(self):
        query = "select * from assesment"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        for r in records:
            print(r)
            
    def retrieve(self,id=None):
        query = "select * from assesment where id=%s"
        values=[id]
        self.cursor.execute(query,values)
        record=self.cursor.fetchone()
        print(record)
        
        
        
asses_instance = AssesPro(user="root",password="Password@123")

# asses_instance.post(title="mysql_main_exam",batch="djangoAug",start_date="2026-10-30",duration=2)

# asses_instance.get()

asses_instance.retrieve(id=2)
asses_instance.put(id=2,start_date="2026-10-15")
asses_instance.retrieve(id=2)