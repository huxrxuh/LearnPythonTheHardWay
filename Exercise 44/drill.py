from random import randint

def Person_new(name, age, eyes, health, attack, defense):
    """Creates a new person dict and attaches the talk() function."""
    person = {
        "name": name,
        "age": age,
        "eyes": eyes,
        "health": health,
        "attack": attack,
        "defense": defense,
        }
    def talk(words):
        """Closure that has access to the person created at the top"""
        print(f"I am {person['name']} and {words}")

    person['talk'] = talk

    def hit(foe):
        """This function simulates one person hitting another"""
        damage = randint(1, person['attack'])
        print(f"{person['name']} hit {foe['name']}")
        if damage > foe['defense']:
            if foe['health'] - damage + foe['defense'] > 0:
                print(f"That was efective, {foe['name']} loses {damage - foe['defense']} HP.")
                foe['health'] -= (damage - foe['defense'])
            else:
                print(f"{foe['name']} fainted. {person['name']} wins!")
                foe['health'] = 0
        else:
            print(f"{foe['name']} dodged {person['name']}'s attack.")

    person['hit'] = hit

    return person

becky = Person_new("Becky", 39, "green", 50, 35, 10)

arthur = Person_new("Arthur", 43, "blue", 50, 25, 10)

becky['talk']("I am talking here!")

arthur['talk']("You sir, are a fish!")

print("FIGHT!")

while arthur['health'] > 0 and becky['health'] > 0:
    arthur['hit'](becky)
    if becky['health'] > 0:
        becky['hit'](arthur)

