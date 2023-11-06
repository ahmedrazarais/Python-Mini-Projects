# season according to months:
print("From December to March:Winter Season")
print("From april to july:Summer Season")
print("From august to september:spring Season")
print("From October to November:Autumn Season")
# Taking input by user:
Month=input("Enter the Month:")
# convert in small blocks:
month=Month.lower()
# conditions:
if month in "decemberjanuaryfeburarymarch":
    print("It's a Winter Season\nEnjoy your Days!")
elif month in "aprilmayjunejuly":
    print("It's A hot season SUMMER!")
elif month in "augustseptember":
    print("It's A beautiful season Spring!")    
elif month in "octobernovemer":
    print("It's A beautiful season Autumn!")    
else:
    print("Invalid 'Check your spelling'" )    