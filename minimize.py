class State:
    def __init__(self, label):
        self.label = label
        self.transitions = []


class AFD:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.states = []


def minimize_afd(afd):
    # Paso 1: Identificar estados distinguibles
    grupos = []
    dist = set()
    for i in range(len(afd.states)):
        for j in range(i):
            if (afd.states[i] in afd.end) != (afd.states[j] in afd.end):
                dist.add((i, j))
    grupos.append(set(range(len(afd.states))) - dist)
    grupos.append(dist)

    # Paso 2: Crear tabla de estados no distinguibles
    tabla = [[False for _ in range(len(grupos))] for _ in range(len(grupos))]
    for i in range(len(grupos)):
        for j in range(i):
            if any((a.label, c) in b.transitions for a in grupos[i] for b in grupos[j] for c in afd.alphabet):
                tabla[i][j] = True
                tabla[j][i] = True

    # Paso 3: Actualizar tabla de estados no distinguibles
    while True:
        cambios = False
        for i in range(len(grupos)):
            for j in range(i):
                if not tabla[i][j]:
                    for c in range(len(grupos)):
                        if tabla[i][c] and tabla[j][c]:
                            tabla[i][j] = True
                            tabla[j][i] = True
                            cambios = True
        if not cambios:
            break

    # Paso 4: Crear nuevo conjunto de estados
    nuevos_estados = []
    nuevos_grupos = []
    for i in range(len(grupos)):
        grupo = grupos[i]
        nuevos_estado = State(
            f"{''.join(sorted([afd.states[j].label for j in grupo]))}")
        nuevos_estados.append(nuevos_estado)
        nuevos_grupos.append(grupo)

    # Paso 5: Actualizar transiciones del nuevo conjunto de estados
    for i in range(len(nuevos_estados)):
        for c in afd.alphabet:
            for j in range(len(grupos)):
                grupo = grupos[j]
                estado = grupo.pop()
                nuevos_estado = nuevos_estados[j]
                destino = None
                for k in range(len(grupos)):
                    if estado in grupos[k]:
                        destino = nuevos_estados[k]
                        break
                grupo.add(estado)
                nuevos_estado.transitions.append((c, destino))

    # Paso 6: Identificar nuevo estado inicial y estados finales
    nuevos_iniciales = None
    for estado in nuevos_estados:
        if afd.start in estado.label:
            nuevos_iniciales = estado
            break
    nuevos_finales = []
    for estado in nuevos_estados:
        for s in afd.end:
            if s in estado.label:
                nuevos_finales.append(estado)
                break
    return AFD(nuevos_iniciales, nuevos_finales)
