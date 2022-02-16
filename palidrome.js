const Delete =(arr,index)=>{
    arr.splice(index,1);
    return arr;
}

function palindrome(str) {
    str = str.toLowerCase();
    var string = "";
    str = str.split("");
    for(let i =0;i<str.length;i++){
        //console.log(/[a-z]/.test(str[i]),str[i]);
        if (!/[a-z0-9]/.test(str[i])) {
            str = Delete(str,i);
            i--;
        }
        //console.log(str);
    }
    str = str.join(" ");
    console.log(str);
    let i = 0;
    let j = str.length-1;
    let bool = true;
    while(i<j){
        i++;
        j--;
        if (str[i]!=str[j] && i != j) {
            console.log("False");
            return false
        }
    }
    console.log("True");
    return true;
  }
  
  
  
  palindrome("Ey45E");
  palindrome("My age is 0, 0 si ega ym.");
  palindrome("0_0 (: /-\ :) 0-0");
  palindrome("five|\_/|four");
  palindrome("1 eye for of 1 eye.");