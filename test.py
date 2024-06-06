#"variant04.xml"
def somik(fil):
    with open(fil,"r",encoding="utf-8") as file:
        data = file.readlines()
    out = ""
    sus = "0"
    for i in data:
        #print(i)
        if i.find("<w:spacing") != -1:
            sus = "1"


        mem = i.find("</w:t>")
        if mem != -1:
            kek = i.find(">")
            out = out + sus * len(i[kek+1:mem])#out + i[kek+1:mem]
            #print(sus)
            sus = "0"
        if i.find("</w:r>") != -1:
            sus = "0"
            
    return out

def tomik(fil):
    with open(fil,"r",encoding="utf-8") as file:
        data = file.readlines()
    out = ""
    sus = "0"
    for i in data:
        #print(i)
        if i.find("<w:w w:val") != -1:
            sus = "1"

        mem = i.find("</w:t>")
        if mem != -1:
            kek = i.find(">")
            out = out + sus * len(i[kek+1:mem])#out + i[kek+1:mem]
            #print(sus)
            sus = "0"
        if i.find("</w:r>") != -1:
            sus = "0"
    return out
#somik("variant04.xml")
#print(tomik("variant03.xml"))