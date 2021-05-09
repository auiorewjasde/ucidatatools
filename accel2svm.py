import sys

BLOCK_SIZE = 2048

infilename = sys.argv[1]
label = sys.argv[2]
outfile0 = sys.argv[3]
outfile1 = sys.argv[4]

with open(outfile0, "w") as filout0:
	with open(outfile1, "w") as filout1:

		with open(infilename) as f:
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

				filout0.write( label + " " )
				cnt = 1
				for j in xyzs0:
					filout0.write( str(cnt) + ":" + j + " " )
					cnt += 1
				filout0.write("\n")

				filout1.write( label + " " )
				cnt = 1
				for k in range(3):
					for j in xyzs1:
						filout1.write( str(cnt) + ":" + j[k] + " " )
						cnt += 1
				filout1.write("\n")

