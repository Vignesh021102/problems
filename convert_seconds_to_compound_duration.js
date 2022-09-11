/*Implement a function which:

takes a positive integer representing a duration in seconds as input (e.g., 100), and
returns a string which shows the same duration decomposed into weeks, days, hours, minutes, and seconds as detailed below (e.g., 1 min, 40 sec).
Demonstrate that it passes the following three test-cases:

Test Cases
Input number	Output number
7259	        2 hr, 59 sec
86400	        1 d
6000000	        9 wk, 6 d, 10 hr, 40 min

Details
The following five units should be used: 
Unit	Suffix used in Output	Conversion
week	wk	                    1 week = 7 days
day	    d	                    1 day = 24 hours
hour	hr	                    1 hour = 60 minutes
minute	min	                    1 minute = 60 seconds
second	sec	                    ---
However, only include quantities with non-zero values in the output (e.g., return 1 d and not 0 wk, 1 d, 0 hr, 0 min, 0 sec).
Give larger units precedence over smaller ones as much as possible (e.g., return 2 min, 10 sec and not 1 min, 70 sec or 130 sec).
Mimic the formatting shown in the test-cases (quantities sorted from largest unit to smallest and separated by comma+space; value and unit of each quantity separated by space). */


function convertSeconds(s){
    let week = s/(7*24*60*60);
    let day = (week -Math.floor(week))*7
    let hour = (day -Math.floor(day))*24
    let min = (hour-Math.floor(hour))*60;
    sec = s%60;

 
    let str = [];
    
    if(Math.floor(week) >0){
        str.push(`${Math.floor(week)} wk`)
    }
    if(Math.floor(day) >0){
        str.push(`${Math.floor(day)} d`)
    }
    if(Math.floor(hour) >0){
        str.push(`${Math.floor(hour)} hr`)
    }
    if(Math.floor(min) >0){
        str.push(`${Math.floor(min)} min`)
    }
    if(Math.floor(sec) >0){
        str.push(`${Math.floor(sec)} sec`)
    }
    str = str.join(", ");
    str = str.trim();
    console.log(str);
    return str
}



console.log(convertSeconds(7259))// should return 2 hr, 59 sec.
convertSeconds(86400)// should return 1 d.
convertSeconds(6000000)
