// solveSudoku([[8, 1, 9, -1, -1, 5, -1, -1, -1],[-1, -1, 2, -1, -1, -1, 7, 5, -1],[-1, 3, 7, 1, -1, 4, -1, 6, -1],[4, -1, -1, 5, 9, -1, 1, -1, -1],[7, -1, -1, 3, -1, 8, -1, -1, 2],[-1, -1, 3, -1, 6, 2, -1, -1, 7],[-1, 5, -1, 7, -1, 9, 2, 1, -1],[-1, 6, 4, -1, -1, -1, 9, -1, -1],[-1, -1, -1, 2, -1, -1, 4, 3, 8]]) should return [[8, 1, 9, 6, 7, 5, 3, 2, 4],[6, 4, 2, 9, 8, 3, 7, 5, 1],[5, 3, 7, 1, 2, 4, 8, 6, 9],[4, 2, 6, 5, 9, 7, 1, 8, 3],[7, 9, 5, 3, 1, 8, 6, 4, 2],[1, 8, 3, 4, 6, 2, 5, 9, 7],[3, 5, 8, 7, 4, 9, 2, 1, 6],[2, 6, 4, 8, 3, 1, 9, 7, 5],[9, 7, 1, 2, 5, 6, 4, 3, 8]]

function solveSudoku(arr,gridRow,gridColumn){
    //finding gridsize of it is undefined
    if(gridRow == undefined &&gridColumn == undefined){
        let size = Math.sqrt(arr.length);
        if (Number.isInteger(size)) {
            gridRow = size;
            gridColumn = size;
        }else{
            gridRow = Math.floor(size);
            gridColumn = gridRow+1;
        }
    }else if (gridColumn == undefined){
        gridColumn = gridRow;
    }

    function checkRow(row,col,ele,del){
        let i,j;
        if(del == undefined){
            for(i=0;i<arr.length;i++){
                if(Array.isArray(arr[row][i])&&i== col) continue;
                if(arr[row][i] == ele) return false;
            }
            return true;
        }else if(del == true || del == false){
            for(i =0;i<arr.length;i++){
                if(Array.isArray(arr[row][i])  && i != col){
                    for(j =0;j<arr[row][i].length;j++){
                        if(arr[row][i][j] == ele){
                            if(del == true )arr[row][i].splice(j,1);
                            if(del == false) return false;
                        }
                    }
                    if(arr[row][i].length == 1){
                        arr[row][i] = arr[row][i][0]
                    }
                }
            }
            if(del == false) return true;
        }
    }
    function checkColumn(row,col,ele,del){
        let i,j;
        if(del == undefined){
            for(i=0;i<arr.length;i++){
                if(Array.isArray(arr[i][col])&&i == row) continue;
                if(arr[i][col] == ele) return false;
            }
            return true;
        }else if(del == true || del == false){
            for(i =0;i<arr.length;i++){
                if(Array.isArray(arr[i][col])  && i != row){
                    for(j =0;j<arr[i][col].length;j++){
                        if(arr[i][col][j] == ele){
                            if(del == true) arr[i][col].splice(j,1);
                            if(del == false) return false;
                        }
                    }
                    if(arr[i][col].length == 1){
                        arr[i][col] = arr[i][col][0]
                    }
                }
            }
            if(del == false) return true;
        }
    }
    function grid(row,column,ele,del){
        let Qrow = row,Qcol = column;
        row = Math.floor(row/gridRow);
        column = Math.floor(column/gridColumn);
        //console.log(row,column);
        if(del == undefined){
            for(let i =(row*gridRow);i<(gridRow+(gridRow*row));i++){
                for(let j = (column*gridColumn);j<(gridColumn+(gridColumn*column));j++){
                    //console.log("   .",i,j);
                    if(Array.isArray(arr[i][j]) &&Qrow == i && Qcol == j) continue;
                    if(arr[i][j] == ele) return false;
                }
            }
            return true;
        }else if(del == true || del == false){
            for(let i =(row*gridRow);i<(gridRow+(gridRow*row));i++){
                for(let j = (column*gridColumn);j<(gridColumn+(gridColumn*column));j++){
                    if(Array.isArray(arr[i][j])  && (Qrow != i && Qcol != j)){
                        for(let k =0;k<arr[i][j].length;k++){
                            if(arr[i][j][k] == ele) {
                                if(del == true) arr[i][j].splice(k,1);;
                                if(del == false) return false;
                            }
                        }
                        if(arr[i][j].length == 1){
                            arr[i][j] = arr[i][j][0]
                        }
                    }
                }
            }
            if(del == false) return true;
        }
    }
    let i,j;
    // finding possible answers
    for(i =0;i<arr.length;i++){
        for(j =0;j<arr.length;j++){
            if(arr[i][j] == -1){
                arr[i][j] = [];
                let k =1;
                while(k<=arr.length){
                    if(checkColumn(i,j,k)&&checkRow(i,j,k)&&grid(i,j,k)){
                        arr[i][j].push(k);
                    }
                    k++;
                }
            }
        }
    }
    //console.log(arr);
// using naked single method
    for(i =0;i<arr.length;i++){
        for(j =0;j<arr.length;j++){
            //console.log(arr[i][j],Array.isArray(arr[i][j]) ,arr[i][j].length==1);
            if(Array.isArray(arr[i][j])  &&arr[i][j].length==1){
                checkRow(i,j,arr[i][j][0],true);
                
                checkColumn(i,j,arr[i][j][0],true);
               
                grid(i,j,arr[i][j][0],true);
                
                arr[i][j] = arr[i][j][0];
            }
        }
    }
    //last checking 
    for(i =0;i<arr.length;i++){
        for(j =0;j<arr.length;j++){
                checkRow(i,j,arr[i][j],true);
                checkColumn(i,j,arr[i][j],true);
                grid(i,j,arr[i][j],true);
        }
    }
  return arr;
}
solveSudoku([[4,-1,-1,-1],[-1,-1,2,-1],[-1,3,-1,-1],[-1,-1,-1,1]]); // ans = [[4,2,1,3],[3,1,2,4],[1,3,4,2],[2,4,3,1]];
solveSudoku([[8, 1, 9, -1, -1, 5, -1, -1, -1],[-1, -1, 2, -1, -1, -1, 7, 5, -1],[-1, 3, 7, 1, -1, 4, -1, 6, -1],[4, -1, -1, 5, 9, -1, 1, -1, -1],[7, -1, -1, 3, -1, 8, -1, -1, 2],[-1, -1, 3, -1, 6, 2, -1, -1, 7],[-1, 5, -1, 7, -1, 9, 2, 1, -1],[-1, 6, 4, -1, -1, -1, 9, -1, -1],[-1, -1, -1, 2, -1, -1, 4, 3, 8]])
