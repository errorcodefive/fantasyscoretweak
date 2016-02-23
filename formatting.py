def formatName(firstlast):
    name = firstlast.strip()

    firstname=name[0:name.find(" ")]
    lastname=name[name.find(" "):name.find("&")].strip()
    return firstname+" "+lastname

def getTeam(input):
    #format fName lName TEAM
    output = input[input.rfind("$")+1:]
    return output.strip()
def retName(input):
    return input[:input.find("#")]
def retID(input):
    return input[input.find("#")+1:input.find("$")]
def retTeam(input):
    return input[input.find("$"):input.find("&")]
def retPos(input):
    return input[input.find("&")+1:input.find("$")]
