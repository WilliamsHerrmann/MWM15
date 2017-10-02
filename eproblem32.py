#We will put the products in a set to avoid duplicates
products = set()

#Digits from 1-9 which will be checked later
to_be_checked = set('123456789')

#in the case of a  single digit multiplicand
for i in xrange(9):
	for j in xrange(999,9999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s) > 9:break

#in the case of a double digit multiplicand
for i in xrange(9,99):
	for j in xrange(99,999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s)>9: break

#to print the result
print sum(products)
