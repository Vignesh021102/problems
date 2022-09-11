/*
A company decides that whenever Xmas falls on a Sunday they will give their workers all extra paid holidays so that, together with any public holidays, workers will not have to work the following week (between the 25th of December and the first of January).

Write a function that takes a start year and an end year and return an array of all the years where the 25th of December will be a Sunday.
*/

function findXmasSunday(start,end){
    let arr = [];
    for(let i =start;i<=end;i++){
        if(new Date(i,11,25).getDay()== 0) arr.push(i);
    }
    return arr;
}
findXmasSunday(1990,2021);
