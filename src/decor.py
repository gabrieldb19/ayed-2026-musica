def opcion(msg: str):
    def opcion(func):
        def wrapper(*args, **kwargs):
            print(msg)
            op: int
            try:
                op = int(input("> ").strip())
            except Exception as e:
                print(f"Opcion no valida: {e}")
                return True
            return func(op)
        return wrapper
    return opcion