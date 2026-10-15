from mysql.connector import connect

class ProductListCreateRetrieveUpdateDelete:
    def __init__(self,user=None,password=None):
        self.connection = connect(
            user=user,
            password=password,
            host="localhost",
            database="inventory_db"
        )
        
        self.cursor = self.connection.cursor()
        
    def post(self,**kwargs):
        keys=[k for k in kwargs.keys()]
        place_holder = ",".join(keys)
        query = f"""
        insert into product({place_holder}) values (%s,%s,%s,%s)
        """
        values = [v for v in kwargs.values()]
        
        self.cursor.execute(query,values)
        
        self.connection.commit()
        
        print("record has been added ....")
        
    def get(self):
        query = "select * from product"
        
        self.cursor.execute(query)
        
        records = self.cursor.fetchall()
        
        for r in records:
            print(r)
            
    def retrieve(self,id=None):
        query = "select * from product where id = %s"
        values=[id]
        self.cursor.execute(query,values)
        record = self.cursor.fetchone()
        print(record)
        
    def put(self,id=None,**kwargs):
        place_holder=""
        for k in kwargs.keys():
            place_holder+=k+"=%s,"
        place_holder=place_holder.rstrip(",")
        
        query=f"""
            update product set {place_holder} where id = %s
            """
        values = [v for v in kwargs.values()]
        values.append(id)
        
        self.cursor.execute(query,values)
        
        self.connection.commit()
        
        print("record updated ....")
        
    def delete(self,id=None):
        query = "delete from product where id = %s"
        
        values=[id]
        
        self.cursor.execute(query,values)
        
        self.connection.commit()
        
        print("record deleted .....")
        
        
        
        
product_instance = ProductListCreateRetrieveUpdateDelete(user="root",password="Password@123")

#product_instance.post(title="sg sports shoe",category="shoes",price=1500,rating=4.5)

# product_instance.get()

product_instance.retrieve(id=3)
product_instance.put(id=3,price=3700,rating=4.8)
product_instance.retrieve(3)

#product_instance.delete(id=2)

#product_instance.get()


"""
mobile crud
id
name
brand
specs
price
"""
