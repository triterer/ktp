groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Петр",
        "surname": "Смирнов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [2, 2, 2]
    }
]
def sorting(students, grade):
    for studen in students:
        n = 0
        sum = 0
        for i in studen['marks']:
            sum = sum + i
            n = n + 1
        if sum/n >=grade:
            print(studen['name'])

sorting(groupmates, 3)
