# creating a function to describe city
def city_country(city,country):
    des_city = city + " is in " + country
    return des_city # returning the value

description = city_country("Dhaka","Bangladesh")
print(description)