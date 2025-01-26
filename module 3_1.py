calls = 0
def count_calls():
    global calls
    calls +=1
def string_info(s):
    count_calls()
    return (len(s), s.upper(), s.lower())
def is_coontains(s, list_to_search):
    count_calls()
    return any(s.lower()== item.lower() for item in list_to_search)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_coontains('Urban',['ban', 'BaNaN', 'urBAN']))
print(is_coontains('cycle',['recycling', 'cyclic']))
print(calls)