import random

class User:
    def __init__(self, name: str, profession: str):
        self.name = name
        self.profession = profession

class Engineer(User):
    def __init__(self, name: str):
        super().__init__(name, "Engineer")

class Technician(User):
    def __init__(self, name: str):
        super().__init__(name, "Technician")

class Politician(User):
    def __init__(self, name: str):
        super().__init__(name, "Politician")

class ComputerEngineer(Engineer):
    def __init__(self, name: str):
        super().__init__(name)

class ElectricalEngineer(Engineer):
    def __init__(self, name: str):
        super().__init__(name)

class MechanicalEngineer(Engineer):
    def __init__(self, name: str):
        super().__init__(name)

CLASS_REGISTRY = {
    "User": User,
    "Engineer": Engineer,
    "Technician": Technician,
    "Politician": Politician,
    "ComputerEngineer": ComputerEngineer,
    "ElectricalEngineer": ElectricalEngineer,
    "MechanicalEngineer": MechanicalEngineer,
}

def make_dynamic_class():
    new_class_name = input("Please enter the name of new class: ").strip()
    base_name = input("Please enter name of base class (blank if none): ").strip()
    new_method_name = input(f"Please enter name of new method for class {new_class_name}: ").strip()
    new_attr_name = input(f"Please enter name of new attribute for class {new_class_name}: ").strip()

    if base_name:
        if base_name not in CLASS_REGISTRY:
            print(f"Base class '{base_name}' does not exist. Aborting.")
            return None
        bases = (CLASS_REGISTRY[base_name],)
    else:
        bases = (object,)

    def dynamic_method(self):
        print(f"{new_class_name}.{new_method_name} called")

    namespace = {
        new_method_name: dynamic_method,
        new_attr_name: random.randint(1, 10**6),
    }

    new_cls = type(new_class_name, bases, namespace)

    CLASS_REGISTRY[new_class_name] = new_cls

    print(f"Class {new_class_name} created with base class: {base_name or 'None'}")
    print(f"Class __name__ is: {new_cls.__name__}")
    print(f"Class __dict__ is: { {k: type(v).__name__ for k, v in new_cls.__dict__.items()} }")

    return new_cls


def main():
    created = make_dynamic_class()
    if created:
        obj = created()
        for name, val in created.__dict__.items():
            if callable(val) and not (name.startswith("__") and name.endswith("__")):
                getattr(obj, name)()
    

if __name__ == "__main__":
    main()