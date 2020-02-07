import os, re, sys 

def verify_inputs():
    try:
        if len(sys.argv) <2 :
            sys.exit("Usage: VBADeobfuscator [options] <filename>")
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
def read_in_file():
    pass

def splice_quotes():
    pass

def main():
    verify_inputs()
    pass

if __name__ is "__main__":
    main()

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
