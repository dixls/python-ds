def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    digits1 = [digit for digit in str(num1)]
    digits2 = [digit for digit in str(num2)]
    digit_count1 = {digit:digits1.count(digit) for digit in digits1}
    digit_count2 = {digit:digits2.count(digit) for digit in digits2}
    return digit_count1 == digit_count2
