//notas por matéria
//https://trello.com/b/Icu1eaQ9/trabalho-desenvolvimento-web

let dias_prova = 3;
let qntd_cap = 10;

let cap_p_dia = qntd_cap/dias_prova;

if (cap_p_dia >=5){
    console.log("Cronograma pesado! Tem que estudar ",cap_p_dia.toFixed(2)," capitulos por dia")
}
if (cap_p_dia <=2){
    console.log("Cronograma leve! Tem que estudar ",cap_p_dia.toFixed(2)," capitulos por dia")
}
if (2<cap_p_dia && cap_p_dia<5 ){
    console.log("Cronograma médio! Tem que estudar ",cap_p_dia.toFixed(2)," capitulos por dia")
}




