import time
import progressbar

#read file
data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
		
print('Read file finished, there are',  len(data),'reviews.')

print(data[0])

# word count
start_time = time.time()
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
end_time = time.time()
print('It took', end_time - start_time, 'seconds to finish the word count.')

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