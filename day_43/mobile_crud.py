from mysql.connector import connect

class MobileListCreateRetrieveUpdateDelete:
    
    def __init__(self,user=None,password=None):
        
        self.connection = connect(
            user=user,
            password=password,
            host="localhost",
            database = "mobile_db"
        )
        
        
        self.cursor = self.connection.cursor()
        
    def post(self,name=None,brand=None,specs=None,price=None,rating=None):
        query = """
        insert into mobile(name,brand,specs,price,rating) values (%s,%s,%s,%s,%s)
        """
        values = [name,brand,specs,price,rating]
        
        self.cursor.execute(query,values)
        
        self.connection.commit()
        
        print("mobile added.....")
        
    def get(self):
        query="select * from mobile"
        
        self.cursor.execute(query)
        
        records=self.cursor.fetchall()
        
        for r in records:
            print(r)
            
    def retrieve(self,id=None):
        query = "select * from mobile where id=%s"
        values=[id]
        self.cursor.execute(query,values)
        record = self.cursor.fetchone()
        print(record)
        
    def put(self,id=None,price=None,rating=None):
        query = "update mobile set price=%s,rating=%s where id = %s"
        values=[price,rating,id]
        self.cursor.execute(query,values)
        self.connection.commit()
        print("mobile updated ....")
        
    def delete(self,id=None):
        query="delete from mobile where id=%s"
        values=[id]
        self.cursor.execute(query,values)
        self.connection.commit()
        print("mobile deleted ......")
        
mobile_instance = MobileListCreateRetrieveUpdateDelete(user="root",password="Password@123")

# mobile_instance.post(name="i phone 18 pro",brand="apple",specs="12gb-512gb",price=80000,rating=4.2)
        
#mobile_instance.get()

# mobile_instance.retrieve(id=2)

# mobile_instance.put(id=2,price=90000,rating=4)

# mobile_instance.retrieve(id=2)

# mobile_instance.delete(id=2)

mobile_instance.get()
