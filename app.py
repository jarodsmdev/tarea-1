
def crear_pares(q_students):
    # DECLARACION DE VARIABLES

    # DECLARACION DE ARRAY
    list_students = []

    # DECLARACION DE PARES
    pair = []

    # LLENADO DEL ARRAY CON CANTIDAD DE ALUMNOS
    for i in range(q_students):
        list_students.append(i)

    for student in list_students:
        # print("Estudiante: ", student)
        for i in list_students:
            if i != list_students[student] and i > list_students[student]:
                pair.append((list_students[student], i))

    print(pair)
    print(f"Cantidad de rotaciones {len(pair)}.") 
    return len(pair)  

def tiempo_necesario(rotations, time_work):
    timeAll = rotations * time_work
    horas = timeAll/60
    print(f"Tiempo mínimo: {timeAll} minutos ({horas} horas).")
    return timeAll

    
if __name__ == "__main__":
    q_students = int(input("Cantidad de alumnos: "))
    time_work = int(input("Tiempo minimo a trabajar (en minutos): "))

    # crear_pares(q_students)
    tiempo_necesario(crear_pares(q_students), time_work)