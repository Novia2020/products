#continue乎略不印出那一行
#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:#在檔案裏的每一行
		if '商品,價格' in line:#假如商品和價格在行裏
			continue #跳到下一迴圈(還是在這個迴圈,只是不執行這個迴圈的以下程式),和break一樣只能在迴圈裏用,break是跳出這一整個迴圈
		name, price = line.strip().split(',')#這一行先從左至右執行strip是去掉換行和空格,split是看到','就切割
		products.append([name, price])
print(products)

#讓使用者輸入
while True:#while迴圈通常用在不確定幾次的迴圈
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])#將每1小組的p清單裝入products大清單中
print(products )#會印出[['01','02'], ['11', '12']]有2個[]

#印出所有購買記錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:#用w寫入語法時,沒有的檔案會被建立,用r讀取語法時,一定要存在要被讀取的檔案
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')#把()中的資料寫入f檔案裏
#存成csv檔,可以用excel開,且","分隔的是區分空格,若存


