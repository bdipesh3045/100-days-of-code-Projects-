import os
dir_list = os.listdir()
value={'acer': '100', 'alcatel': '408', 'allview': '157', 'amazon': '24', 'amoi': '47', 'apple': '111', 'archos': '43', 'asus': '197', 'at&t': '4', 'benefon': '9', 'benq': '35', 'benq-siemens': '27', 'bird': '61', 'blackberry': '92', 'blackview': '49', 'blu': '360', 'bosch': '10', 'bq': '20', 'casio': '5', 'cat': '21', 'celkon': '229', 'chea': '12', 'coolpad': '41', 'dell': '20', 'doogee': '40', 'emporia': '15', 'energizer': '62', 'ericsson': '40', 'eten': '22', 'fairphone': '3', 'fujitsu siemens': '2', 'garmin-asus': '5', 'gigabyte': '63', 'gionee': '95', 'google': '22', 'haier': '59', 'honor': '158', 'hp': '41', 'htc': '278', 'huawei': '406', 'i-mate': '34', 'i-mobile': '37', 'icemobile': '61', 'infinix': '102', 'innostream': '18', 'inq': '5', 'intex': '15', 'jolla': '3', 'karbonn': '60', 'kyocera': '24', 'lava': '133', 'leeco': '9', 'lenovo': '238', 'lg': '667', 'maxon': '31', 'maxwest': '41', 'meizu': '67', 'micromax': '289', 'microsoft': '32', 'mitac': '12', 'mitsubishi': '25', 'modu': '8', 'motorola': '582', 'mwg': '5', 'nec': '73', 'neonode': '3', 'niu': '30', 'nokia': '554', 'nothing': '1', 'nvidia': '3', 'o2': '45', 'oneplus': '52', 'oppo': '256', 'orange': '19', 'palm': '17', 'panasonic': '123', 'pantech': '72', 'parla': '10', 'philips': '229', 'plum': '113', 'posh': '30', 'prestigio': '56', 'qmobile': '90', 'qtek': '21', 'razer': '2', 'realme': '152', 'sagem': '120', 'samsung': '1347', 'sendo': '19', 'sewon': '25', 'sharp': '68', 'siemens': '94', 'sonim': '18', 'sony': '155', 'sony ericsson': '188', 'spice': '120', 't-mobile': '61', 'tcl': '45', 'tecno': '110', 'tel.me.': '7', 'telit': '30', 'thuraya': '1', 'toshiba': '35', 'ulefone': '64', 'unnecto': '30', 'vertu': '17', 'verykool': '139', 'vivo': '338', 'vk mobile': '31', 'vodafone': '87', 'wiko': '96', 'wnd': '5', 'xcute': '4', 'xiaomi': '317', 'xolo': '81', 'yezz': '107', 'yota': '3', 'yu': '13', 'zte': '345'}


import pandas as pd

def checker(a):
    pd_xl_file = pd.ExcelFile(a)
    df = pd_xl_file.parse("Sheet1")
    dimensions = df.shape
    column=(dimensions[0]-1)
    return(column)
li=[]
ok=[]
total=0
for i in dir_list:
    index_of_dot = i.index('.')
    file_name_without_extension = i[:index_of_dot]
    file_name_without_extension=file_name_without_extension.lower()
    file_name_without_extension=file_name_without_extension.replace('phones', '').strip()
    if i=="main.py" or i=="main1.py":
        continue
    
    a=checker(i)
    total+=int(a)
    try:
        if int(value[file_name_without_extension])==int(a):
            print(f"{file_name_without_extension} Check passed No of columns {a}")
        else:
            print(f"{file_name_without_extension} Check Not passed No of columns in website {value[file_name_without_extension]} No of column in excel sheet {a}")
            li.append(f"{file_name_without_extension} Check Not passed No of columns in website {value[file_name_without_extension]} No of column in excel sheet {a}")
    except:
        ok.append(file_name_without_extension)
print("Eror")
   
for a in li:
    print(a)            
print("phoen")
for z in ok:
    print(z)       

print(total)


