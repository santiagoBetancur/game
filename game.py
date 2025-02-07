import random
from termcolor import colored

class Monster:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health       

    def attack(self):
        damage_ = random.randint(1, self.damage)  # Daño aleatorio entre 1 y su daño máximo
        return damage_

    # Método para calcular daño con tipo de daño
    def damage_percent(self):
        roll = random.randint(0, 9)
        if roll == 0:  # Crítico
            damage = random.randint(11, 15)
            damage_type = "CRÍTICO"
        elif roll == 1:  # Daño bajo
            damage = random.randint(5, 8)
            damage_type = "BAJO"
        else:  # Daño normal
            damage = random.randint(8, 11)
            damage_type = "NORMAL"
        
        return damage, damage_type

# Generar nombres aleatorios para monstruos y humanos
def random_monster_name():
    names = ["Dragón", "Ogro", "Duende", "Medusa", "Esqueleto"]
    return random.choice(names)

def random_human_name():
    names = ["Mago", "Rey", "Nigromante"]
    return random.choice(names)

# Función para calcular el resultado de un ataque
def apply_damage(attacker_damage, defender_health):
    remaining_health = defender_health - attacker_damage
    return max(remaining_health, 0)  # Evitar salud negativa

# Crear personajes aleatorios
new_monster = Monster(random_monster_name(), 15, random.randint(50, 100))
new_human = Monster(random_human_name(), 15, random.randint(50, 100))

# Mostrar los atributos iniciales
print(f"Monstruo creado: {new_monster.name}, Daño Máx: {new_monster.damage}, Salud: {new_monster.health}")
print(f"Humano creado: {new_human.name}, Daño Máx: {new_human.damage}, Salud: {new_human.health}")
print("***** COMIENZA EL COMBATE *****\n")
input()

# Simular combate
while new_monster.health > 0 and new_human.health > 0:
    # Monstruo ataca al humano
    monster_attack_damage, damage_type = new_monster.damage_percent()
    new_human.health = apply_damage(monster_attack_damage, new_human.health)
    print(f"{new_monster.name} ataca con {monster_attack_damage} de daño ({damage_type}). Salud restante de {new_human.name}: {new_human.health}")
    
    # Verificar si el humano ha sido derrotado
    if new_human.health == 0:
        print(f"\n{new_monster.name} es el ganador del combate!")
        input()
        break

    # Humano ataca al monstruo
    human_attack_damage, damage_type = new_human.damage_percent()
    new_monster.health = apply_damage(human_attack_damage, new_monster.health)
    print(f"{new_human.name} ataca con {human_attack_damage} de daño ({damage_type}). Salud restante de {new_monster.name}: {new_monster.health}")
    
    # Verificar si el monstruo ha sido derrotado
    if new_monster.health == 0:
        print(f"\n{new_human.name} es el ganador del combate!")
        input()
        break
