def Person_new(name, age, eyes):
    """Creates a new person dict and attaches the talk() function."""
    person = {
        "name": name,
        "age": age,
        "eyes": eyes,
        }
    def talk(words):
        """Closure that has access to the person created at the top"""
        print(f"I am {person['name']} and {words}")

    person['talk'] = talk

    return person

becky = Person_new("Becky", 39, "green")

becky['talk']("I am talking here!")
