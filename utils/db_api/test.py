from sqlite import Database

db = Database()

def test():
    db.create_table_applys()
    orders = db.get_all_applys()
    print("Do dobavleniya: " + str(orders))



    orders = db.get_all_applys()
    print("Posle: " + str(orders))

def test2():
    db.create_table_price()
    db.add_price("assss", "sasa")
    price = db.get_price()
    print("Do dobavleniya: " + str(price))

    db.update_price("asfasfa", "12.12.12", 1)

    price = db.get_price()
    print("Posle: " + str(price))


test()
test2()

