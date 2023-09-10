def convert_to_celsius(fahrenheit):
    '''
Return the number Celsius degrees equivalen tto fahrenheit degrees
(number) -> float
convert_to_celsius(32)
>>> convert_to_celsius(32)
0
>>> convert_to_celsius(212)
100
'''
    return (fahrenheit - 32) * (5/9)
