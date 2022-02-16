function fearNotLetter(str) {
    const array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
    var num;
    var string = "";

    for (let i = 0; i < str.length; i++) {
        let bool = false;

        for (let j = 0; j < array.length; j++) {
            if (str[0] == array[j]) {
                num = j;
                break;
            }
        }
    }

    for (let i = num+1;i < (str.length+num);i++) {
        let bool = false
        for(let j = 0;j < str.length;j++) {
            if (array[i] == str[j]) {
                bool = true;
            }
            console.log(array[i],str[j],bool);
        }

        if (!bool) {
            string+=array[i]
        }
    }
    if (string == "") {
        string = undefined
    }
    console.log(string);
    return string;
}

  fearNotLetter("dbcdefghijalmnopqstuvwxyz");