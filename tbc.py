import random

class Character:
    def __init__(self, name, hit_points, hit_chance, max_damage, armor):
        self.name = name
        self.hit_points = hit_points
        self.hit_chance = hit_chance
        self.max_damage = max_damage
        self.armor = armor
        
    
    def is_alive(self):
        return self.hit_points > 0
    
    def print_stats(self):
        print(f"{self.name} - Health: {self.hit_points}, Armor: {self.armor}")
            
def combat_loop(hero, enemy):
    while hero.is_alive() and enemy.is_alive():
        for attacker, defender in [(hero, enemy), (enemy, hero)]:
            if random.randint(1, 100) <= attacker.hit_chance:
                max_damage = random.randint(1, attacker.max_damage)
                damage_after_armor = max(0, max_damage - defender.armor)
                defender.hit_points -= damage_after_armor
                
                print(f"{attacker.name} hits {defender.name} for {damage_after_armor} points of damage.")
                print(f"{defender.name}'s armor absorbs {defender.armor} points.")
            else:
                print(f"{attacker.name}'s attack DID NO DAMAGE LOL to {defender.name}")
                
            # Print stats after each attack
            hero.print_stats()
            enemy.print_stats()

        # Pause for user input before the next round
        input("Press Enter to continue to the next round...")

    if hero.is_alive():
        print(f"{hero.name} DEFEATS {enemy.name}!")

if __name__ == "__main__":
            hero = Character(name="Mario", hit_points=10, hit_chance=50, max_damage=5, armor=2)
            enemy = Character(name="Bowser", hit_points=20, hit_chance=30, max_damage=5, armor=0)

            hero.print_stats()
            enemy.print_stats()