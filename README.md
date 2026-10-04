# 🎮 Simulador de Entrenamiento Pokémon (POO en Python)

Este proyecto es una aplicación interactiva desarrollada en Python que simula un sistema de gestión y entrenamiento de Pokémon en consola. Fue creado para aplicar de manera práctica los conceptos clave de la Programación Orientada a Objetos (POO).

---

## 🚀 Conceptos de POO Aplicados

1. **Herencia**: La clase base `Pokemon` transfiere sus atributos y métodos generales a las clases derivadas `PokemonFuego`, `PokemonAgua` y `PokemonPlanta`.
2. **Reutilización de miembros con `super()`**: Se utiliza `super().__init__()` para inicializar el constructor base y `super().mostrar_info()` para extender la información propia de cada elemento.
3. **Redefinición de métodos y Polimorfismo**: Cada tipo de Pokémon redefine el método `atacar()` aplicando sus ventajas y desventajas elementales:
   - 🔥 **Fuego**: x2 contra 🍃 **Planta** y x0.5 contra 💧 **Agua**.
   - 💧 **Agua**: x2 contra 🔥 **Fuego** y x0.5 contra 🍃 **Planta**.
   - 🍃 **Planta**: x2 contra 💧 **Agua** y x0.5 contra 🔥 **Fuego**.
4. **Métodos de Clase y Estáticos**: 
   - `@classmethod total_pokemons()`: Rastrea la cantidad de Pokémon activos mediante el atributo de clase `_contador_pokemons`.
   - `@staticmethod validar_estadistica()`: Verifica que las estadísticas sean valores numéricos positivos.
5. **Constructores y Destructores**: Control automático del contador de Pokémon al capturar (`__init__`) y liberar (`__del__`) integrantes del equipo.

---

## 📂 Estructura del Proyecto

```text
pokemon_simulator/
│
├── main.py
├── README.md
└── clases/
    └── pokemon.py
