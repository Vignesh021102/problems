/*
Calculate the Shannon entropy H of a given input string.

Given the discreet random variable  X  that is a string of  N  "symbols" (total characters) consisting of  n  different characters (n=2 for binary), the Shannon entropy of X in bits/symbol is:

H2(X)=  −∑ni=1  counti/N (log2(counti/N)) 
where  counti  is the count of character  ni .
*/
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

entropy("abcanc")
