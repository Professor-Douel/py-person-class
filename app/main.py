class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]
        instance = Person.people[name]

        if "wife" in person and person["wife"]:
            instance.wife = instance.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            instance.husband = instance.people[person["husband"]]

    return person_list
