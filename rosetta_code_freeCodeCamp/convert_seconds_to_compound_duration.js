function convertSeconds(s){
    console.log(sec);
    let year = sec/(12*4.34524*7*24*60*60);
    let month = (year -Math.floor(year))*12;
    let week = (month -Math.floor(month))*4.34524;
    let day = (week -Math.floor(week))*7
    let hour = (day -Math.floor(day))*24
    let min = (hour-Math.floor(hour))*60;
    sec = sec/60;

 
    let str = "";
    if(Math.floor(year) > 0){
        str += ` ${Math.floor(year)} year,`
    }
    if(Math.floor(month) >0){
        str += ` ${Math.floor(month)} months,`
    }
    if(Math.floor(week) >0){
        str += ` ${Math.floor(week)} weeks,`
    }
    if(Math.floor(day) >0){
        str += ` ${Math.floor(day)} days,`
    }
    if(Math.floor(hour) >0){
        str += ` ${Math.floor(hour)} hours,`
    }
    if(Math.floor(min) >0){
        str += ` ${Math.floor(min)} mins,`
    }
    if(Math.floor(sec) >0){
        str += ` ${Math.floor(sec)} seconds,`
    }
    console.log(str);
}



function getSeconds(sec,min,hour,day,week,month,year){
    if(sec == undefined) return 0;
    let result = sec;
    if(min == undefined)return result;
    result += (min*60);
    if(hour == undefined)return result;
    result += hour*(60*60);
    if(day == undefined)return result;
    result += day*(60*60*24);
    if(week == undefined)return result;
    result += week*(60*60*24*7);
    if(month == undefined)return result;
    result += month*(60*60*24*7*4.34524);
    if(year == undefined)return year;
    result += year*(60*60*24*7*4.34524*12);
    return result;
}
let sec = getSeconds(60,1);
console.log(sec);
convertSeconds(sec);
