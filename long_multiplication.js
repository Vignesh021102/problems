/*
Explicitly implement long multiplication.

This is one possible approach to arbitrary-precision integer algebra.

Write a function that takes two strings of large numbers as parameters. Your function should return the product of these two large numbers as a string.

Note: In JavaScript, arithmetic operations are inaccurate with large numbers, so you will have to implement precise multiplication yourself.
*/

function mult(n1,n2){
    n1 = n1.split("").reverse().join("");
    n2 = n2.split("").reverse().join("");
    let temp = "",tempSum = [],sum = [],num;
    for(let i =0;i<n1.length;i++){
        tempSum = [];
        for(let j =0;j<n2.length;j++){
            temp = `${n1[i]*n2[j]}`;
            
            temp = temp.split("").reverse().join("")
            for(let k =0;k<temp.length;k++){
                if(tempSum[j+k]){
                    let l = j+k;
                    num = `${parseInt(tempSum[l])+parseInt(temp[k])}`
                    while(num.length == 2){
                        tempSum[l] = num[1];
                        l++;
                        if(!tempSum[l]){
                            num = num[0]
                        }else{
                            num = `${parseInt(tempSum[l])+parseInt(num[0])}`
                        }
                    }
                    tempSum[l] = num
                }else{
                    tempSum[j+k] = temp[k]
                }
            }
        }
        for(let j =0;j<tempSum.length;j++){
            if(!sum[i+j]){
                sum[i+j] = tempSum[j];
            }else{
                let k = i+j;
                num = `${parseInt(sum[k])+parseInt(tempSum[j])}`
                while(num.length == 2){
                    sum[k] = num[1];
                    k++;
                    if(sum[k]){
                        num = `${parseInt(sum[k])+parseInt(num[0])}`
                    }else{
                        num = num[0];
                    }
                };
                sum[k] = num[0];
            }
        }
    }
    return sum.reverse().join("");
}
console.log(mult("18446744073709551616", "18446744073709551616"));
