def opcion(msg: str):
    def opcion(func):
        def menu(*args, **kwargs):
            print(msg)
            opcion = None
            try:
                opcion = int(input("> ").strip())
            except Exception as e:
                print(f"Opcion no valida: {e}")
                return True
            return func(opcion)
        return menu
    return opcion