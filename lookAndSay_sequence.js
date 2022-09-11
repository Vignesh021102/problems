/*
The Look and say sequence is a recursively defined sequence of numbers.

Sequence Definition

Take a decimal number
Look at the number, visually grouping consecutive runs of the same digit.
Say the number, from left to right, group by group; as how many of that digit there are - followed by the digit grouped.
This becomes the next number of the sequence.
An example:

Starting with the number 1, you have one 1 which produces 11
Starting with 11, you have two 1's. I.E.: 21
Starting with 21, you have one 2, then one 1. I.E.: (12)(11) which becomes 1211
Starting with 1211, you have one 1, one 2, then two 1's. I.E.: (11)(12)(21) which becomes 111221
Write a function that accepts a string as a parameter, processes it, and returns the resultant string.
*/
function lookAndSay(str) {
    if(str.length == 1) return str += str
    str = str.match(/\d\d/g);
    for(let i = 0;i<str.length;i++){
        if(str[i].length ==1){
            str[i]+=str[i]
        }else if(str[i][0] == str[i][1]){
            str[i] = `2${str[i][0]}`
        }else{
            str[i] = `1${str[i][0]}1${str[i][1]}`
        }
    }
    return str.join("")
}
lookAndSay("1345")
console.log(lookAndSay("1"));
lookAndSay("1211")
