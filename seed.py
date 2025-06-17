from server.app import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    pizza1 = Pizza(name="BBQ", ingredients="Tomato, Meat, Bacon")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Pepperoni")

    restaurant1 = Restaurant(name="Pizza in", address="123 Galleria karen")
    restaurant2 = Restaurant(name="Dominos", address="456 Hub karen")

    rp1 = RestaurantPizza(price=10, restaurant=restaurant1, pizza=pizza1)
    rp2 = RestaurantPizza(price=12, restaurant=restaurant2, pizza=pizza2)

    db.session.add_all([pizza1, pizza2, restaurant1, restaurant2, rp1, rp2])
    db.session.commit()

    print("Seeded")
