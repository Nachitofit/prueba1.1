opcion = int(input("seleccione una opcion:\n1. Configurar una interfaz.\n2. Configurar una interfaz y crear en OSPF\n "))

if opcion == 1:
    interfaz= input("ingrese interfaz: ")
    ip= input("ingrese la direccion ip: ")
    masck= input("ingrese mascara de subnet: ")
    nombre= input("ingrese nombre: ")
    
    lista1= [
        f"configura lo siguiente:",
        f" ",
        f"interface {interfaz}",
        f"no shut",
        f"ip address {ip} {masck}",
        f"descripcon *** {nombre}***",
        f"speed 100",
        f"duplex full",
        f"",
        f"Consulte los siguientes comandos ",
        f"",
        f"show ip interface brief",
        f"show run interface {interfaz}",
        f"show interface {interfaz}",
    ]   
    
    for lista1 in lista1:
        print(lista1)
        
else :
    
 interfaz2= input("ingrese interfaz: ")
 ip2= input("ingrese la direccion ip: ")
 masck2= input("ingrese mascara de subnet: ")
 nombre2= input("ingrese nombre: ")
 proceso= input(" N° proceso OSPF: ")
 id= input("ID de area OSPF: ")   
 
 lista2 = [
        f"configura lo siguiente:",
        f" ",
        f"interface {interfaz2}",
        f"no shut",
        f"ip address {ip2} {masck2}",
        f"descripcon *** {nombre2}***",
        f"speed 100",
        f"duplex full",
        f"",
        f"Router ospf {proceso}",
        f"network {ip2}",
        f"pasive-interface {interfaz2}",
        f"Consulte los siguientes comandos ",
        f"",
        f"show ip interface brief",
        f"show run interface {interfaz2}",
        f"show interface {interfaz2}",
    ]   
 for lista2 in lista2:
        print(lista2)
   
