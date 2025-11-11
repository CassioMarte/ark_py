def format_return(type_route: str, type: str, count: int = 1, attributes: dict | list | None = None) -> dict:
    return {
        "data": {
            "typeRoute": type_route,
            "type": type,
            "count": count,
            "attributes": attributes or {} 
        }
  }