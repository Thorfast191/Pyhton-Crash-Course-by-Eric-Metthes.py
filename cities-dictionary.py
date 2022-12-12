# creating a dictionary called  cities
cities = {
    'Dhaka':{  # dictionary in a dictionary
        'type': 'Capital',
        'country': 'Bangladesh',
        'population': '15 millions'
    },
    'Chittagong':{
        'type': 'Division',
        'country': 'Bangladesh',
        'population': '10 millions'
    },
    'Sylhet':{
        'type': 'Division',
        'country': 'Bangladesh',
        'population': '8 millions'
    }
}

# using a for loop to print
for k,n in cities.items():
    print(k+str(n))
