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

print(data[0])

wc = {}#word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #new key put in dictionary
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print('There are', len(wc), 'different words in the reviews.')
print('Your name Stephen has been shown', wc['Stephen'], 'times in the reviews.')

while True:
	word = input('Word you want to search:')
	if word == 'q':
		break
	if word in wc:
		print(word, 'has been used', wc[word], 'times.')
	else:
		print('This word has not been used in the reviews.')
		
print('Thanks for using this search function.')