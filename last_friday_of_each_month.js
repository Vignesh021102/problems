/*
Write a function that returns the date of the last Friday of a given month for a given year.
*/

function lastFriday(year,month){
    month-=1;
    let friday = 0;
    for(let i =15;i<35;i++){
        let date = new Date(year,month,i)
        if(date.getMonth() != month){
            break;
        }
        if(date.getDay() == 5){
            friday = i;
        }
    }
    console.log(friday);
    return friday;
}
lastFriday(2018, 1) //should return 26.

lastFriday(2017, 2) //should return 24.

lastFriday(2012, 3) //should return 30.

lastFriday(1900, 4) //should return 27.

lastFriday(2000, 5) //should return 26.

lastFriday(2006, 6) //should return 30.

lastFriday(2010, 7) //should return 30.

lastFriday(2005, 8) //should return 26.
