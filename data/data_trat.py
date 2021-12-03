data = open('lesmis.txt','r')
arq_escrita = open('lesmis2.txt', 'w')
with data, arq_escrita:
    for line in data:
        if 'node' in line:
            arq_escrita.write(f"{line.strip()}\n")
            next(data)
            arq_escrita.write(f"{next(data).strip()}\n")
            arq_escrita.write(f"{next(data).strip()}\n")
            next(data)

        if 'edge' in line:
            arq_escrita.write(f"{line.strip()}\n")
            next(data)
            arq_escrita.write(f"{next(data).strip()}\n")
            arq_escrita.write(f"{next(data).strip()}\n")
            arq_escrita.write(f"{next(data).strip()}\n")
            next(data)

        # line = line.split(',')
        # if line[0] not in grafo:
        #     vertices.append(line[0])
        #     grafo[line[0]] = {}
        # grafo[line[0]][line[1]] = int(line[2].strip())

 