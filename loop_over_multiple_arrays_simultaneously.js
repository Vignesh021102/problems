/*
Loop over multiple arrays simultaneously
Loop over multiple arrays and create a new array whose  ith  element is the concatenation of  ith  element of each of the given.

For this example, if you are given this array of arrays:

[ ["a", "b", "c"], ["A", "B", "C"], [1, 2, 3] ]
the output should be:

["aA1","bB2","cC3"]
Write a function that takes an array of arrays as a parameter and returns an array of strings satisfying the given description.
*/

function loopSimult(A) {
    let arr = [],str = "";
    console.log(arr);
    for(let i =0;i<A[0].length;i++){
        str = ""
        for(let j =0;j<A.length;j++){
            str += A[j][i];
        }
        arr.push(str);
    }
    return arr;
}
console.log(loopSimult([["a", "b", "c", "d"], ["A", "B", "C", "d"], [1, 2, 3, 4]]));
