def square_filter(start, end):
    squares = [i**2 for i in range(start, end+1)]
    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    print("All squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

start = int(input('Start number? '))
end = int(input('End number? '))
square_filter(start, end)
