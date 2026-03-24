def mostrar_menu():
    while True:
        print("\n" + "=" * 50)
        print("Programa que convierte decimal, binario y octal")
        print("=" * 50)
        print("[1] Decimal -> Binario")
        print("[2] Decimal -> Octal")
        print("[3] Binario -> Decimal")
        print("[4] Binario -> Octal")
        print("[5] Octal   -> Decimal")
        print("[6] Octal   -> Binario")
        print("[7] Salir")
        
        opcion_base = input("Ingrese una opción (1-7) y luego presione enter: ")
        print("=" * 50)
        
        if opcion_base == '7':
            print("Saliendo... ¡Hasta luego!")
            break
        
        if opcion_base not in ['1', '2', '3', '4', '5', '6']:
            print(">>> ERROR: Opción no válida. Intente de nuevo.")
            continue

        num_decimal = 0.0
        if opcion_base in ['3', '5']: base_actual = "Decimal"
        elif opcion_base in ['1', '6']: base_actual = "Binario"
        else: base_actual = "Octal"


        while True: 
            try:
                if opcion_base in ['1', '2']:
                    entrada = input("Ingrese número decimal: ")
                    if "/" in entrada:
                        p = entrada.split("/"); num_decimal = int(p[0]) / int(p[1])
                    else:
                        num_decimal = float(entrada)
                    break

                if opcion_base in ['3', '4']:
                    entrada = input("Ingrese número binario: ")
                    ent_calc = entrada[1:] if entrada.startswith("-") else entrada
                    if not all(c in '01.' for c in ent_calc):
                        print(">>> Ey, ese no es un número binario válido.")
                        continue
                    p_e, p_d = (ent_calc.split(".") if "." in ent_calc else (ent_calc, ""))
                    val_abs = int(p_e, 2) if p_e else 0
                    for i, bit in enumerate(p_d):
                        val_abs += int(bit) * (2 ** -(i + 1))
                    num_decimal = -val_abs if entrada.startswith("-") else val_abs
                    break

                if opcion_base in ['5', '6']:
                    entrada = input("Ingrese número octal y luego presione enter: ")
                    ent_calc = entrada[1:] if entrada.startswith("-") else entrada
                    if not all(c in '01234567.' for c in ent_calc):
                        print(">>> Ese no es un número octal válido.")
                        continue
                    p_e, p_d = (ent_calc.split(".") if "." in ent_calc else (ent_calc, ""))
                    val_abs = int(p_e, 8) if p_e else 0
                    for i, d in enumerate(p_d):
                        val_abs += int(d) * (8 ** -(i + 1))
                    num_decimal = -val_abs if entrada.startswith("-") else val_abs
                    break
            except ValueError:
                print(">>> Formato incorrecto.")


        while True:
            resultado_final = ""
            if base_actual == "Decimal":
                # Redondeo a 10 decimales para limpiar el ruido de precisión 
                # rstrip elimina ceros innecesarios a la derecha
                resultado_final = format(round(num_decimal, 10), '.10f').rstrip('0').rstrip('.')
            
            elif base_actual == "Binario":
                entero = int(abs(num_decimal)); decimal = abs(num_decimal) - entero
                res_e = bin(entero).replace("0b", "") if entero != 0 else "0"
                res_decimal = ""
                temp_d = decimal
                while temp_d > 0 and len(res_decimal) < 32:
                    temp_d *= 2; digito = int(temp_d)
                    res_decimal += str(digito); temp_d -= digito
                resultado_final = ("-" if num_decimal < 0 else "") + res_e + ("." + res_decimal if res_decimal else "")

            elif base_actual == "Octal":
                entero = int(abs(num_decimal)); decimal = abs(num_decimal) - entero
                res_e = oct(entero).replace("0o", "") if entero != 0 else "0"
                res_decimal = ""
                temp_d = decimal
                while temp_d > 0 and len(res_decimal) < 32:
                    temp_d *= 8; digito = int(temp_d)
                    res_decimal += str(digito); temp_d -= digito
                resultado_final = ("-" if num_decimal < 0 else "") + res_e + ("." + res_decimal if res_decimal else "")

            print("-" * 40)
            print(f"El resultado en {base_actual} es: {resultado_final}")
            print("-" * 40)

            resp = input("¿Quieres convertir este mismo número a otra base? (s/n): ").lower()
            
            if resp == 's':
                opciones = ["Decimal", "Binario", "Octal"]
                opciones.remove(base_actual)
                print("\nSeleccione la nueva base y luego presione enter:")
                print(f"[1] {opciones[0]}")
                print(f"[2] {opciones[1]}")
                nueva_op = input("Opción: ")
                if nueva_op == '1': base_actual = opciones[0]
                elif nueva_op == '2': base_actual = opciones[1]
                else: print(">>> Opción inválida.")
                continue 
            break 


        continuar_programa = True
        while True:
            answer = input("\n¿Hacer otra conversión con un número nuevo? (s/n): ").lower()
            if answer == "s":
                break 
            elif answer == "n":
                print("Gracias por usar la calculadora :)")
                continuar_programa = False
                break
            else:
                print(">>> Escribe 's' o 'n'.")
        
        if not continuar_programa:
            break

mostrar_menu()