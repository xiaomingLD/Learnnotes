import json
import numpy as np

name_emb = {'a':'1111', 'b':'2222','c':'3333','d':'4444'}

with open("nameconfig.json",'w') as f:
    isR = json.dump(name_emb,f,indent=4,ensure_ascii=False)

f.close()
