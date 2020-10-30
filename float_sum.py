
#sum of two floats wich return the true mathemathical sum as s and mistake as t
def sum_two_floats (a, b):
	s = (a+b);
	bb = (s-a);
	aa = (s-bb);
	d_b = (b-bb);
	d_a = (a-aa);
	t = (d_a+d_b);
	return (s, t)

a = 0.1
b = 0.3

print (sum_two_floats(a, b))

#sum of floats in list wich return the true mathemathical sum as s and mistake as t
def sum_list_of_floats (x):
	i = 0
	while i < len(x):
		a = x[i]
		j = i + 1
		if j == 1:
			b = x[j]
		else:
			b = s
			
		s = (a+b);
		bb = (s-a);
		aa = (s-bb);
		d_b = (b-bb);
		d_a = (a-aa);
		t = (d_a+d_b);
		if j==1:
			i = j + 1
		else:
			i = i+1
	return (s, t)

x = [a, b]
print (sum_list_of_floats(x))

x = [0.3, 0.1]
print (sum_list_of_floats(x))

x = [0.3, 0.1, 0.2, 0.7, 0.9, 0.3]
print (sum_list_of_floats(x))
