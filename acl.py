acl= int(input("Ingrese el numero de la ACL: "))

if acl <= 99 and acl >= 1:
	print("esta acl corresponde a una estandar")
elif acl >= 100 and acl <=200:
	print("esta acl corresponde a una extendida")
else:
	print("esta acl no es valida")

