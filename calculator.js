function calculate(str){
    function check(arr,symbole){
        for (let i = 0; i < arr.length; i++) {
            if(arr[i] == symbole) return true;
        }
        return false;
    }
    function factorial(num){
        if(num == 1) {
            return 1;
        }else if(num>1){
            return num*factorial(num-1);
        }
    }
    //finding tan,sin,cos,log
    while(/tan[(](.)*[)]/.test(str)){
        let temp = str.match(/tan[(](.)*[)]/)[0];
        str = str.replace(temp,Math.tan(calculate(temp.slice(4,temp.length-1))))
    }
    while(/sin[(](.)*[)]/.test(str)){
        let temp = str.match(/sin[(](.)*[)]/)[0];
        str = str.replace(temp,Math.sin(calculate(temp.slice(4,temp.length-1))))
    }
    while(/cos[(](.)*[)]/.test(str)){
        let temp = str.match(/cos[(](.)*[)]/)[0];
        str = str.replace(temp,Math.cos(calculate(temp.slice(4,temp.length-1))))
    }
    while(/log[(](.)*[)]/.test(str)){
        let temp = str.match(/log[(](.)*[)]/)[0];
        str = str.replace(temp,Math.log10(calculate(temp.slice(4,temp.length-1))))
    }
    
    //calculating inside (...) 
    while(/[(](.)*[)]/.test(str)){
       let string = str.match(/[(]([^(|^)]*)[)]/);
        string2 = string[0].slice(1,string[0].length-1);
        //5(20) => 5 * 20 insted if 520
        if(/\d/.test(str[string.index-1])){
            str = str.replace(string[0],`*${calculate(string2)}`)
        }else{
        str = str.replace(string[0],calculate(string2))
        }
        
    }


    let i =0,arr = [];
    let reg1 = /[%,!,e,√,π,^,*,/,+,--]/;
    let str2 = ""
    //string => array
    for(i = 0;i<str.length;i++){
        
        if(reg1.test(str[i])){
            if(str2 != ""){
                arr.push(parseFloat(str2));
                str2 = "";
            }
            arr.push(str[i]);
        }else{
            str2 += str[i];
            if(i == str.length-1){
                arr.push(parseFloat(str2));
            }
        }
        
    }
    for(i =0;i<arr.length;i++){
        if(arr[i] == "-"&&(arr[i-1] == undefined ||/\D/.test(arr[i-1]))){
            arr[i+1] *= -1;
            arr.splice(i,1)
        }
        if(arr[i] == "+"&&(arr[i-1] == undefined ||/\D/.test(arr[i-1]))){
            arr.splice(i,1)
        }
        
    }

    while(check(arr,'!')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '!'){
                arr[j-1] = factorial(Math.floor(arr[j-1]));
                arr.splice(j,1);
                j-=1;
            }
        }
    }
    
    while(check(arr,'e')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == 'e'){
                arr[j-1] *= Math.pow(10,arr[j+1]);
                arr.splice(j,2);
                j-=1;
            }
        }
    }
    
    while(check(arr,'π')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == 'π'&& (arr[j-1]=="*"||arr[j-1] == undefined)){
                arr[j] = Math.PI;
                j-=1;
            }else if(arr[j]== "π"){
                let temp = arr.slice(0,j);
                temp.push(...["*",Math.PI]);
                temp.push(...arr.slice(j+1,));
                arr = temp;
                j-=1;
            }
        }
    }
    while(check(arr,'√')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '√'){
                arr[j+1] = Math.sqrt(arr[j+1]);
                arr.splice(j,1);
                j-=1;
            }
        }
    }
    
    while(check(arr,'^')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '^'){
                arr[j-1] = Math.pow(arr[j-1],arr[j+1]);
                arr.splice(j,2);
                j-=1;
            }
        }
    }
    while(check(arr,'%')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '%'){
                arr[j-1] = arr[j-1]%arr[j+1];
                arr.splice(j,2);
                j-=1;
            }
        }
    }
    while(check(arr,'*')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '*'){
                arr[j-1] *= arr[j+1];
                arr.splice(j,2);
                j-=1;
            }
        }
    }
    while(check(arr,'/')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '/'){
                arr[j-1] /= arr[j+1];
                arr.splice(j,2);
                j-=1;
            }
        }
    }
    while(check(arr,'+')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '+'){
                arr[j-1] += arr[j+1];
                arr.splice(j,2);
                j-=1;
            }
        }
    }
    while(check(arr,'-')){
        for(j =0;j<arr.length;j++){
            if(arr[j] == '-'){
                arr[j-1] -= arr[j+1];
                arr.splice(j,2);
                j-=1;
            }
        }
    }
    
    return arr[0]
}
let str = "(7-3)+(1*(5+5))"
console.log(calculate(str))