# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def Descending_Order(num):
    # Create a list with the split up ints from num
    numlist = [int(i) for i in str(num)]

    # Create a new list that is sorted from greatest to least
    sortedlist = sorted(numlist, reverse=True)

    # Join the sorted list together and convert to int
    return int(''.join(str(i) for i in sortedlist))
