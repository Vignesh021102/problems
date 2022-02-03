function longestString(arr) {
    let max = 0;
    arr.forEach(element => {
        if(max<element.length) max = element.length;
    });
    let list = [];
    for(let i =0;i<arr.length;i++){
        if(arr[i].length == max) list.push(arr[i])
    }
    return list;
}

console.log(longestString(["a","as","e","ab"]));