class Grid{
    constructor(width,height,res){
      this.width = Math.floor(width);
      this.height = Math.floor(height);
      this.row = Math.floor(height/res);
      this.col = Math.floor(width/res);
      this.res = res
      this.arr = [];
      this.cell = class {
        constructor(i,j,res,val){
          this.f=-1;
          this.g=0;
          this.h=0;
          this.res = res;
          this.i = i;
          this.j = j;
          this.neighbour = [];
          this.pre = undefined;
          this.val = val;
        }
        show(color){
          if(this.val == 1){
            fill(255)
          }else{
            fill(color)
          }
          
          stroke(10)
          rect(this.j*this.res,this.i*this.res,this.res,this.res)
        }
        addNeighbour(arr){
          this.neighbour = [];
          for(let i =-1;i<2;i++){
            for(let j =-1;j<2;j++){
      
              if(i ==0 &&j==0) continue;
              if(this.i ==0 &&i == -1) continue;
              if(this.j ==0 &&j==-1) continue;
              if(this.i ==arr.length-1 &&i==1) continue;
              if(this.j==arr[0].length-1 &&j==1) continue;
      
              this.neighbour.push(arr[this.i+i][this.j+j])
            }
          }
          
        }
      }
    }
    initArr(){
      for(let i = 0;i<this.row;i++){
        this.arr.push([])
        for(let j =0;j<this.col;j++){
          this.arr[i].push(new this.cell(i,j,this.res,Math.random()<0.3?1:0))
        }
      }
      this.row = this.arr.length;
      this.col = this.arr[0].length
      console.log(this.row,this.col);
    } 
    #removeFromArray(list,pos){
      for(let i=0;i<list.length;i++){
        if(list[i].i==pos.i&&list[i].j==pos.j){
          list.splice(i,1);
          return;
        }
      }
    }
    findPath(pos1,pos2){
      let current,openSet = [],closedSet = [];
      pos1.val = 0;
      pos2.val =0;
      openSet.push(pos1);
      var newPath;
      for(let i=0;i<this.arr.length;i++){
        for(let j =0;j<this.arr[i].length;j++){
          this.arr[i][j].addNeighbour(this.arr)
        }
      }
      while(openSet.length >=1){
        var low = 0;
        for(let i=0;i<openSet.length;i++){
          if(openSet[i].f == -1)continue;
          if(openSet[i].f < openSet[low].f) low = i;
        }
        current = openSet[low];
        if(current === pos2) {
          console.log("DONE");
          //DONE
            var path = [];
            var temp = current;
            path.push(temp)
            while(temp.pre){
            temp.show(color(0,0,255));
            path.push(temp.pre);
            temp = temp.pre;
            }
            temp.show(color(0,0,255))
            noLoop()
            return path;
        };
        this.#removeFromArray(openSet,current)
        closedSet.push(current);
    
        let nei,tempG;
        for(let i=0;i<current.neighbour.length;i++){
          nei = current.neighbour[i];
          newPath = false;
          if(!closedSet.includes(nei)&&nei.val == 0){
            tempG = current.g+1;
            if(openSet.includes(nei)){
              if(tempG<nei.g){
                nei.g = tempG;
                newPath = true;
              };
            }else{
              newPath = true;
              nei.g = tempG;
              openSet.push(nei)
            }
            if(newPath){
              nei.h = dist(nei.j,nei.i,pos2.j,pos2.i);
              nei.f = nei.g+nei.h;
              nei.pre = current;
            }
            
          }
        }
      }
        console.log("no solution");
        return undefined;
    }
  }