/*
Write a function to generate the nth Fibonacci number.

The nth Fibonacci number is given by:

Fn = Fn-1 + Fn-2

The first two terms of the series are 0 and 1.

Hence, the series is: 0, 1, 1, 2, 3, 5, 8, 13...
*/

function fibonacci(num){
    //using recurrsion
    if(num == 1||num == 2){
        return 1
    }else if (num >=3){
        return fibonacci(num-2)+fibonacci(num-1)
    }
}
console.log(fibonacci(10));
//using while loop
function fibonacci(num){
    let n1 = -1,n2 =1,n3 = 0;
    while(num >=0){
        n3= n1+n2;
        n1 = n2;
        n2 = n3;
        num--;
        if(n3 == Infinity){
            break;
        }
    }
    return n3;
}
console.log(fibonacci(10))
