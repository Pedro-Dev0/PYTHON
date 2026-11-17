status = "indisponivel"

match status:
    case "disponivel":
        print("online para conversar")
    case "ausente":
        print("indisponivel para conversar")
    case "indisponivel":
        print("não consegue conversar no momento ocupada")
    case _:
        print("Offline")
