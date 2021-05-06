import sys

fileSeqNo = 0

def out_a_block_lines(a_blk_lns, sbj, act):
	global fileSeqNo
	if act == "1":
		if a_blk_lns:
			#for li in a_blk_lns:
			#	print("\t", li, end="")
			#print("----")
			#filename = "__"+str(fileSeqNo)+"s"+sbj+"a"+act+".txt"
			filename = "__%03d_s%02d_a%d.txt" % (fileSeqNo, int(sbj), int(act))
			with open(filename, "w") as outf:
				outf.writelines( a_blk_lns )
			fileSeqNo += 1
			#print("wrote to ", filename)
	#else:
	#	print("skip act ", act)


with open(sys.argv[1]) as f:
	last_sbj = None
	last_act = None
	a_block_lines = None
	for s_line in f:
		#print(s_line, end="")
		idx = s_line.find("\t") # index of the first tab
		sbj = s_line[0:idx]
		idx += 1
		act = s_line[idx]
		#print("sbj=", sbj, " act=", act)

		#print(last_sjb,last_act,

		if last_sbj == None or sbj != last_sbj or act != last_act:
			# entered a new block of lines
			out_a_block_lines( a_block_lines, last_sbj, last_act)
			a_block_lines = [s_line]
		else:
			a_block_lines.append(s_line)
			
		last_sbj = sbj
		last_act = act
	out_a_block_lines( a_block_lines, last_sbj, last_act)
