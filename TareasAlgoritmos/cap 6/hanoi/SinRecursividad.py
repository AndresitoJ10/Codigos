def hanoi(num_discos):
    torre_inicial = list(range(num_discos, 0, -1))
    torre_auxiliar = []
    torre_destino = []

    if num_discos % 2 == 0:
        torre_auxiliar, torre_destino = torre_destino, torre_auxiliar

    total_movimientos = 2**num_discos - 1

    for movimiento in range(1, total_movimientos + 1):
        if movimiento % 3 == 1:
            mover_disco(torre_inicial, torre_destino)
        elif movimiento % 3 == 2:
            mover_disco(torre_inicial, torre_auxiliar)
        elif movimiento % 3 == 0:
            mover_disco(torre_auxiliar, torre_destino)

    return torre_destino


def mover_disco(desde, hacia):
    if not desde:
        desde.append(hacia.pop())
    elif not hacia:
        hacia.append(desde.pop())
    elif desde[-1] < hacia[-1]:
        hacia.append(desde.pop())
    else:
        desde.append(hacia.pop())
