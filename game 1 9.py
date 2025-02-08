import random
from termcolor import colored

class Monster:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health       

    def attack(self):
        """Genera un ataque con daño aleatorio y tipo de daño."""
        roll = random.randint(0, 9)
        if roll == 0:  # Crítico
            damage = random.randint(11, 15)
            damage_type = colored("CRÍTICO", "red")
        elif roll == 1:  # Daño bajo
            damage = random.randint(5, 8)
            damage_type = colored("BAJO", "blue")
        else:  # Daño normal
            damage = random.randint(8, 11)
            damage_type = colored("NORMAL", "yellow")
        
        return damage, damage_type

# Generar nombres aleatorios
def random_monster_name():
    return random.choice(["Dragón", "Ogro", "Duende", "Medusa", "Esqueleto"])

def random_human_name():
    return random.choice(["Mago", "Rey", "Nigromante"])

# Función para calcular el daño
def apply_damage(attacker_damage, defender_health):
    return max(defender_health - attacker_damage, 0)  # Evitar salud negativa

# Función para colorear la salud según el nivel
def health_color(health):
    if health >= 50:
        return colored(str(health), "green")
    elif health >= 20:
        return colored(str(health), "yellow")
    else:
        return colored(str(health), "red")

# Función de combate
def battle_round(attacker, defender):
    damage, damage_type = attacker.attack()
    defender.health = apply_damage(damage, defender.health)

    print(colored(f"{attacker.name} ataca con {damage} de daño", "magenta"), f"({damage_type})")
    print(colored(f"Salud restante de {defender.name}: ", "cyan") + health_color(defender.health) + "\n")

    return defender.health == 0

# Bucle de juego
while True:
    # Crear personajes
    new_monster = Monster(random_monster_name(), 15, random.randint(50, 100))
    new_human = Monster(random_human_name(), 15, random.randint(50, 100))

    print(colored(f"\nMonstruo: {new_monster.name}, Salud: ", "red") + health_color(new_monster.health))
    print(colored(f"Humano: {new_human.name}, Salud: ", "blue") + health_color(new_human.health) + "\n")
    print(colored("***** COMIENZA EL COMBATE *****", "green"))
    input("Presiona Enter para continuar...\n")

    # Simulación de combate
    while new_monster.health > 0 and new_human.health > 0:
        if battle_round(new_monster, new_human):
            print(colored(f"\n{new_monster.name} GANA EL COMBATE!", "green"))
            break
        if battle_round(new_human, new_monster):
            print(colored(f"\n{new_human.name} GANA EL COMBATE!", "green"))
            break

    # Preguntar si quiere jugar otra vez
    retry = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
    if retry != "s":
        print(colored("Gracias por jugar. ¡Hasta la próxima!", "magenta"))
        break
