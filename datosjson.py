import json
import yaml

with open("myfile.json", "r") as json_file:
	ourjson = json.load(json_file)
print("NUESTRO TOKEN ES EL SIGUIENTE:  {}".format(ourjson["access_token"]))
print("NUESTRO TOKEN EXPIRA EN {} segundos.".format(ourjson["expires_in"]))
