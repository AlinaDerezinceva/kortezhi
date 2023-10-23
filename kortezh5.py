def good_students(students):
    a = 0
    for student in students:
        a += student[2]
    a /= len(students)

    names = []
    for student in students:
        if student[2] > a:
            names.append(student[0])

    shortNames = ''
    for name in names:
        end = name.index(' ')
        shortNames += f'{name[:end]}, '

    return f"Ученики {shortNames[:-2]} в этом семестре хорошо учатся!"

students = (("Левина Алина Александровна", 17, 4, "Черепаново"),
            ("Гришина Анна Александровна", 17, 3, "Черепаново"),
            ("Геньш Данил Константинович", 17, 5, "Бердск"),
            ("Утенко Марина Сергеевна", 17, 5, "Черепаново"),
            ("Бобровская Анастасия Дмитриевна", 18, 5, "Стрежевой"),
            ("Щербина Екатерина Ивановна", 16, 4, "Искитим"),
            ("Федореев Всеволод Константинович", 17, 3, "Новосибирск"))
print(good_students(students))