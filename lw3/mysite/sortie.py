groupmates = [
    {
        'name':'Василий',
        'group':'912-2',
        'age':19,
        'marks':[4,3,5,5,4]
    },
{
        'name':'Анна',
        'group':'912-1',
        'age':198,
        'marks':[3,3,2,5,4]
    }
]


def print_students(students):
    print('Имя студента\t','Группа\t','Возраст\t','Оценки\t')
    for studen in students:
        print(studen['name'],'\t',studen['group'],'\t',studen['age'],studen['marks'],'\t')
        print('\n')


print_students(groupmates)


def sorting(students, grade):
    for studen in students:
        n = 0
        sum = 0
        for i in studen['marks']:
            sum = sum + i
            n = n + 1
        if sum/n >=grade:
            print(studen['name'])


sorting(groupmates, 4)