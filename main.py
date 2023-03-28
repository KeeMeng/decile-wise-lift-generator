# confusion matrix:
#        Predicted
#           Y N
# Actual Y [A B]
#        N [C D]

# sorted confusion matrix, predicted has priority
# [A, C, B, D]
report = [3, 3, 2, 5]
total = sum(report)
global_mean = (report[0] + report[2]) / total
decile_means = [0 for i in range(10)]

# convert confusion matrix into binary list
# 1 when actual value is yes (A and B)
data = []
[data.extend([int(index%2==0) for j in range(i)]) for (index, i) in enumerate(report)]
print(f"data: {data}")

decile = 0
for (count, i) in enumerate(data):
	# check if data exceeds current decile
	print(f"data {count}: {i} ({int((count)/total*100)}%-{int((count+1)/total*100)}%)")
	if (count+1)/total*10 > decile + 1:
		# counters start from 0, need to add 1
		exceed = ((count+1)/total - (decile+1)/10)
		
		decile_means[decile] += (1/total - exceed) * i
		print(f"- decile {decile} add {round((1/total - exceed) * i, 3)}")
		
		# add exceed to next decile
		decile_means[decile+1] += exceed * i
		print(f"- decile {decile+1} add {round(exceed * i, 3)}")
		decile += 1
	else:
		decile_means[decile] += (1/total) * i
		print(f"- decile {decile} add {round((1/total) * i, 3)}")

heights = [round(decile_mean*10/global_mean, 2) for decile_mean in decile_means]
# print(decile_means)
print(f"heights: {heights}")
