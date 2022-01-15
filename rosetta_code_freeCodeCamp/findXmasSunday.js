function findXmasSunday(start,end){
    let arr = [];
    for(let i =start;i<=end;i++){
        if(new Date(i,11,25).getDay()== 0) arr.push(i);
    }
    return arr;
}
findXmasSunday(1990,2021);
