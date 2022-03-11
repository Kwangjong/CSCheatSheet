def selectionSort(unsorted):
	array = unsorted[:] # duplicate list
	for i in range(len(array)):
		smallestInd = i
		for j in range(i+1, len(array)): # find index of the smallest elements started from i+1
			if(array[j] < array[smallestInd]):
				smallestInd = j

		temp = array[i] # swap i and smallestInd
		array[i] = array[smallestInd]
		array[smallestInd] = temp

	return array