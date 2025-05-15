
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
niveles_azucar = [130, 160, 95, 175, 160, 145, 100]        # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700, 2200, 2100]   # mg
presion_sistolica = [115, 130, 110, 125, 175, 138, 122]    # mmHg



def evaluar_azucar(nivel):
    if 70 <= nivel <= 140:
        return "Normal"
    else:
        return "Alerta: Azúcar fuera del rango saludable"

def evaluar_sal(nivel):
    if nivel <= 2300:
        return "Normal"
    else:
        return "Alerta: Exceso de sal"

def clasificar_presion(sistolica):  
    if sistolica < 120:
        return "Presión Normal"
    elif 120 <= sistolica <= 129:
        return "Presión Elevada"
    elif 130 <= sistolica <= 139:
        return "Hipertensión Etapa 1"
    else:
        return "Hipertensión Etapa 2"


print("Evaluación diaria:\n")

for i in range(len(dias)):
    print(f"{dias[i]}:")
    azucar = niveles_azucar[i]
    sal = niveles_sal[i]
    presion = presion_sistolica[i]

    print(f"  Azúcar en sangre: {azucar} mg/dL - {evaluar_azucar(azucar)}")
    print(f"  Consumo de sal: {sal} mg - {evaluar_sal(sal)}")
    print(f"  Presión sistólica: {presion} mmHg - {clasificar_presion(presion)}")
    print()

prom_azucar = sum(niveles_azucar) / len(niveles_azucar)
prom_sal = sum(niveles_sal) / len(niveles_sal)
prom_presion = sum(presion_sistolica) / len(presion_sistolica)

print("Resumen semanal:")
print(f"  Promedio azúcar: {prom_azucar:.1f} mg/dL - {evaluar_azucar(prom_azucar)}")
print(f"  Promedio sal: {prom_sal:.1f} mg - {evaluar_sal(prom_sal)}")
print(f"  Promedio presión sistólica: {prom_presion:.1f} mmHg - {clasificar_presion(prom_presion)}")
