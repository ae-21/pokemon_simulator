"""
Programa Principal - Simulador de Entrenamiento Pokémon
Maneja la interacción con el usuario y valida las entradas.
"""

import sys
import os
from clases.pokemon import Pokemon, PokemonFuego, PokemonAgua, PokemonPlanta

equipo_pokemon = []

def listar_equipo():
    """Muestra los Pokémon registrados con índice."""
    if not equipo_pokemon:
        print("⚠️️ No tienes ningún Pokémon en tu equipo.")
        return False
    
    print("\n=== TU EQUIPO PÓKEMON ===")
    for idx, p in enumerate(equipo_pokemon, 1):
        estado = " [DEBILITADO]" if p.salud <= 0 else ""
        print(f"{idx}. {p.nombre} ({p._tipo}) - Nivel {p.nivel} - HP: {p.salud:.1f}/{p.salud_maxima:.1f}{estado}")
    return True

def capturar_pokemon():
    print("\n--- 🐾 CAPTURAR PÓKEMON ---")
    nombre = input("Nombre del Pokémon: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    print("Tipos disponibles: 1. Fuego | 2. Agua | 3. Planta")
    tipo_input = input("Selecciona tipo (Fuego/Agua/Planta o 1/2/3): ").strip().capitalize()

    if tipo_input in ["1", "Fuego"]:
        tipo = "Fuego"
    elif tipo_input in ["2", "Agua"]:
        tipo = "Agua"
    elif tipo_input in ["3", "Planta"]:
        tipo = "Planta"
    else:
        print("❌ Tipo no válido. Debe ser Fuego, Agua o Planta.")
        return

    try:
        ataque = float(input("Puntos de Ataque: "))
        defensa = float(input("Puntos de Defensa: "))
        salud = float(input("Puntos de Salud: "))

        if not (Pokemon.validar_estadistica(ataque) and 
                Pokemon.validar_estadistica(defensa) and 
                Pokemon.validar_estadistica(salud)):
            print("❌ Error: Todas las estadísticas deben ser números mayores a 0.")
            return

        if tipo == "Fuego":
            nuevo_p = PokemonFuego(nombre, ataque, defensa, salud)
        elif tipo == "Agua":
            nuevo_p = PokemonAgua(nombre, ataque, defensa, salud)
        elif tipo == "Planta":
            nuevo_p = PokemonPlanta(nombre, ataque, defensa, salud)

        equipo_pokemon.append(nuevo_p)

    except ValueError:
        print("❌ Error: Ingresa un valor numérico válido para las estadísticas.")

def entrenar_pokemon():
    print("\n--- 🏋️ ENTRENAR PÓKEMON ---")
    if not listar_equipo():
        return

    try:
        idx = int(input("\nSelecciona el número del Pokémon a entrenar: ")) - 1
        if 0 <= idx < len(equipo_pokemon):
            p = equipo_pokemon[idx]
            print("\nOpciones de entrenamiento:")
            print("1. Entrenamiento General (Mejora todo)")
            print("2. Entrenamiento Enfocado (Elige hasta 2 stats: ataque/defensa/salud)")
            opcion = input("Opción (1/2): ").strip()

            if opcion == "2":
                stat1 = input("Primera stat a mejorar (ataque/defensa/salud): ").strip().lower()
                stat2 = input("Segunda stat a mejorar (opcional, presiona Enter para omitir): ").strip().lower()
                p.entrenar(stat1 if stat1 else None, stat2 if stat2 else None)
            else:
                p.entrenar()
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("❌ Por favor ingresa un número válido.")

def simular_ataque():
    print("\n--- ⚔️ BATALLA PÓKEMON ---")
    if len(equipo_pokemon) < 2:
        print("⚠️ Necesitas al menos 2 Pokémon en tu equipo para simular una batalla.")
        return

    listar_equipo()
    try:
        idx_atacante = int(input("\nSelecciona el Pokémon ATACANTE: ")) - 1
        idx_defensor = int(input("Selecciona el Pokémon OBJETIVO: ")) - 1

        if not (0 <= idx_atacante < len(equipo_pokemon) and 0 <= idx_defensor < len(equipo_pokemon)):
            print("❌ Selección fuera de rango.")
            return

        if idx_atacante == idx_defensor:
            print("❌ Un Pokémon no puede atacarse a sí mismo.")
            return

        atacante = equipo_pokemon[idx_atacante]
        objetivo = equipo_pokemon[idx_defensor]

        if atacante.salud <= 0:
            print(f"❌ {atacante.nombre} está debilitado y no puede atacar.")
            return
        if objetivo.salud <= 0:
            print(f"❌ {objetivo.nombre} ya está debilitado.")
            return

        print(f"\n⚡ ¡{atacante.nombre} ataca a {objetivo.nombre}!")
        atacante.atacar(objetivo)

    except ValueError:
        print("❌ Ingresa números enteros válidos.")

def ver_informacion():
    print("\n--- 📜 INFORMACIÓN DEL EQUIPO ---")
    if not equipo_pokemon:
        print("⚠️ No hay Pokémon capturados.")
        return

    for p in equipo_pokemon:
        p.mostrar_info()
        print("-" * 35)

def mostrar_total():
    print("\n--- 📊 ESTADÍSTICAS GLOBALES ---")
    print(f"Total de Pokémon activos en el sistema: {Pokemon.total_pokemons()}")

def liberar_pokemon():
    print("\n--- ✨ LIBERAR PÓKEMON ---")
    if not listar_equipo():
        return

    try:
        idx = int(input("\nSelecciona el número del Pokémon que deseas liberar: ")) - 1
        if 0 <= idx < len(equipo_pokemon):
            liberado = equipo_pokemon.pop(idx)
            del liberado
        else:
            print("❌ Selección fuera de rango.")
    except ValueError:
        print("❌ Ingresa un número válido.")

def menu():
    while True:
        print("\n" + "="*35)
        print("  📋 MENÚ DE ENTRENADOR PÓKEMON  ")
        print("="*35)
        print("1. Capturar Pokémon")
        print("2. Entrenar Pokémon")
        print("3. Atacar")
        print("4. Ver información")
        print("5. Total de Pokémon")
        print("6. Liberar Pokémon")
        print("7. Salir")
        print("="*35)

        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            simular_ataque()
        elif opcion == "4":
            ver_informacion()
        elif opcion == "5":
            mostrar_total()
        elif opcion == "6":
            liberar_pokemon()
        elif opcion == "7":
            print("\n¡Gracias por jugar, Maestro Pokémon! 👋")
            sys.exit()
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()