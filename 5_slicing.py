clouds = "aws ibm azure hp gcp alibaba oracle"
description = "Hi all, I am Madhava Reddy Bonam from hyderabad"

# slicing
print(clouds[1]) #w
print(clouds[6]) #m
print(clouds[-1]) #e
print(clouds[-10]) #a

print(description[13:20])
print(description[13:33])
print(description[:6])
print(description[38:])

# slicing tuple
os = ("redhat", "ubuntu", "mac", "windows", "suse","fedora", "kali", "rocky")

print(os[1]) # ubuntu
print(os[7]) # rockey
print(os[2:5]) #('mac', 'windows', 'suse')
print(os[2:5][0]) # mac
print(os[2:5][0][1:3]) # ac

# slicing List
sports = ["cricket", "volleyball", "football", "carrom", "badminton", "running", ["chess", "Ludo", "pubg"], "tennis"]
print(sports)
print(sports[0]) # cricket
print(sports[6]) # ['chess', 'Ludo', 'pubg']
print(sports[6][1:3]) #['Ludo', 'pubg']
print(sports[5:8]) # ['running', ['chess', 'Ludo', 'pubg'], 'tennis']
print(sports[6][-1]) #pubg

# Dictionary example
tools = {"vcs":"git", "container":"docker", "cicd":("jenkins","bamboo","circle-ci"), "config-mgmt":"ansible", "iac":["terraform", "ctf", "ARM-template", "gcp-templates"]}
print(tools)
print(tools["vcs"]) # git
print(tools["cicd"]) #('jenkins', 'bamboo', 'circle-ci')
print(tools["iac"]) #['terraform', 'ctf', 'ARM-template', 'gcp-templates'
print(tools["iac"][1]) #cft
print(tools["iac"][1:3]) #['ctf', 'ARM-template']
