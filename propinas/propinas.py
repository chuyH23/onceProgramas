
factura_total = float(input("Ingrese la factura total: "))


porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dar: "))


propina = factura_total * (porcentaje_propina / 100)


total_con_propina = factura_total + propina


print(f"Propina del {porcentaje_propina}%: ${propina:.2f}")
print(f"Total con propina: ${total_con_propina:.2f}")