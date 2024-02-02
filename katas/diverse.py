from datetime import datetime, timedelta
import numpy as np


def fibonacci(n):
    fib_ = [0, 1]
    while len(fib_) < n:
        net_n = fib_[-1] + fib_[-2]
        fib_.append(net_n)
    return fib_


def somme_multiple(n):
    total = 0
    # Use a breakpoint in the code line below to debug your script.
    for i in range(n):
        if i % 3 == 0 or 5 % i == 0:
            total += i
    
    return total


def palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]


def max_num(tab):
    maxi = tab[0]
    
    for nb in tab:
        if nb > maxi:
            maxi = nb
    return maxi


def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def square(val):
    new_val = val ** 2
    return new_val


def calculate_result(identifier):
    identifier_str = str(identifier)
    
    sum_even = 0
    sum_odd = 0
    
    for position, digit_str in enumerate(identifier_str):
        digit = int(digit_str)
        
        if position % 2 == 0:  # Even-numbered position
            sum_even += digit
        else:  # Odd-numbered position
            sum_odd += digit
    
    intermediate_result = (sum_even * 3) + sum_odd
    last_digit = intermediate_result % 10
    
    if last_digit != 0:
        result = 10 - last_digit
    else:
        result = 0
    
    return result


def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    similarity = dot_product / (norm1 * norm2)
    return similarity


def euclidean_distance(vector1, vector2):
    distance = np.linalg.norm(vector1 - vector2)
    return distance


def get_current_and_next_week_dates():
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the date for next week
    next_week_date = current_date + timedelta(weeks=1)
    
    # Format dates as strings
    current_date_str = current_date.strftime("%Y-%m-%d")
    next_week_date_str = next_week_date.strftime("%Y-%m-%d")
    
    return current_date_str, next_week_date_str


def city():
    yield ("zurick")
    yield ("stugart")


if __name__ == '__main__':
    n = 10
    result = somme_multiple(n)
    print(result)
    
    word = "radar"
    if palindrome(word):
        print("palindrome")
    else:
        print("not palindrome")
    
    f_n = 10
    fib = fibonacci(f_n)
    print(fib)
    
    tab = [0, 5, 10]
    nb_max = max_num(tab)
    print(nb_max)
    # Test cases
    
    number = 7
    result = check_odd_even(number)
    print(f"{number} is {result}.")
    
    s = square(3)
    print(s)
    
    identifier = 39847
    calculated_result = calculate_result(identifier)
    
    print(
        f"The calculated result for identifier {identifier} is {calculated_result}.")
    
    # Call the function
    current_date, next_week_date = get_current_and_next_week_dates()
    
    # Print the result
    print("Current date:", current_date)
    print("Next week date:", next_week_date)
    
    cities = city()
    for city in cities:
        print(city)
    for city in cities:
        print(city)
    
    lis1 = [1, 4, 6, 10]
    list2 = (x ** 2 for x in lis1)
    
    print(next(list2), next(list2))
    
    n = set(["horche", "j", "H"])
    print(n)
    
    print(type(5 / 2))
    
    my_string = "Hey there"
    print(my_string[2:])
    
    my_dict = {
        "a": "lorem",
        "b": "ipsum"
    }
    
    other_dict = my_dict
    other_dict["c"] = "lorem"
    del other_dict["a"]
    
    print(my_dict)
    print(other_dict)
    
    nums = set([1, 1, 2, 3, 3, 3, 4])
    print(len(nums))
    
    res = 5 / 2
    print(res)
    var = "ipsum"
    print(f"lorem {var} dolorem")
    lis1 = ["a", "b"]
    lis1.reverse()
    print(lis1)
    
    name = "jhon"
    if (n := name.lower())[0] == "J":
        print("yes")
    else:
        print("no")
    
    colors1 = {
        "apples": "Green",
    }
    
    colors2 = colors1
    
    colors2["apples"] = "Yellow"
    
    print('colors1:', colors1)
    print('colors2:', colors2)
    
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    
    similarity = cosine_similarity(vector1, vector2)
    print(f"Similarity Cosine: {similarity}")
    
    distance = euclidean_distance(vector1, vector2)
    print(f"Euclidean Distance: {distance}")
