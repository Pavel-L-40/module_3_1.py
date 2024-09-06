def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len_str = len(string)
    second_par = string.upper()
    third_par = string.lower()
    end_tuple = (len_str,second_par,third_par)
    return end_tuple


def is_contains(string, list_to_search):
    count_calls()
    fir_par = string.lower()
    sec_par = []
    for i in list_to_search:
        sec_par.append(i.lower())
    if fir_par in sec_par:
        flag = True
    else: flag = False

    return flag

calls = 0



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)