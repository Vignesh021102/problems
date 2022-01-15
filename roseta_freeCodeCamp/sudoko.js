// solveSudoku([[8, 1, 9, -1, -1, 5, -1, -1, -1],[-1, -1, 2, -1, -1, -1, 7, 5, -1],[-1, 3, 7, 1, -1, 4, -1, 6, -1],[4, -1, -1, 5, 9, -1, 1, -1, -1],[7, -1, -1, 3, -1, 8, -1, -1, 2],[-1, -1, 3, -1, 6, 2, -1, -1, 7],[-1, 5, -1, 7, -1, 9, 2, 1, -1],[-1, 6, 4, -1, -1, -1, 9, -1, -1],[-1, -1, -1, 2, -1, -1, 4, 3, 8]]) should return [[8, 1, 9, 6, 7, 5, 3, 2, 4],[6, 4, 2, 9, 8, 3, 7, 5, 1],[5, 3, 7, 1, 2, 4, 8, 6, 9],[4, 2, 6, 5, 9, 7, 1, 8, 3],[7, 9, 5, 3, 1, 8, 6, 4, 2],[1, 8, 3, 4, 6, 2, 5, 9, 7],[3, 5, 8, 7, 4, 9, 2, 1, 6],[2, 6, 4, 8, 3, 1, 9, 7, 5],[9, 7, 1, 2, 5, 6, 4, 3, 8]]
/*
function solveSudoku(arr,gridRow,gridColumn){
    function checkRow(row,ele){
        let i;
        for(i=0;i<arr.length;i++){
            if(arr[row][i] == ele) return false;
        }
        return true;
    }
    function checkColumn(col,ele){
        let i;
        for(i=0;i<arr.length;i++){
            if(arr[i][col] == ele) return false;
        }
        return true;
    }
    function grid(row,column,element){
        row = Math.floor(row/gridRow);
        column = Math.floor(column/gridColumn);
        //console.log(row,column);
        for(let i =(row*gridRow);i<(gridRow+(gridRow*row));i++){
            for(let j = (column*gridColumn);j<(gridColumn+(gridColumn*column));j++){
                //console.log("   .",i,j);
                if(arr[i][j] == element) return false;
            }
        }
        return true;
    }
    function isAvailFull(){
        for(let i =0;i<avail.length;i++){
            if(avail[i] < avail.length){
                return false;
            }
        }
        return true;
    }
    let avail = new Array(arr.length).fill(0,0,arr.length);
    let i,j;
    for(i =0;i<arr.length;i++){
        for(j =0;j<arr.length;j++){
            if(arr[i][j] != -1){
                avail[arr[i][j]-1]++;
            }
        }
    }
    let big = 0;
   
    while(!isAvailFull()){
        big = 0;
        for(i =0;i<avail.length;i++){
            if((avail[big] >=avail.length || avail[big]>avail[i]) && avail[i] <avail.length){
                big = i;
            }
        }
        console.log(big);
        if(avail[big] >= avail.length){
            break;
        }
        for(i=0;i<arr.length;i++){
            for(j =0;j<arr[i].length;j++){
                if(checkRow(i,big+1)&&checkColumn(j,big+1)&&avail[big]<avail.length&&grid(i,j,big+1)&&arr[i][j] == -1){
                    arr[i][j] = big+1;
                    avail[big]++;
                }
            }
        }
        console.log(avail);
    }
    console.log("\narr = ");
    arr.forEach(element => {
        console.log(element);
    });
}
*/
function solveSudoku(arr,gridRow,gridColumn){
    function checkRow(row,ele){
        let i;
        for(i=0;i<arr.length;i++){
            if(arr[row][i] == ele) return false;
        }
        return true;
    }
    function checkColumn(col,ele){
        let i;
        for(i=0;i<arr.length;i++){
            if(arr[i][col] == ele) return false;
        }
        return true;
    }
    function grid(row,column,element){
        row = Math.floor(row/gridRow);
        column = Math.floor(column/gridColumn);
        //console.log(row,column);
        for(let i =(row*gridRow);i<(gridRow+(gridRow*row));i++){
            for(let j = (column*gridColumn);j<(gridColumn+(gridColumn*column));j++){
                //console.log("   .",i,j);
                if(arr[i][j] == element) return false;
            }
        }
        return true;
    }
    function sortAndRemove(Arr) {
        for(let i=0;i<Arr.length;i++){
            if(Arr[i].no == Arr.length){
                Arr.splice(i,1);
                i=0;
                continue;
            }
            let temp = i;
            for(let j =i;j<Arr.length;j++){
                //console.log(i,j);
                if(Arr[temp].no < Arr[j].no){
                    temp = j;
                }
            }
            let tem = Arr[temp];
            Arr[temp] = Arr[i];
            Arr[i] = tem;
        }
        return Arr;
    }
    let avail = [];
    let i,j,k;
    for(i=0;i<arr.length;i++){
        avail.push({id:i+1,no:0});
    }
    //filling avail.no for all avail.
    for(i =0;i<arr.length;i++){
        for(j =0;j<arr.length;j++){
            if(arr[i][j] != -1){
                for(k=0;k<avail.length;k++){
                    if(avail[k].id == arr[i][j]){
                        avail[k].no++;
                        break;
                    }
                }
            }
        }
    }
    avail = sortAndRemove(avail)
    console.log(avail);
    console.log(arr);

    for(i =0;i<arr.length;i++){
        for(j =0;j<arr.length;j++){
            if(arr[i][j] == -1){
                for(k=0;k<avail.length;k++){
                    let num = avail[k].id;
                    if(checkColumn(j,num)&&checkRow(i,num)&&grid(i,j,num)){
                        arr[i][j] = num;
                        avail[k].no++;
                        avail = sortAndRemove(avail);
                    }
                }
                if(arr[i][j] == -1){
                    console.log(`error ${i} ${j}`);
                }
            }
            ///console.log(i,j,arr[i]);
        } 
    }
    console.log("\n");
   arr.forEach((e)=>{
       console.log(e);
   })
   console.log(avail);
}
let arr = [[8, 1, 9, -1, -1, 5, -1, -1, -1],[-1, -1, 2, -1, -1, -1, 7, 5, -1],[-1, 3, 7, 1, -1, 4, -1, 6, -1],[4, -1, -1, 5, 9, -1, 1, -1, -1],[7, -1, -1, 3, -1, 8, -1, -1, 2],[-1, -1, 3, -1, 6, 2, -1, -1, 7],[-1, 5, -1, 7, -1, 9, 2, 1, -1],[-1, 6, 4, -1, -1, -1, 9, -1, -1],[-1, -1, -1, 2, -1, -1, 4, 3, 8]]
solveSudoku(arr,3,3)