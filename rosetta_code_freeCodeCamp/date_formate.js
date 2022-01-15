/*
Return an array with two date strings of the current date with the following specifications:

The first string's date order should be the year number, month number, and day number separated by dashes (-).
The first string's year should be four digits in length.
The first string's month and day should not contain any leading zeros.
The second string's weekday and month names should not be abbreviated.
The second string's day should not contain any leading zeros.
*/

function getDateFormats() {
    let day,dayOweek,month,year,monthS;
    let date  = new Date();
    switch(date.getDay()){
        case 0:
            dayOweek = "Sunday";
            break;
        case 1:
            dayOweek = "Monday";
            break;
        case 2:
            dayOweek = "Tuesday";
            break;
        case 3:
            dayOweek = "Wednesday";
            break;
        case 4:
            dayOweek = "Thursday";
            break;
        case 5:
            dayOweek = "Fridayday";
            break;
        case 6:
            dayOweek = "Saturday";
            break;
    }
    day = date.getDate()
    year = date.getFullYear();
    month = date.getMonth()
    switch(month){
        case 0:
            monthS = "January";
            break;
        case 1:
            monthS = "February";
            break;
        case 2:
            monthS = "March";
            break;
        case 3:
            monthS = "April";
            break;
        case 4:
            monthS = "May";
            break;
        case 5:
            monthS = "June";
            break;
        case 6:
            monthS = "July";
            break;
        case 7:
            monthS = "August";
            break;
        case 8:
            monthS = "September";
            break;
        case 9:
            monthS = "October";
            break;
        case 10:
            monthS = "November";
            break;
        case 11:
            monthS = "December";
            break;
    }
    return [`${year}-${month+1}-${day}`,`${dayOweek} ,${monthS} ${day}, ${year}`]
}
console.log(getDateFormats())