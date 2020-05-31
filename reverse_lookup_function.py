def ReverseLookup(dictionary, lookup_value):
    keys_list = [key for key, value in dictionary.items() if value == lookup_value]
    return keys_list
