document.write('<img class="chara" src = "../static/img/character (' + result + ').png">');
/*result=Number(result);*/
if (result<=50){
    var star=1;
}
else if(result<=80){
    var star=2;
}
else if(result<=100){
    var star=3;
}
else if(result<=110){
    var star=4;
}
else{
    var star=5;
}

for(var i=0; i<star; i++){
    document.write('<img class="star" src="../static/img/star.png">');
}

