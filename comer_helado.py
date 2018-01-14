apetece_helado_input = input("¿Te apetece un helado? (Si/No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no, a ver si te enteras. No se que me has dicho, asi que cuento como que no.")
    apetece_helado = False

tienes_dinero_input = input("¿Tienes dinero para un helado un helado? (Si/No): ").upper()
esta_el_senor_helados_input = input("¿Esta el señor de los helados? (Si/No): ").upper()
esta_tia_input = input("¿Estas con tu tia? (Si/No): ").upper()



apetece_helado = apetece_helado_input == "SI"
tienes_dinero = tienes_dinero_input == "SI"
esta_tia = esta_tia_input == "SI"
puede_permitirselo = tienes_dinero or esta_tia
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Genial, puedes tomarte un helado")
else:
    print("Vaya, otra vez sera")