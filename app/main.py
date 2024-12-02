class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_list.append(Person(name, age))

    for person in people:
        name = person["name"]
        instance = Person.people[name]

        if "wife" in person and person["wife"]:
            instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            instance.husband = Person.people[person["husband"]]

    return person_list
