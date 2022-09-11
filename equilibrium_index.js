/*
An equilibrium index of a sequence is an index into the sequence such that the sum of elements at lower indices is equal to the sum of elements at higher indices.

For example, in a sequence  A :

A0=−7 
A1=1 
A2=5 
A3=2 
A4=−4 
A5=3 
A6=0 
3 is an equilibrium index, because:

A0+A1+A2=A4+A5+A6 
6 is also an equilibrium index, because:

A0+A1+A2+A3+A4+A5=0 
(sum of zero elements is zero)

7 is not an equilibrium index, because it is not a valid index of sequence  A .

Write a function that, given a sequence, returns its equilibrium indices (if any).


*/


function equilibrium(a) {
    if(a == undefined) return undefined;
    if(a == []) return [];

    function add(array,start,end){
        if(array.lenth > end) return undefined;
        let sum = 0;
        for(let i = start;i<=end;i++){
            sum+=array[i]
        }
        //console.log(sum,start,end,a.slice(start,end+1));
        return sum;
    }

    let sum=0,result = [];
    for(let i =0;i <a.length;i++){
        //console.log(i," = ",a[i]);
        if(i === 0){
            if(add(a,i+1,a.length-1) == 0) result.push(i);
        }else if(i === a.length-1){
            if(add(a,0,i-1) == 0) result.push(i);
        }else if (add(a,0,i-1) == add(a,i+1,a.length-1)){
            result.push(i);
        }
    }

    //console.log(result);
    return result;
}
equilibrium([-7, 1, 5, 2, -4, 3, 0])
