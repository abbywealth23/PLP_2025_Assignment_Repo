#Question 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent/100)
        return discounted_price
    else:
        return price
    
#Question 2

price_input = float (input ('Enter the original price of the item: '))
discount_input = float(input('Enter the discount percentage: '))
final_price = calculate_discount(price_input, discount_input)
print( f" the final price after discount is: {final_price}")
