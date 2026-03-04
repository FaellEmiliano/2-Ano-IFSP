//notas por matéria
let bloco_de_materias = [
    [10,9,9],
    [6,4,5],
    [1,10,8],
]
let soma_total = 0

//tira as medias de cada materias(linha do array)
for (let i=0;i<bloco_de_materias.length;i++){
    let soma_materia = 0
    let media_materia = 0

    for (let j=0;j<bloco_de_materias[i].length;j++)
        soma_materia +=bloco_de_materias[i][j]
    media_materia = soma_materia / bloco_de_materias[i].length
    media_materia = Math.round(media_materia * 100) / 100;
    bloco_de_materias[i] = media_materia
    soma_total += bloco_de_materias[i]
}

//media total do bloco
let media_total = soma_total / bloco_de_materias.length
media_total = Math.round(media_total*100)/100
bloco_de_materias = media_total
console.log('Nota: ',bloco_de_materias)

//ve se passou ou nao
if (bloco_de_materias>=6)
    console.log('Aprovado!')
else
    console.log('Reprovado!')







