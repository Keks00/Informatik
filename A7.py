wine1= 12.99
wine2= 9.98
wine3= 11.99
wine1_amount=int(input('Please enter the number of "Rotwein"'))
wine2_amount=int(input('Please enter the number of "Rosewein"'))
wine3_amount=int(input('Please enter the number of "Weißwein"'))
wine1_total = wine1_amount * wine1
wine2_total = wine2_amount * wine2
wine3_total = wine3_amount * wine3
total = str(wine1_total + wine2_total + wine3_total)
print(total, "$.")