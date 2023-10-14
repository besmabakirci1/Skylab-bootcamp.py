#This program could find the perfect square numbers between the min and max value which you gonna input in.
def perfect_squre_numbers_find( min_value , max_value):
    Perfect_squre_numbers = [ ]
    Square_root_minvalue = int(min_value ** 0.5)
    Square_root_maxvalue = int(max_value ** 0.5)
    for i in range(Square_root_minvalue ,Square_root_maxvalue + 1):
     Perfect_squre_number = i ** 2
     if min_value <= Perfect_squre_number <= max_value:
      Perfect_squre_numbers.append(Perfect_squre_number)

    return Perfect_squre_numbers

min_value= int(input("Please enter min value: "))
max_value= int(input("Please enter max value: "))
result = perfect_squre_numbers_find(min_value, max_value)
print("perfect squre numbers:", result)
