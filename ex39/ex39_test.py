#-*-coding:utf8


import hashmap

# create a mapping to states to abbreciation
states = hashmap.new()
hashmap.set(states, 'Oregen', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Hawaii', 'HI')

# create a basio set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'Los Angeles')
hashmap.set(cities, 'HI', 'Honolulu')
hashmap.set(cities, 'FL', 'Orlando')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print('-' * 10)
print("NY State has: %s" % hashmap.get(cities, 'NY'))
print("HI State has: %s" % hashmap.get(cities, 'HI'))

# print some states
print('-' * 10)
print("Hawaii's abbreviation is: %s" % hashmap.get(states, 'Hawaii'))
print("Florida's abbreviation is: %s" % hashmap.get(states, 'Florida'))

# do it by using the state then cities diot
print('-' * 10)
print("Hawaii's abbreviation is: %s" % hashmap.get(cities, hashmap.get(states, 'Hawaii')))
print("Florida's abbreviation is: %s" %  hashmap.get(cities, hashmap.get(states, 'Florida')))

# print every state abbreviation
print('-' * 10)
hashmap.list(states)

# print every city in state
print('-' * 10)
hashmap.list(cities)

print('-' * 10)
state = hashmap.get(states, 'Texas')

if not state:
    print("Sorry, no Texas")

# default values using l l = with the nill result
# can you do this one line?
city = hashmap.get(cities, 'TX', 'Not Entered Vet')
print("The city for the state 'TX' is: %s" % city)

