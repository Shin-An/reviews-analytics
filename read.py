data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 是一運算符號，用來求餘數(意即為count要是1000的倍數)
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) # 讀取每一筆長度並累加
	
print('留言的平均長度為', sum_len/len(data))