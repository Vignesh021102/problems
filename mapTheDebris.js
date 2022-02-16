function orbitalPeriod(arr) {
    var array = [];
    var GM = 398600.4418;
    var earthRadius = 6367.4447
    for(let i =0;i<arr.length;i++){
        let oP = Math.round(2* Math.PI * Math.sqrt(((arr[i].avgAlt+earthRadius) ** 3) / GM));
        array.push({name: arr[i].name,orbitalPeriod: oP})
    }
    console.log(array);
    return array;
  }
orbitalPeriod([{name : "sputnik", avgAlt : 35873.5553}])
