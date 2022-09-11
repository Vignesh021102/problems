/*
Write a function to generate a string output which is the concatenation of input words from a list/sequence where:

1.An input of no words produces the output string of just the two brace characters ("{}")
2.An input of just one word, e.g. ["ABC"], produces the output string of the word inside the two braces, e.g. "{ABC}"
3.An input of two words, e.g. ["ABC", "DEF"], produces the output string of the two words inside the two braces with the words separated by the string " and ", e.g. "{ABC and DEF}"
4.An input of three or more words, e.g. ["ABC", "DEF", "G", "H"], produces the output string of all but the last word separated by ", " with the last word separated by " and " and all within braces; e.g. "{ABC, DEF, G and H}"
*/

function quibble(words) {
    if(words == undefined) return undefined;
    if(words.length == 0) return `{}`;
    if(words.length ==1 ) return `{${words[0]}}`
    return `{${words.slice(0,-1).join(",")} and ${words[words.length-1]}}`
}
