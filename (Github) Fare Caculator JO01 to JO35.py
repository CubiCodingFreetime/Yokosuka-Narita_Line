import pandas as pd
from IPython.display import clear_output



#Yokosuka_Sen = pd.read_excel("Yokosuka_Sobu_NaritaAirport Line.xlsx",'Yokosuka Line')
Yokosuka_dict = {'Station No.':['JO01',	'JO02',	'JO03',	'JO04',	'JO05',	'JO06',	'JO07',	'JO08',	'JO09',	'JO10',	'JO11',	'JO12',	'JO13',	'JO14',	'JO15',	'JO16',	'JO17',	'JO18',	'JO19'],
                 'Station':['Kurihama',	'Kinugasa',	'Yokosuka',	'Taura',	'Higashi-Zushi',	'Zushi',	'Kamakura',	'Kita-Kamakura',	'Ōfuna',	'Totsuka',	'Higashi-Totsuka',	'Hodogaya',	'Yokohama',	'Shin-Kawasaki',	'Musashi-Kosugi',	'Nishi-Ōi',	'Shinagawa',	'Shimbashi',	'Tokyo'],
                 'Japanese':['久里浜',	'衣笠',	'横須賀',	'田浦',	'東逗子',	'逗子',	'鎌倉',	'北鎌倉',	'大船',	'戸塚',	'東戸塚',	'保土ヶ谷',	'横浜',	'新川崎',	'武蔵小杉',	'西大井',	'品川',	'新橋',	'東京'],
                 'Distance Between Stations (km)':[0,	4.6,	3.4,	2.1,	3.4,	2,	3.9,	2.2,	2.3,	5.6,	4.2,	4.9,	3,	7.1,	2.7,	6.4,	3.6,	4.9,	1.9],
                 'Location':['Yokosuka',	'Yokosuka',	'Yokosuka',	'Yokosuka',	'Zushi',	'Zushi',	'Kamakura',	'Kamakura',	'Kamakura',	'Totsuka-ku, Yokohama',	'Totsuka-ku, Yokohama',	'Hodogaya-ku, Yokohama',	'Nishi-ku, Yokohama',	'Saiwai-ku, Kawasaki',	'Nakahara-ku, Kawasaki',	'Shinagawa',	'Minato',	'Minato',	'Chiyoda'],
                 'Location2':['Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Kanagawa',	'Tokyo',	'Tokyo',	'Tokyo',	'Tokyo']
                 }
Yokosuka_Sen = pd.DataFrame.from_dict(Yokosuka_dict)
#Sobu_kaisoku_Sen = pd.read_excel("Yokosuka_Sobu_NaritaAirport Line.xlsx",'Sobu Line (Rapid)')
Sobu_dict = {'Station No.':['JO20',	'JO21',	'JO22',	'JO23',	'JO24',	'JO25',	'JO26',	'JO27',	'JO28'],
             'Station':['Shin-Nihombashi',	'Bakurochō',	'Kinshichō',	'Shin-Koiwa',	'Ichikawa',	'Funabashi',	'Tsudanuma',	'Inage',	'Chiba'],
             'Japanese':['新日本橋',	'馬喰町',	'錦糸町',	'新小岩',	'市川',	'船橋',	'津田沼',	'稲毛',	'千葉'],
             'Distance Between Stations (km)':[1.2,	1.1,	2.5,	5.2,	5.4,	7.8,	3.5,	9.2,	3.3],
             'Location':['Chūō',	'Chūō',	'Sumida',	'Katsushika',	'Ichikawa',	'Funabashi',	'Narashino',	'Inage-ku',	'Chūō-ku'],
             'Location2':['Tokyo',	'Tokyo',	'Tokyo',	'Tokyo',	'Chiba',	'Chiba',	'Chiba',	'Chiba',	'Chiba']
             }
Sobu_kaisoku_Sen = pd.DataFrame.from_dict(Sobu_dict)

#Narita_Kuko_Sen = pd.read_excel("Yokosuka_Sobu_NaritaAirport Line.xlsx",'Narita Line (Airport)')
Narita_dict = {'Station No.':['JO29',	'JO30',	'JO31',	'JO32',	'JO33',	'JO34',	'JO35',	'JO36',	'JO37'],
               'Station':['Higashi-Chiba',	'Tsuga',	'Yotsukaidō',	'Monoi',	'Sakura',	'Shisui',	'Narita',	'Narita Airport Terminal 2·3',	'Narita Airport Terminal 1'],
               'Japanese':['東千葉',	'都賀',	'四街道',	'物井',	'佐倉',	'酒々井',	'成田',	'空港第２ビル',	'成田空港'],
               'Distance Between Stations (km)':[0.9,	3.3,	3.5,	4.2,	4.2,	6.4,	6.7,	9.8,	1],
               'Location':['Chūō-ku',	'Wakaba-ku',	'Yotsukaidō',	'Yotsukaidō',	'Sakura',	'Shisui',	'Narita',	'Narita',	'Narita'],
               'Location2':['Chiba',	'Chiba',	'Chiba',	'Chiba',	'Chiba',	'Chiba',	'Chiba',	'Chiba',	'Chiba']
               }
Narita_Kuko_Sen = pd.DataFrame.from_dict(Narita_dict)


JR_East_Fares_Table_raw = pd.read_html('https://jr-group.jp/higashinihon-fare/',match='JR東日本幹線運賃表')
JR_East_Fares = JR_East_Fares_Table_raw[0].copy()
JR_East_Fares_ENG = JR_East_Fares.set_axis(['Distance Brackets (km)','Fare of One-Way (円)'],axis=1)
list_of_price_yen = JR_East_Fares_ENG['Fare of One-Way (円)'].tolist()
list_of_price = [s.strip('円') for s in list_of_price_yen]
JR_East_Fares_ENG['Fare of One-Way (円)'] = list_of_price


JO0119 = Yokosuka_Sen.iloc[:,[0,1,3]]
JO2028 = Sobu_kaisoku_Sen.iloc[:,[0,1,3]]
JO2937 = Narita_Kuko_Sen.iloc[:,[0,1,3]]

Go_Through = [JO0119,JO2028,JO2937]
JO0137_unfinish1 = pd.concat(Go_Through)
JO0137_unfinish2 = JO0137_unfinish1.reset_index(drop=True)
Total_Distance = []
result = 0
for i in range(len(JO0137_unfinish2)):
    result +=JO0137_unfinish2.values[i,2]
    Total_Distance.append(round(result,1))
JO0137_unfinish2['Bussiness Distance (km)'] = Total_Distance
JO0137 = JO0137_unfinish2


for i in range(len(JO0137)):
    print(f"{JO0137.values[i,0]} - {JO0137.values[i,1]}")
clear_output(wait = True)
Go = int(input('Please enter the Starting Point (using Number of Station code below)'))
Stop = int(input('Please enter the Stop Point (using Number of Station code below)'))
if Go <= 10 or Stop <= 10:
    Go_info = str('JO' + '0' + str(Go))
    Stop_info = str('JO' + '0' + str(Stop))
else:
    Go_info = str('JO' + str(Go))
    Stop_info = str('JO' + str(Stop))   
JO0137_list = JO0137['Station No.'].tolist()
if Go_info not in JO0137_list and Stop_info not in JO0137_list:
    print(f"Information incorrect, please make sure you have enter correct Station code, maximum number is: {len(JO0137_list)}")
else:
    print(f"Your trip is: \n  Departure Station: {JO0137.values[Go-1,1]} \n  Arrival Station: {JO0137.values[Stop-1,1]}")

Travelling = 0
for i in range(Go,Stop):
    Travelling += JO0137.values[i,2]
Travelling_2 = round(Travelling,1)
print(f"\nThe total travel length is {Travelling_2}")
bracket_km = JR_East_Fares_ENG.values[:,0]
ticket_price = [a.strip(',') for a in list_of_price]
for i in range(len(bracket_km)):
    bracket_pos = str(bracket_km[i]).split('-')
    if int(bracket_pos[0]) <= Travelling_2 <= int(bracket_pos[1]):
        print(f"The ticket price is: ¥{ticket_price[i]}")
        break