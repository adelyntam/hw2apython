def swap_list(list):
	i = 0
	for x in list:
		i+=1
	middleInd = (int(i-1)/2)
	while i > -1:
		list[middleInd], list[i-1] = list[i-1], list[middleInd]	
		i -= 1
		middleInd += 1
