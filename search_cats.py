
import json
import pickle

with open('criteria.json') as f:
    data = f.read()
    criteria = json.loads(data)

search_range = criteria['search_range']
chk_tr_len = criteria['alltraits']
chk_Background = criteria['chk_Background']
chk_Body = criteria['chk_Body']
chk_Eyes = criteria['chk_Eyes']
chk_Mouth = criteria['chk_Mouth']
chk_Collar = criteria['chk_Collar']
chk_Accessory = criteria['chk_Accessory']
chk_OG = criteria['chk_OG']

interested_Background = []
for key,value in criteria['interested_Background'].items():
    if value == 1:
        interested_Background.append(key)
    
interested_Body = []
for key,value in criteria['interested_Body'].items():
    if value == 1:
        interested_Body.append(key)
    
interested_Eyes = []
for key,value in criteria['interested_Eyes'].items():
    if value == 1:
        interested_Eyes.append(key)
    
interested_Mouth = []
for key,value in criteria['interested_Mouth'].items():
    if value == 1:
        interested_Mouth.append(key)
    
interested_Collar = []
for key,value in criteria['interested_Collar'].items():
    if value == 1:
        interested_Collar.append(key)
    
interested_Accessory = []
for key,value in criteria['interested_Accessory'].items():
    if value == 1:
        interested_Accessory.append(key)

def load_db():
    with open ('cats_db', 'rb') as fp:
        return pickle.load(fp)

Allcats=load_db()

for i in range(search_range[0],search_range[1]):
    catsNFT = Allcats[i]
    traits = catsNFT["traits"]
    traits_len = len(traits)
    trait_types = []

    interested = 1

    for j in range(traits_len):
        the_trait = traits[j]
        if ((chk_Background == 1) and (the_trait["trait_type"] == "Background")):
            if the_trait["value"] not in set(interested_Background):
                interested = 0
                break
        if ((chk_Body == 1) and (the_trait["trait_type"] == "Body")):
            if the_trait["value"] not in set(interested_Body):
                interested = 0
                break
        if ((chk_Eyes == 1) and (the_trait["trait_type"] == "Eyes")):
            if the_trait["value"] not in set(interested_Eyes):
                interested = 0
                break
        if ((chk_Mouth == 1) and (the_trait["trait_type"] == "Mouth")):
            if the_trait["value"] not in set(interested_Mouth):
                interested = 0
                break
        if ((chk_Collar == 1) and (the_trait["trait_type"] == "Collar")):
            if the_trait["value"] not in set(interested_Collar):
                interested = 0
                break
        if ((chk_Accessory == 1) and (the_trait["trait_type"] == "Accessory")):
            if the_trait["value"] not in set(interested_Accessory):
                interested = 0
                break
        trait_types.append(the_trait["trait_type"])

    if ((chk_Collar == 1) and ("Collar" not in set(trait_types))):
        interested = 0
    if ((chk_Accessory == 1) and ("Accessory" not in set(trait_types))):
        interested = 0
    if ((chk_OG == 1) and ("OG" not in set(trait_types))):
        interested = 0
    if ((chk_tr_len == 1) and (("Collar" not in set(trait_types)) or ("Accessory" not in set(trait_types)))):
        interested = 0


    if interested == 1:
        print(catsNFT["id"])

