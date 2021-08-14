import requests as rq

# Setting the base URL from the API
base_url = 'http://www.boredapi.com/api/activity/'

# A list of types of activity from the API
lst_type_activity = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music",
                     "busywork"]
# The price params will be a number in [0.0, 1.0]
# The participants params will be a number in [0, n]

while True:
    print('------------------------------')
    print('Activities: ')
    for activity in lst_type_activity:
        print(activity)
    print('------------------------------')

    # Forcing the user to type a activity on the list of activities
    while True:
        type_activity = str(input('What kind of activity do you want: '))
        if type_activity not in lst_type_activity:
            print('This activity is not on the list! Type something valid...')
        else:
            break
    # Forcing the user to type a price in the interval [0.0, 1.0]
    while True:
        price = float(input('How much do you want it to cost?[0.0, 1.0]'))
        if price < 0 or price > 1:
            print('Please, type a number in [0.0, 1.0]')
        else:
            break
    while True:
        participants = int(input('How much participants do you want in the activity?[1, n]'))
        if participants < 1:
            print('Please, type a number major or equal to 1')
        else:
            break
    pay_load = {'type': type_activity, 'price': price, 'participants': participants}
    
    # trying to get a pay_load with the parameters set. If it can't, an error
    # message will show up to the user
    try:
        # Requesting from the API with get method
        request = rq.get(base_url, params=pay_load)
        # Parsing the request data to json (read as dictonary)
        data = request.json()
        # Printing the data found
        print(data)
    except Exception as e:
        print(f'Ops, something went wrong')

    option = str(input('Continue?[Y/N]'))
    if option == 'N':
        break

print('Thanks for using our software :)')