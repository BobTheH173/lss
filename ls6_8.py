class BuildingError(Exception):
    def __str__(self):
        return f"With this much material the house cannot be built"


def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "Enough material"
    else:
        raise BuildingError(amount_of_material)


materials = 150
print(check_material(materials, 300))
