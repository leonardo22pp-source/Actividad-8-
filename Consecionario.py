from abc import ABC, abstractmethod
from tabulate import tabulate  # Librería para mostrar la tabla


# CLASE VEHICULO
class Vehiculo(ABC):
    
    def __init__(self, marca, modelo, precio_base):
        self._marca = marca
        self._modelo = modelo
        self._precio_base = max(1, precio_base)

    # Getters 
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_precio_base(self):
        return self._precio_base

    # Método abstracto 
    @abstractmethod
    def impuesto(self):
        pass

    # Método para calcular el precio final del vehículo (precio base + impuesto)
    def precio_final(self):
        return self._precio_base + self.impuesto()

    # Devuelve una ficha informativa base del vehículo
    def ficha(self):
        return f"{self._marca} {self._modelo} (${self._precio_base:.2f})"

    # Representación en texto del objeto (equivalente a toString en Java)
    def __str__(self):
        return f"{self.ficha()}  |  Final: ${self.precio_final():.2f}"


# SUBCLASE: MOTO

class Moto(Vehiculo):
    

    def __init__(self, marca, modelo, precio_base, cc):
        super().__init__(marca, modelo, precio_base)
        self._cc = cc  # Cilindraje del motor

    def impuesto(self):
        # Si tiene hasta 250cc, paga 5%, si tiene más, paga 9%
        tasa = 0.05 if self._cc <= 250 else 0.09
        return self.get_precio_base() * tasa

    # Sobrescritura del método ficha() con más detalles
    def ficha(self):
        return f"Moto  |  {super().ficha()}  |  {self._cc}cc"


# SUBCLASE: AUTOMOVIL
class Automovil(Vehiculo):
  

    def __init__(self, marca, modelo, precio_base, puertas):
        super().__init__(marca, modelo, precio_base)
        self._puertas = puertas

    def impuesto(self):
        # Impuesto base del 8%
        imp = self.get_precio_base() * 0.08
        # Descuento del 1% si el vehículo tiene 5 puertas
        desc = self.get_precio_base() * 0.01 if self._puertas == 5 else 0
        return imp - desc

    def ficha(self):
        return f"Automovil  |  {super().ficha()}  |  {self._puertas} puertas"


# CLASE PRINCIPAL 
def main():
 

    # Lista (equivalente al List.of() en Java)
    inventario = [
        Automovil("Toyota", "Yaris", 40000, 5),
        Moto("Pulsar", "NS 200", 10000, 199),
        Automovil("Mazda", "CX30", 30000, 4),
        Moto("Yamaha", "R3", 34000, 350)
    ]

    # Lista para mostrar como tabla
    tabla_datos = []
    total = 0

    # Recorrer todos los vehículos e imprimir sus datos
    for vehiculo in inventario:
        # Agregamos cada fila a la tabla
        tabla_datos.append([
            vehiculo.__class__.__name__,  # Tipo (Automovil o Moto)
            vehiculo.get_marca(),
            vehiculo.get_modelo(),
            f"${vehiculo.get_precio_base():,.2f}",
            f"${vehiculo.precio_final():,.2f}"
        ])
        # Acumulamos el valor final total
        total += vehiculo.precio_final()

    # Imprimir la tabla
    print("\n🚗 INVENTARIO DEL CONCESIONARIO 🚙\n")
    print(tabulate(
        tabla_datos,
        headers=["Tipo", "Marca", "Modelo", "Precio Base", "Precio Final"],
        tablefmt="fancy_grid"
    ))

    # Mostrar total del inventario
    print(f"\n💰 Valor total del inventario: ${total:,.2f}\n")


# Punto de entrada (equivalente a public static void main en Java)
if __name__ == "__main__":
    main()
