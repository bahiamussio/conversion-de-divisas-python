 # Paso 1: Definir el valor actual del Euro y Dolar con respecto al Peso Mexicano.
tipo_cambio_eur_a_mxn = 23.70 # En un caso real habría que linkearlo con información actualizada de una BDD o API
tipo_cambio_usd_a_mxn = 20.75# En un caso real habría que linkearlo con información actualizada de una BDD o API

# Paso 2: Solicitar al usiario el tipo de conversión (Eu a MX o USD a MX)
tipo_conversion = input("Ingrese la moneda de orígen para la conversión (EUR/USD): ").lower()

# Validar si la moneda ingresada es válida antes de pedir el monto
if tipo_conversion not in ["eur", "usd"]:
    print("Este tipo de conversión no está disponible.")
else:
    # Paso 3: Solicitar al usuario el monto a convertir.
    monto_a_convertir = float(input("Por favor, ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente. 
if tipo_conversion == "eur":
        resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
        print("El resultado de la conversión de EUR a MX es:", resultado)
elif tipo_conversion == "usd":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MX es:", resultado)