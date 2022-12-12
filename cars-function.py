def make_car(manufacturer,model_name,**description):
    car_info = {}

    # storing values in dictionary
    car_info["Manufacturer"] = manufacturer
    car_info["Model name"] = model_name

    # storing arbitary key arguments in dictionary
    for key, values in description.items():
        car_info[key] = values
    return car_info

car  = make_car('Toyota','Corolla',color = 'White',bodyfitnes = 'Good') #calling the function

print(car) # print the function