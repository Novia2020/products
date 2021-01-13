products = []#products是大火車,裝大清單,裝一組一組的小p;p小火車裝小清單,一個商品一個清單
while True:#while迴圈通常用在不確定幾次的迴圈
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])#將每1小組的p清單裝入products大清單中

print(products )#會印出[['01','02'], ['11', '12']]有2個[]
for p in products:
	print(p[0], '的價格是', p[1])

	#print(p[1])==>印出清單中的第2個欄位-價格

products[0][1]#找出第1節車節中的第2個小座位的值





#   p = []#產生1個價格+1個商品的小清單
#	p.append(name)#將名稱裝入p清單中
#	p.append(price)#將價格裝入p清單中
#	p = [name, price]這一行可以取代上面三行

#	p = [name, price]
#   products.append([name, price])這行可以取代上一行,就不用p了

