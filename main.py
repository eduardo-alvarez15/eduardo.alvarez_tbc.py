import tbc

def main():
    hero = tbc.Character(name="Mario", hit_points=10, hit_chance=50, max_damage=5, armor=2)
    enemy = tbc.Character(name="Bowser", hit_points=20, hit_chance=30, max_damage=5, armor=0)
         
    hero.print_stats()
    enemy.print_stats()

    tbc.combat_loop(hero, enemy)

if __name__ == "__main__":
    main()
    