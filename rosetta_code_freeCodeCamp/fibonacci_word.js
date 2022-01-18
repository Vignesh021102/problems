/*
The Fibonacci Word may be created in a manner analogous to the Fibonacci Sequence as described here:

Define  F_Word1  as  1
Define  F_Word2  as  0
Form   F_Word3  as  F_Word2   concatenated with  F_Word1   i.e.:  01
Form   F_Wordn  as  F_Wordn-1  concatenated with  F_wordn-2
Write a function to return the Fibonacci Words up to n. n will be provided as a parameter to the function. The function should return an array of objects. The objects should be of the form: { N: 1, Length: 1, Entropy: 0, Word: '1' }.
*/

function fibWord(num) {
    //function to calculate entropy
    function entropy(str) {
        let N,n,i,j,count,sum = 0;
        N = str.length;
        // removing duplicate values in str
        str = str.split("")
        for(i =0;i<str.length;i++){
            str[i] = {id:str[i],num:1}; 
        }
        for(i = 0;i<str.length;i++){
            for(j = i;j<str.length;j++){
                if(str[i].id == str[j].id && i != j){
                    str.splice(j,1);
                    str[i].num++;
                    j--;
                }
            }
        }
        //console.log(str);
        for(i =0;i<str.length;i++){
           sum += (str[i].num/N)*Math.log2(str[i].num/N)
        }
        sum = -1 * sum;
        return sum;
    }

    let i = 1,n1 ="1",n2="0",n3;
    let arr = [],obj;
    while(i <= num){
        obj = {};
        if(i ==  1){
            n3 = "1"
        }else if(i == 2){
            n3 = "0"
        }else{
            n3 = n2+n1;
            n1= n2;
            n2= n3;
        }
        obj.N = i;
        obj.Length = n3.length;
        obj.Entropy = entropy(n3);
        obj.Word = n3;
        i++;
        //console.log(obj);
        arr.push(obj)
    }
    //console.log(arr);
    return arr;
}
fibWord(5)
