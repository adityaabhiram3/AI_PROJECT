s = []
word=""
datas=[]
count_total=0
count_total2=0
count_total3=0
count_total4=0
count_favourable1=0
count_favourable2=0
count_favourable3=0
count_favourable4=0
count_favourable5=0
count_favourable6=0
count_favourable7=0
count_favourable8=0
count_delay=0
with open("dataset.txt") as f :
	for i in f :
		i = i.strip()
		for j in i :
			if j!=" " and j!='\\':
				#print(i)
				word+=j
			else:
				#print(word)
				s.append(word)
				word=""
			if len(s)==5 :
				datas.append(s)
				s=[]
print(datas)
outlook = input("enter the outlook of the weather today(CLEAR\OVERCAST\CLOUDY):")
humidity = input("enter the humidity(HIGH\LOW) :")
windspeed = input("enter the windspeed(HIGH\LOW) :")
temperature = input("enter the temperature(HIGH\LOW) :")
for k in range(1,len(datas)) :
	if datas[k][4]=='DELAYED':
		count_delay+=1
	if outlook==datas[k][0]:
		count_total+=1
		if datas[k][4]=='DELAYED':
			count_favourable1+=1
		else:
			count_favourable2+=1
	if humidity==datas[k][1]:
		count_total2+=1
		if datas[k][4]=='DELAYED':
			count_favourable3+=1
		else:
			count_favourable4+=1
	if windspeed==datas[k][2]:
		count_total3+=1
		if datas[k][4]=='DELAYED':
			count_favourable5+=1
		else:
			count_favourable6+=1
	if temperature==datas[k][3]:
		count_total4+=1
		if datas[k][4]=='DELAYED':
			count_favourable7+=1
		else:
			count_favourable8+=1
count_on_time=len(datas)-count_delay
P_X1_DELAY=(count_favourable1/count_total)*(count_favourable3/count_total2)*(count_favourable5/count_total3)*(count_favourable7/count_total4)*(count_delay/len(datas))
P_X1=(count_total/len(datas))*(count_total2/len(datas))*(count_total3/len(datas))*(count_total4/len(datas))
P_DELAY=(P_X1_DELAY)/(P_X1)
#print(P_DELAY)
P_X1_ON_TIME=((count_favourable2/count_total)*(count_favourable4/count_total2)*(count_favourable6/count_total3)*(count_favourable7/count_total4)*(count_on_time/len(datas)))
P_X1
#print(P_X1_ON_TIME)
if P_X1_ON_TIME > P_X1_DELAY:
	print("the flight is on time")
else:
	print("the flight is delayed")











