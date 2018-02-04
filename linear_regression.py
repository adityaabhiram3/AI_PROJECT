datas = []
s = []
word=""
X_MEAN = 0
Y_MEAN = 0
X_TOTAL = 0
Y_TOTAL = 0
SUM1 = 0
SUM2 = 0
INTERCEPT = 0
with open("dataset2.txt") as f :
	for i in f :
		i = i.strip()
		for j in i :
			if j!=" " and j!='\\':
				#print(i)
				word+=j
			else:
				s.append(word)
				word = ""
			if len(s)==2:
				datas.append(s)
				s = []
#print(datas)
for k in range(1,len(datas)):
	datas[k][0] = float(datas[k][0])
	datas[k][1] = float(datas[k][1])
#print(datas)
for l in range(1,len(datas)) :
	X_TOTAL += datas[l][0]
	X_MEAN = X_TOTAL/(len(datas)-1)
	Y_TOTAL += datas[l][1]
	Y_MEAN = Y_TOTAL/(len(datas)-1)
for m in range(1,len(datas)) :
	X = datas[m][0]
	Y = datas[m][1]
	if X == 0.0 :
		INTERCEPT = Y
	SUM1 += (X-X_MEAN)*(Y-Y_MEAN)
	SUM2 += (X-X_MEAN)**2
SLOPE = SUM1/SUM2
SEPAL_LENGTH = input("the sepal length is :")
SEPAL_LENGTH = float(SEPAL_LENGTH)
SEPAL_WIDTH = (SLOPE*SEPAL_LENGTH)+INTERCEPT
print("the predicted sepal width is : ",SEPAL_WIDTH)
for v in range(1,len(datas)) :
	X = datas[v][0]
	Y = datas[v][1]
	if SEPAL_LENGTH == X :
		ACCURACY = (SEPAL_LENGTH/Y)*100
print("the precision of the algorithm is :",ACCURACY)
