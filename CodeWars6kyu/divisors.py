# Create a function named divisors/Divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
def divisors(integer):
    # List we append divisors to
    result = []

    # Iterates for numbers between 1 and the integer
    for i in range(1, integer):
        # If we find a divisor, ...
        if integer % i == 0:
            # we check that it is not 1 or the given integer
            if i != 1 and i != integer:
                # and if not, we add it to the list
                result.append(i)

    # If the list is empty, we return the necessary string and return the list otherwise
    if not result:
        return str(integer) + ' is prime'
    else:
        return result
