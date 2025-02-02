#!/usr/bin/env python3

'''
dictionary holds key value pairs: 
1. key identifier (can be of any data type)
2. corresponding value (can be of any data type)

eg: a phone book
- key = names of people
- value = corresponding names
'''

# creating a dictionary
print("creating a dictionary:")
'''
key: state
value: capital
'''

states_to_captials = {
    "texas" : "austin",
    "new york" : "albany"
}

print("the state for new york is: ", states_to_captials["new york"])

# for each key in the dictionary key, print the key - which is texas and new york
for key in states_to_captials.keys():
    print(key)

# if wanna access both key and value, use items
for key, value in states_to_captials.items():
    print(key, " | ", value) 
    '''
    note:
    can use either , or + but there are some differences
    , can be used with any data type
    + must be with the same type. in this case is strings. if not will get TypeError
    '''


# mutating a dictionary
print("\n\nmutating a dictionary:")

# this has a mixture of strings, numerical and boolean
user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

print("current user preferences: ", user_preferences, "\n")

# to change values by using the key
user_preferences["language"] = "Spanish"
user_preferences["volume_level"] = 50

# to add a new key
user_preferences["highlight_colour"] = "yellow"

# to delete an item
del user_preferences["currency"] # cannot retrieve the item once deleted

removed_item = user_preferences.pop("date_format", "N/A") # if want to retrieve item once deleted

print("updated user preferences: ", user_preferences)


# dropping empty items
print("\n\ndropping empty items:")
'''
creating a function that takes in a dictionary and
creates a new dictionary without the empty values

eg: user preferences below has 2 None. 
the output must show only those with value. so the 2 None won't be showed
'''
user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

def update_preferences(user_preferences):

    print("exsting user preference is: ", user_preferences)

    new_user_preferences = {} # creating a new dictionary

    for key, value in user_preferences.items():
        if value is not None:
            new_user_preferences[key] = value # add those without None value to the new dictionary
    return new_user_preferences # return the new dictionary

print("\nnew user preference after removing None is: ", update_preferences(user_preferences))
