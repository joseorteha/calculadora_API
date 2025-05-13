"""
Calculadora de Impuesto Personal de Ingresos (IPI)
Autor: José Ortega
Versión: 1.1
Descripción:
    Simula el cálculo del impuesto anual (IPI) en un país ficticio.

Reglas de Cálculo:
    - Ingreso ≤ 85,528 => impuesto = ingreso * 18% - 556.02
    - Ingreso > 85,528 => impuesto = 14,839.02 + (ingreso - 85,528) * 32%
    - El impuesto nunca es menor a 0

Extras:
    - Valida entradas negativas
    - Formato de salida mejorado
    - Opción para guardar resultados en archivo
"""

import os

def calcular_ipi(ingreso: float) -> float:
    if ingreso <= 0:
        return 0.0
    elif ingreso <= 85528:
        impuesto = ingreso * 0.18 - 556.02
        return round(impuesto if impuesto > 0 else 0.0, 2)
    else:
        impuesto = 14839.02 + (ingreso - 85528) * 0.32
        return round(impuesto, 2)

def mostrar_banner():
    print("\033[95m" + "=" * 60)
    print("        🧮 CALCULADORA DE IMPUESTO IPI - VERSIÓN 1.1")
    print("=" * 60 + "\033[0m")

def formatear_moneda(valor: float) -> str:
    return f"${valor:,.2f} MXN"

def guardar_en_archivo(ingreso: float, impuesto: float):
    with open("historial_impuestos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Ingreso: {formatear_moneda(ingreso)} -> Impuesto: {formatear_moneda(impuesto)}\n")

def main():
    mostrar_banner()
    try:
        ingreso = float(input("💼 Ingreso anual en pesos: "))
        impuesto = calcular_ipi(ingreso)
        print(f"\n💰 Impuesto a pagar: \033[92m{formatear_moneda(impuesto)}\033[0m")

        # Preguntar si desea guardar el resultado
        guardar = input("📝 ¿Deseas guardar el resultado en un archivo? (s/n): ").lower()
        if guardar == "s":
            guardar_en_archivo(ingreso, impuesto)
            print("✅ Resultado guardado en 'historial_impuestos.txt'")
    except ValueError:
        print("\033[91m❌ Error: Debes ingresar un número válido.\033[0m")

if __name__ == "__main__":
    main()
