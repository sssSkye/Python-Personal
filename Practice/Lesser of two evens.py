# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(x,y):
    if x % 2 == 0 and y % 2 == 0:
        return min(x,y)
    else:
        return max(x,y)
        
print(lesser_of_two_evens(2,4))
