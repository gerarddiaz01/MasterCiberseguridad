#pedir al usuario que hamburguesa quiere
hamburguesa = input("¿Qué hamburguesa desea? La clasica o la vegana: ").strip().lower()

if hamburguesa == "clasica":
    print("¿Qué ingredientes extra desea en su hamburguesa clasica?")
    queso = input("¿Desea queso idiazabal? Si o No: ").strip().lower() == "si"
    bacon = input("¿Desea bacon? Si o No: ").strip().lower() == "si"
    huevo = input("¿Desea huevo? Si o No: ").strip().lower() == "si"
    
    print("Has escogido una hamburguesa clasica con los siguientes ingredientes extra:")
    if queso:
        print("- Queso idiazabal")
    if bacon:
        print("- Bacon")
    if huevo:
        print("- Huevo")
    if not (queso or bacon or huevo):
        print("Sin ingredientes extra.")

elif hamburguesa == "vegana":
    print("¿Qué ingredientes extra desea en su hamburguesa vegana?")
    tofu = input("¿Desea tofu? Si o No: ").strip().lower() == "si"
    cebolla = input("¿Desea cebolla? Si o No: ").strip().lower() == "si"
    
    print("Has escogido una hamburguesa vegana con los siguientes ingredientes extra:")
    if tofu:
        print("- Tofu")
    if cebolla:
        print("- Cebolla")
    if not (tofu or cebolla):
        print("Sin ingredientes extra.")

else:
    print("Opción no válida. Por favor, elija entre 'clasica' o 'vegana'.")