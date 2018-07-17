import csv
 
with open('AQI_20180717.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)

    aqi=50
    
    print(reader)
    for i in reader:
        try:
            temp=int(i[2]) 
        except ValueError:
            print('detect str')
        else:
            if temp < aqi:
                aqi = int(i[2])
    
    print("最小AQI是:",aqi)
        
        
            
        

        
 
