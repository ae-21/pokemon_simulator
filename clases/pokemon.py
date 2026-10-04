"""
Módulo de Clases para el Simulador de Entrenamiento Pokémon
Demuestra Herencia, Redefinición de Métodos, super() y Polimorfismo.
"""

class Pokemon:
    _contador_pokemons = 0  # Atributo de clase (protegido)

    def __init__(self, nombre: str, ataque: float, defensa: float, salud: float):
        if not (self.validar_estadistica(ataque) and 
                self.validar_estadistica(defensa) and 
                self.validar_estadistica(salud)):
            raise ValueError("Las estadísticas deben ser valores numéricos positivos mayores a cero.")

        # Atributos públicos
        self.nombre = nombre
        self.nivel = 1
        self.ataque = float(ataque)
        self.defensa = float(defensa)
        self.salud = float(salud)
        self.salud_maxima = float(salud)

        # Atributo protegido
        self._tipo = "Normal"

        # Incrementar contador de clase
        Pokemon._contador_pokemons += 1
        print(f"¡{self.nombre} ha sido capturado! 🎉")

    def __del__(self):
        Pokemon._contador_pokemons -= 1
        print(f"{self.nombre} ha sido liberado ✨")

    @staticmethod
    def validar_estadistica(valor):
        """Verifica que un valor de estadística sea positivo."""
        try:
            val = float(valor)
            return val > 0
        except (ValueError, TypeError):
            return False

    @classmethod
    def total_pokemons(cls):
        """Devuelve cuántos Pokémon han sido creados y siguen activos."""
        return cls._contador_pokemons

    def subir_nivel(self):
        """Método interno para subir de nivel y mejorar estadísticas base."""
        self.nivel += 1
        self.ataque += 2
        self.defensa += 2
        incremento_salud = 5
        self.salud_maxima += incremento_salud
        self.salud = min(self.salud + incremento_salud, self.salud_maxima)

    def entrenar(self, stat1=None, stat2=None, stat3=None):
        """
        Aumenta el nivel y mejora las estadísticas indicadas.
        Simula sobrecarga mediante valores por defecto: si no recibe argumentos, mejora todas.
        """
        self.subir_nivel()
        
        if stat1 is None and stat2 is None and stat3 is None:
            self.ataque += 3
            self.defensa += 3
            self.salud_maxima += 5
            self.salud = self.salud_maxima
            print(f"¡{self.nombre} ha realizado un entrenamiento intensivo completo! 🏋️")
        else:
            stats = [s.lower() for s in (stat1, stat2, stat3) if s is not None]
            if "ataque" in stats:
                self.ataque += 5
            if "defensa" in stats:
                self.defensa += 5
            if "salud" in stats:
                self.salud_maxima += 10
                self.salud += 10
            print(f"¡{self.nombre} ha completado su entrenamiento enfocado! 🎯")

    def atacar(self, objetivo):
        """Simula un ataque básico hacia otro Pokémon."""
        if self.salud <= 0:
            print(f"¡{self.nombre} está debilitado y no puede atacar!")
            return 0

        dano_base = self.ataque - objetivo.defensa
        dano = max(1.0, dano_base)  # Daño mínimo de 1
        return dano

    def recibir_dano(self, cantidad: float):
        """Reduce la salud del Pokémon y verifica si fue debilitado."""
        self.salud -= cantidad
        if self.salud <= 0:
            self.salud = 0
            print(f"💥 {self.nombre} recibió {cantidad:.1f} de daño y se ha DEBILITADO... 😵")
        else:
            print(f"🛡️ {self.nombre} recibió {cantidad:.1f} de daño. Salud restante: {self.salud:.1f}/{self.salud_maxima:.1f}")

    def mostrar_info(self):
        """Muestra la ficha técnica del Pokémon."""
        print(f" ─── {self.nombre} ───")
        print(f"  Tipo: {self._tipo}")
        print(f"  Nivel: {self.nivel}")
        print(f"  Ataque: {self.ataque:.1f}")
        print(f"  Defensa: {self.defensa:.1f}")
        print(f"  Salud: {self.salud:.1f}/{self.salud_maxima:.1f}")


# ─────────────────────────────────────────────────────────────
# CLASES DERIVADAS
# ─────────────────────────────────────────────────────────────

class PokemonFuego(Pokemon):
    def __init__(self, nombre: str, ataque: float, defensa: float, salud: float):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Fuego"

    def atacar(self, objetivo):
        dano_base = super().atacar(objetivo)
        if dano_base == 0:
            return 0

        if objetivo._tipo == "Planta":
            dano = dano_base * 2.0
            print("¡Es súper efectivo! 🔥🍃")
        elif objetivo._tipo == "Agua":
            dano = dano_base * 0.5
            print("No es muy efectivo... 🔥💧")
        else:
            dano = dano_base

        objetivo.recibir_dano(dano)
        return dano

    def mostrar_info(self):
        super().mostrar_info()
        print("  Motto: 🔥 ¡Arde con pasión!")


class PokemonAgua(Pokemon):
    def __init__(self, nombre: str, ataque: float, defensa: float, salud: float):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Agua"

    def atacar(self, objetivo):
        dano_base = super().atacar(objetivo)
        if dano_base == 0:
            return 0

        if objetivo._tipo == "Fuego":
            dano = dano_base * 2.0
            print("¡Es súper efectivo! 💧🔥")
        elif objetivo._tipo == "Planta":
            dano = dano_base * 0.5
            print("No es muy efectivo... 💧🍃")
        else:
            dano = dano_base

        objetivo.recibir_dano(dano)
        return dano

    def mostrar_info(self):
        super().mostrar_info()
        print("  Motto: 💧 ¡Fluye como el río!")


class PokemonPlanta(Pokemon):
    def __init__(self, nombre: str, ataque: float, defensa: float, salud: float):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Planta"

    def atacar(self, objetivo):
        dano_base = super().atacar(objetivo)
        if dano_base == 0:
            return 0

        if objetivo._tipo == "Agua":
            dano = dano_base * 2.0
            print("¡Es súper efectivo! 🍃💧")
        elif objetivo._tipo == "Fuego":
            dano = dano_base * 0.5
            print("No es muy efectivo... 🍃🔥")
        else:
            dano = dano_base

        objetivo.recibir_dano(dano)
        return dano

    def mostrar_info(self):
        super().mostrar_info()
        print("  Motto: 🌿 ¡Crece con fuerza!")