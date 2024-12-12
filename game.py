import random

class Monster:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health       

    def attack(self):
        damage_ = random.randint(1, self.damage)  # Daño aleatorio entre 1 y su daño máximo
        return damage_

# Generar nombres aleatorios para monstruos y humanos
def random_monster_name():
    names = ["Dragón", "Ogro", "Duende", "Meduza", "Esqueleto"]

    return random.choice(names)

def random_human_name():
    names = ["Mago", "Rey", "Nigromante"]
    return random.choice(names)

# Función para calcular el resultado de un ataque
def apply_damage(attacker_damage, defender_health):
    remaining_health = defender_health - attacker_damage
    remaining_health = max(remaining_health, 0)  # Evitar salud negativa
    return remaining_health

# Crear personajes aleatorios
new_monster = Monster(random_monster_name(), random.randint(5, 15), random.randint(50, 100))
new_human = Monster(random_human_name(), random.randint(5, 15), random.randint(50, 100))

# Mostrar los atributos iniciales
print(f"Monstruo creado: {new_monster.name}, Daño: {new_monster.damage}, Salud: {new_monster.health}")
print(f"Humano creado: {new_human.name}, Daño: {new_human.damage}, Salud: {new_human.health}")
print("***** COMIENZA EL COMBATE *****")

input()
# Simular combate
while new_monster.health > 0 and new_human.health > 0:
    # Monstruo ataca al humano
    monster_attack_damage = new_monster.attack()
    new_human.health = apply_damage(monster_attack_damage, new_human.health)
    print(f"{new_monster.name} ataca con {monster_attack_damage} de daño. Salud restante de {new_human.name}: {new_human.health}")
    print("")
    #input()
    
    # Verificar si el humano ha sido derrotado
    if new_human.health == 0:
        print(f"{new_monster.name} es el ganador del combate!")
        break

    # Humano ataca al monstruo
    human_attack_damage = new_human.attack()
    new_monster.health = apply_damage(human_attack_damage, new_monster.health)
    print(f"{new_human.name} ataca con {human_attack_damage} de daño. Salud restante de {new_monster.name}: {new_monster.health}")

    # Verificar si el monstruo ha sido derrotado
    if new_monster.health == 0:
        print(f"{new_human.name} es el ganador del combate!")
        break
