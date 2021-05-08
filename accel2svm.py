import sys

BLOCK_SIZE = 2048

with open(sys.argv[3], "w") as filout:
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
			for j in range(BLOCK_SIZE):
				_, x, y, z = ar[j].rstrip().split(",")
				xs.append(x)
				ys.append(y)
				zs.append(z)
			xyzs = xs + ys + zs
			for j in xyzs:
				filout.write( j + " " )
			filout.write("\n")

