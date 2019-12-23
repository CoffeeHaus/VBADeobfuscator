import os, re, sys 
f = open(sys[1], "r")
VBA = f.read()
f.close()

out = ""
for line in VBA.split("\n"):
    search = re.search(r"\"([^&]+)\"\s*&\s*\"([^&]+)\"", line)
    while search:
        line = line.replace(search[0],"\"%s%s\""%(search[1],search[2]))
        search = re.search(r"\"([^&]+)\"\s*&\s*\"([^&]+)\"", line)
    out += "%s\n" % line
    
f = open(sys[1], "r")
f.write(out)
f.close()
