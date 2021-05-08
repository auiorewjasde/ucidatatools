import sys

BLOCK_SIZE = 2048


with open(sys.argv[3], "w") as filout0:
	with open(sys.argv[4], "w") as filout1:

		with open(sys.argv[1]) as f:
			lines = f.readlines()
			n_blocks = int( len(lines) / BLOCK_SIZE )
			print("size of lines =", len(lines), " n_blocks = ", n_blocks)
			#for line in lines:
			#	print(line,end="")
			for i in range(n_blocks):
				ar = lines[ BLOCK_SIZE*i : BLOCK_SIZE*(i+1) ]
				xs = []
				ys = []
				zs = []
				xyzs1 = []
				for j in range(BLOCK_SIZE):
					_, x, y, z = ar[j].rstrip().split(",")
					xs.append(x)
					ys.append(y)
					zs.append(z)
					xyzs1.append([x,y,z])
				xyzs0 = xs + ys + zs
				xyzs1.sort(key=lambda x: float(x[0])**2+float(x[1])**2+float(x[2])**2)

				for j in xyzs0:
					filout0.write( j + " " )
				filout0.write("\n")

				for k in range(3):
					for j in xyzs1:
						filout1.write( j[k] + " " )
				filout1.write("\n")

