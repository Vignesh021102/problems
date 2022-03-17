
class AVL{
    constructor(){
        this.root = null;
        this.NODE = class {
            constructor(num,ht){
                this.id = num;
                this.ht = ht;
                this.L = null;
                this.R = null;
                
            }
        }
    }
    #add(t,val){
        
        if(!t){
            return new this.NODE(val,0);
        }else if(val > t.id){
            //right
            t.R = this.#add(t.R,val);
            if(this.#BF(t) == -2){
                t = val > t.R.id ?this.#RR(t):this.#RL(t);
            }
            this.#ht(t.R);
        }else if(val < t.id ){
            //left
            t.L = this.#add(t.L,val);
            if(this.#BF(t) == 2){
                t = val < t.L.id ?this.#LL(t):this.#LR(t);
            }
            this.#ht(t.L);
        }
        this.#ht(t);
        return t;
    }
    #ht(t){
        let l = t.L != null?t.L.ht+1:0;
        let r = t.R != null?t.R.ht+1:0;
        t.ht = l>r?l:r;
    }
    #rotateLeft(t){
        let right = t.R;
        t.R = right.L;
        right.L = t;
        this.#ht(t);
        this.#ht(right);
        return right;
    }
    #rotateRight(t){
        let temp = t.L;
        t.L = temp.R;
        temp.R = t;
        this.#ht(t);
        this.#ht(temp);
        return temp;
    }
    #LL(t){
        return this.#rotateRight(t)
    }
    #RR(t){
        return this.#rotateLeft(t);
    }
    #LR(t){
        t.L = this.#rotateLeft(t.L);
        return this.#rotateRight(t);
    };
    #RL(t){
        t.R = this.#rotateRight(t.R);
        return this.#rotateLeft(t);
    }
    #BF(t){
        let l = t.L?t.L.ht+1:0;
        let r = t.R?t.R.ht+1:0;
        return l-r;
    }
    #preOrder(t){
        if(!t) return;
        console.log(t.id);
        if(t.L)this.#preOrder(t.L);
        if(t.R)this.#preOrder(t.R)
    }
    insert(val){
        this.root = this.#add(this.root,val);
    }
    display(){
        console.log(this.root);
        //this.#preOrder(this.root)
    }
}

var avl = new AVL();
for(let i=0;i<100;i++){
    avl.insert(i);
}
avl.display();