'use strict'

var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 4, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [2, 4, 3]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    }
];

console.log(groupmates);

let rpad = function(str, length) {
// js не поддерживает добавление нужного количества символов
// справа от строки, т.е. аналога ljust из Python здесь нет
str = str.toString(); // преобразование в строку
while (str.length < length){
str = str + ' '; // добавление пробела в конец строки return str; // когда все пробелы добавлены, возвратить строку
return str;
}
};

let printStudents = function(students){
console.log(
rpad("Имя", 15),
rpad("Фамилия", 15),
rpad("Группа", 8),
rpad("Оценки", 20)
);
// был выведен заголовок таблицы
for (let i = 0; i<students.length; i++){
// в цикле выводится каждый экземпляр студента
console.log(
rpad(students[i]['name'], 15),
rpad(students[i]['surname'], 15),
rpad(students[i]['group'], 8),
rpad(students[i]['marks'], 20)
);
}
console.log('\n'); // добавляетсяпустаястрокавконцевывода
};
printStudents(groupmates);


function groupsort(students){
let x = prompt("Текст окна запроса", "Заполнитель поля ввода");
for (let i = 0; i<students.length; i++){
    if(students[i]['group']==x){
        console.log(students[i]['name']);
    }
}
}

groupsort(groupmates);


function ratesort(students, score){
    for(let i = 0; i<students.length;i++){
        let current = 0;
        for(let j = 0; j<(students[i]['marks']).length; j++){
            current = current + students[i]['marks'][j];
        }
        current = current/students[i]['marks'].length;
        if(current>score){
            console.log(students[i]['surname']);
        }
    }
}
ratesort(groupmates, 4);