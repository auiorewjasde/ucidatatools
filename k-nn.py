import sys


k = int(sys.argv[1])
vallen = int(sys.argv[2])

trainingfile = sys.argv[3]
testfile = sys.argv[4]

def line2label_n_values(line):
	#print(line,end="")
	tokens = line.rstrip().split(",")

	label = tokens[0]
	vals = tokens[1:1+vallen]
	#print([label,vals])
	return [label,vals]

def evalFn(vals0, l_n_vals1):
	#print("l_n_vals1=", l_n_vals1)
	vals1 = l_n_vals1[1]
	#print(vals1)
	dist = 0.0
	for i in range(vallen):
		dist += (float(vals0[i]) - float(vals1[i]))**2
	return dist


with open(trainingfile) as filtrain:
	l_vals = []
	lines = filtrain.readlines()
	for line in lines:
		l_n_v = line2label_n_values(line)
		l_vals.append(l_n_v)

with open(testfile) as filtest:
	lines = filtest.readlines()
	for line in lines:
		label,values = line2label_n_values(line)

		l_vals_s = sorted(l_vals, key=lambda x:evalFn(values,x))

		formax = min( len(l_vals_s), k)
		
		print("accu= ",label, " : ", end="")
		for i in range(formax):
			lv = l_vals_s[i]
			print(lv[0], " ", end="")
		print()

