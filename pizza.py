pizza = ('mushroom', 8, 'thin crust')
topping, number_slices, crust = pizza
andrew_pizza = ('pepperoni', 12, 'thin')
esther_pizza = ('basil', 4, 'burnt')

#Don't change the actual text of sentences.
print "My favorite pizza topping is {}. I can eat {} slices of that! But only on a {} crust".format(pizza[0],pizza[1],pizza[2])

#Hey, what are these numbers inside the brackets?
print "My favorite pizza topping is {}. I can eat {} slices of that! But only on a {} crust".format(pizza[0],pizza[1],pizza[2])

#Out of order!
print "I'd like to order {1} slices of pizza, on a {2} crust please! And hold the {0}".format(pizza[0],pizza[1],pizza[2])

#Hmm, what happened to 1?
print "I'd like to order a {0} pizza. {2} slices, please! I don't care what crust".format(pizza[0],pizza[1],pizza[2])

