# 📊 Calculadora de Impuesto IPI

Calculadora simple de impuesto anual basada en un escenario ficticio.

## ⚙️ Lógica de Cálculo

* Si el ingreso ≤ **\$85,528**, el impuesto es:

  ```
  ingreso * 18% - $556.02
  ```

* Si el ingreso > **\$85,528**, el impuesto es:

  ```
  $14,839.02 + (ingreso - 85,528) * 32%
  ```

## 📦 Requisitos

* Python 3.7 o superior
* Terminal que soporte colores ANSI (como VS Code o Windows Terminal)

## 🧪 Ejemplos

```bash
💼 Ingreso anual en pesos: 10000
💰 Impuesto a pagar: $1,244.00 MXN

💼 Ingreso anual en pesos: 100000
💰 Impuesto a pagar: $19,470.00 MXN
```

## 📁 Guardado de Resultados

Puedes guardar los cálculos en un archivo `historial_impuestos.txt` para referencia futura.

## 🧑‍💻 Autor

José Ortega — [GitHub](https://github.com/joseorteha)
