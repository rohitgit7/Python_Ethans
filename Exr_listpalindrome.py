#print integers in a list are palindrome or not

lt = [121,123,454,237]

for n in lt:
	reverse= 0
	orig = n
	while n != 0:
		remainder = n % 10
		reverse = reverse*10 + remainder
		n = n / 10
	if orig == reverse:
		print "No. %d is palindrome" %(reverse)
	else:
		print "No. %d is Not palindrome" %(reverse)

#print number with max occurence 
lt1 = [1,2,4,2,1,5,1,1,2,3,2,3,3,3,3,3,3,2,2,2]
d = {}
maxkey = []
for n in lt1:
	if d.has_key(n):
		d[n] += 1
	else:	
		d[n] = 1
for k,v in d.items():
	if d[k] == max(d.values()):
		maxkey.append(k) 
print "\nThe maximum times occured nos. in the list is/are %s and their count is %d \n" %(maxkey,max(d.values()))
#print keys_list[values_list.index(max(values_list))]

