#read file
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Read file finished, there are',  len(data),'reviews.')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('Average lenth of each review is', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new),'reviews that less than 100 words')

#good = []
#for d in data:
#	 if 'good' in d:
#		good.append(d)
good =[d for d in data if 'good' in d]
print('There are', len(good), 'reviews with good.')