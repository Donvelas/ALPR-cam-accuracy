#!/bin/python3
import pandas as pd
import csv, os

sites = []
user = os.getlogin()
if_file = input("Drag and drop input file: ")
location = (if_file.replace("\\","/"))
week = input("Date: ")
if_contents = []
df3 = pd.DataFrame()

master_dict = {
"tractor" : {
    
    "match" : {
        "asset" : []
    },

    "one" : {
        "asset" : [],
        "prism" : [],
        "defects" : {
            "Y" : 0,
            "PB": 0,
            "miss" : 0
        }
    },
    "blank" : {
        "padding" : []
    },

    "two" : {
        "asset" : [],
        "prism" : []
    },
    "three" : {    
        "asset" : [],
        "prism" : []
    },
    "counts" : {
        "totals" : []
    }
},

"trailer" : {
    "match" : {
        "asset" : []
    },
    "one" : {
        "asset" : [],
        "prism" : [],
        "defects" : {
            "Y" : 0,
            "PB": 0,
            "miss" : 0
        }
    },
    "blank" : {
        "padding" : []
    },

    "two" : {
        "asset" : [],
        "prism" : []
    },
    "three" : {    
        "asset" : [],
        "prism" : []
    },
    "counts" : {
        "totals" : []
    }
    },
    "CHECK_IN":[],
    "CHECK_OUT":[]
}

l1 = []
totals = []

tract_root = (master_dict["tractor"])
trail_root = (master_dict["trailer"])
tract_match = (master_dict["tractor"]["match"]["asset"])
trail_match = (master_dict["trailer"]["match"]["asset"])
tract_one = (tract_root["one"]["asset"])
trail_one = (trail_root["one"]["asset"])
tract_two = (tract_root["two"]["asset"])
trail_two = (trail_root["two"]["asset"])
tract_three = (tract_root["three"]["asset"])
trail_three = (trail_root["three"]["asset"])
tract_blank = (tract_root["blank"]["padding"])
trail_blank = (trail_root["blank"]["padding"])

def get_sites():
    with open(location, "r") as f:
        reader = csv.reader(f)
        for i in reader:
            if_contents.append(i)
            if i[0] not in sites:
                sites.append(i[0])
        sites.pop(0)

def check_dirs():
    for i in sites:
        check1 = os.path.isdir("C:/Users/" + user + "/" + i)
        if check1 == False:
            os.mkdir("C:/Users/" + user + "/" + i)
            os.mkdir("C:/Users/" + user + "/" + i + "/Camera_Accuracy")
        elif check1 == True:
                check2 = os.path.isdir("C:/Users/" + user + "/" + i + "/Camera_Accuracy")
                if check2 == False:
                    os.mkdir("C:/Users/" + user + "/" + i + "/Camera_Accuracy/")

def clear():


    master_dict["tractor"]["blank"]["padding"].clear()
    master_dict["trailer"]["blank"]["padding"].clear()
    global df3
    df3 = pd.DataFrame()
    totals.clear()
    for i in master_dict["tractor"]["one"]["defects"]:
        master_dict["tractor"]["one"]["defects"][i] = 0
    for i in master_dict["trailer"]["one"]["defects"]:
            master_dict["trailer"]["one"]["defects"][i] = 0
    
def sort(lane):

    master_dict[lane] = [x for x in l1 if x[1] == lane]
    root1 = master_dict["tractor"]
    root2 = master_dict["trailer"]
    root1["match"]["asset"] = [x[10] for x in master_dict[lane] if x[18] == "1" or x[19] == "1" or x[20] == "1"]
    root1["one"]["asset"] = [x[10] for x in master_dict[lane] if x[21] == "1"]
    root1["one"]["prism"] = [x[11] for x in master_dict[lane] if x[21] == "1"]
    root1["two"]["asset"] = [x[10] for x in master_dict[lane] if x[22] == "1"]
    root1["two"]["prism"] = [x[11] for x in master_dict[lane] if x[22] == "1"]
    root1["three"]["asset"] = [x[10] for x in master_dict[lane] if x[23] == "1"]
    root1["three"]["prism"] = [x[11] for x in master_dict[lane] if x[23] == "1"]
    root1["Total"] = [(len(root1["match"]["asset"])+len(root1["one"]["asset"])+len(root1["two"]["asset"])+len(root1["three"]["asset"]))]
    root2["match"]["asset"] = [x[15] for x in master_dict[lane] if x[28] == "1" or x[29] == "1" or x[30] == "1"]
    root2["one"]["asset"] = [x[15] for x in master_dict[lane] if x[31] == "1"]
    root2["one"]["prism"] = [x[16] for x in master_dict[lane] if x[31] == "1"]
    root2["two"]["asset"] = [x[15] for x in master_dict[lane] if x[32] == "1"]
    root2["two"]["prism"] = [x[16] for x in master_dict[lane] if x[32] == "1"]
    root2["three"]["asset"] = [x[15] for x in master_dict[lane]  if x[33] == "1"]
    root2["three"]["prism"] = [x[16] for x in master_dict[lane] if x[33] == "1"]
    root2["Total"] = [(len(root2["match"]["asset"])+len(root2["one"]["asset"])+len(root2["two"]["asset"])+len(root2["three"]["asset"]))]

    totals.append("Tractor Match: " + str(len(root1["match"]["asset"])))
    totals.append("Tractor One: " + str(len(root1["one"]["asset"])))
    totals.append("Tractor Two: " + str(len(root1["two"]["asset"])))
    totals.append("Tractor Three: " + str(len(root1["three"]["asset"])))

    totals.append("Trailer Match: " + str(len(root2["match"]["asset"])))
    totals.append("Trailer One: " + str(len(root2["one"]["asset"])))
    totals.append("Trailer Two: " + str(len(root2["two"]["asset"])))
    totals.append("Trailer Three: " + str(len(root2["three"]["asset"])))

    for i in root1["one"]["asset"]:
        idx = root1["one"]["asset"].index(i)
        if i.startswith("Y") and not root1["one"]["prism"][idx].startswith("Y"):
            root1["one"]["defects"]["Y"] += 1
        if i.startswith("PB") and root1["one"]["prism"][idx].startswith("P8"):
            root1["one"]["defects"]["PB"] += 1
        if len(i) != len(root1["one"]["prism"][idx]):
            root1["one"]["defects"]["miss"] += 1
    for i in root2["one"]["asset"]:
        idx = root2["one"]["asset"].index(i)
        if i.startswith("Y") and not root2["one"]["prism"][idx].startswith("Y"):
            root2["one"]["defects"]["Y"] += 1
        if i.startswith("PB") and root2["one"]["prism"][idx].startswith("P8"):
            root2["one"]["defects"]["PB"] += 1
        if len(i) != len(root2["one"]["prism"][idx]):
            root2["one"]["defects"]["miss"] += 1

def write(lane, site):
    path = ("C:/Users/" + user + "/" + site + "/Camera_Accuracy/" + site + "-" + week + ".xlsx")
    df1 = pd.DataFrame()
    df1['Tractor Matches:'] = pd.Series(master_dict["tractor"]["match"]["asset"],dtype=object)
    df1[totals[0]] = pd.Series(master_dict["tractor"]["blank"]["padding"],dtype=object)
    df1['Tractor_1 Asset:'] = pd.Series(master_dict["tractor"]["one"]["asset"],dtype=object)
    df1['Tractor_1 Prism:'] = pd.Series(master_dict["tractor"]["one"]["prism"],dtype=object)
    df1[totals[1]] = pd.Series(master_dict["tractor"]["blank"]["padding"],dtype=object)
    df1['Tractor_2 Asset:'] = pd.Series(master_dict["tractor"]["two"]["asset"],dtype=object)
    df1['Tractor_2 Prism:'] = pd.Series(master_dict["tractor"]["two"]["prism"],dtype=object)
    df1[totals[2]] = pd.Series(master_dict["tractor"]["blank"]["padding"],dtype=object)
    df1['Tractor_3 Asset:'] = pd.Series(master_dict["tractor"]["three"]["asset"],dtype=object)
    df1['Tractor_3 Prism:'] = pd.Series(master_dict["tractor"]["three"]["prism"],dtype=object)
    df1[totals[3]] = pd.Series(master_dict["tractor"]["blank"]["padding"],dtype=object)
    df1[totals[3]] = pd.Series(master_dict["tractor"]["blank"]["padding"],dtype=object)
    df1[totals[3]] = pd.Series(master_dict["tractor"]["blank"]["padding"],dtype=object)
    df1["fn_1 Defects"] = pd.Series(["Y Misreads:","PB Misreads:","Missing Characters"])
    df1["Defect Values"] = pd.Series([master_dict["tractor"]["one"]["defects"]["Y"],master_dict["tractor"]["one"]["defects"]["PB"],master_dict["tractor"]["one"]["defects"]["miss"]])
    df1["Total:"] = pd.Series(master_dict["tractor"]["Total"],dtype=object)

    df2 = pd.DataFrame()
    df2['Trailer Matches:'] = pd.Series(master_dict["trailer"]["match"]["asset"],dtype=object)
    df2[totals[4]] = pd.Series(master_dict["trailer"]["blank"]["padding"],dtype=object)
    df2['Trailer_1 Asset:'] = pd.Series(master_dict["trailer"]["one"]["asset"],dtype=object)
    df2['Trailer_1 Prism:'] =pd.Series(master_dict["trailer"]["one"]["prism"],dtype=object)
    df2[totals[5]] = pd.Series(master_dict["trailer"]["blank"]["padding"],dtype=object)
    df2['Trailer_2 Asset:'] = pd.Series(master_dict["trailer"]["two"]["asset"],dtype=object)
    df2['Trailer_2 Prism:'] = pd.Series(master_dict["trailer"]["two"]["prism"],dtype=object)
    df2[totals[6]] = pd.Series(master_dict["trailer"]["blank"]["padding"],dtype=object)
    df2['Trailer_3 Asset:'] = pd.Series(master_dict["trailer"]["three"]["asset"],dtype=object)
    df2['Trailer_3 Prism:'] = pd.Series(master_dict["trailer"]["three"]["prism"],dtype=object)
    df2[totals[7]] = pd.Series(master_dict["trailer"]["blank"]["padding"],dtype=object)
    df2[totals[7]] = pd.Series(master_dict["trailer"]["blank"]["padding"],dtype=object)
    df2[totals[7]] = pd.Series(master_dict["trailer"]["blank"]["padding"],dtype=object)
    df2["fn_1 Defects"] = pd.Series(["Y Misreads:","PB Misreads:","Missing Characters"])
    df2["Defect Values"] = pd.Series([master_dict["trailer"]["one"]["defects"]["Y"],master_dict["trailer"]["one"]["defects"]["PB"],master_dict["trailer"]["one"]["defects"]["miss"]])
    df2["Total:"] = pd.Series(master_dict["trailer"]["Total"],dtype=object)

    
    try:
        with pd.ExcelWriter(path, mode="a") as writer:
            df1.to_excel(writer, sheet_name= lane + " Tractors", index=False)
            df2.to_excel(writer, sheet_name= lane + " Trailers", index=False)
    except:
        with pd.ExcelWriter(path) as writer:
            df1.to_excel(writer, sheet_name= lane + " Tractors", index=False)
            df2.to_excel(writer, sheet_name= lane + " Trailers", index=False)


get_sites()

check_dirs()
os.listdir()

#for i in sites:
  #  out_path = ("C:/Users/" + user + "/" + i + "/Camera_Accuracy/" + i + "-" + week + ".xlsx")
   # l1 = [x for x in if_contents if x[0] == i]
   # if os.path.isfile(out_path) == True:
     #   os.remove(out_path)
    #sort("CHECK_IN")
    #write("CHECK_IN", i)
    #clear()
    #sort("CHECK_OUT")
    #write("CHECK_OUT", i)
    #clear()
    #print("Output saved: " + out_path)