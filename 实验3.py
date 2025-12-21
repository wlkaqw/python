
def start(s):
	lst1=[]
	L=s.split()
	for i in L:
		if len(i)<2:
			continue
		if not i.isupper():
			i=i.lower()
		if i.endswith((',','.','\'',"\"",':',';')):
			i=i[:-1]
		if i[0].isdigit():
			continue
		lst1.append(i)
		word_count={}
	lst2=[]
	for i in lst1:
		if i not in lst2:
			lst2.append(i)
		word_count[i]=word_count.get(i,0)+1
	n=len(lst2)
	parts=[f'{word}({count})' for word,count in zip(lst2,[word_count[w] for w in lst2])]
	res = f'"{n}: {"; ".join(parts)};"'
	return res
# 以下为测试代码
if __name__ == '__main__':
	s = "Participants in the 16th BRICS Excellence Training Program on Artificial Intelligence Technology and Governance \
visit the robot section of the 2024 BRICS New Industrial Revolution Exhibition in Xiamen, Fujian province, in \
September. Photo provided to China Daily When Dipuo Mazibuko embarked on her first overseas travel in September, \
it was to China. She took a close look at the country's achievements in the field of artificial intelligence and \
gained a deeper understanding of the importance of working with China and other BRICS countries on AI." 
	
	print(start(s))
