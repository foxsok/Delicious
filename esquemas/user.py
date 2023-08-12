def CafesEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "Nombre": item["Nombre"],
        "Descripción": item["Descripción"],
        "Precio": item["Precio"],
        "Tipo": item["Tipo"],
    }


def CafeEntity(entity) -> list:
    return [CafesEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]