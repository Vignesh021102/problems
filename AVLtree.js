
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
    #remove(t,val){
        if(!t){
            console.log(`${val} not found`);
            return t;
        }
        if(t.id == val){
            if(!(t.L&&t.R))return null;
            if(!t.R){
                t = t.L;
                t = this.#remove(t.L,t.L.id)
            }
            this.#ht(t);
            t = this.#min(t.R);
            t = this.#remove(t.R,t.id);
            return t;
        }else if(val > t.id){
            t.R = this.#remove(t.R,val);
            this.#ht(t);
            
            if(this.#BF(t) >= 2){
                console.log("bf\n");
                t = this.#BF(t.L) >= 0 ?this.#LL(t):this.#LR(t);
            }
        }else{
            t.L = this.#remove(t.L,val);
            this.#ht(t);
            
            if(this.#BF(t) <= -2){
                t = this.#BF(t.R) <= 0?this.#RR(t):this.#RL(t)
            }
        }
        //console.log(t.id,this.#BF(t));
        return t;
    }
    delete(val){
        this.root = this.#remove(this.root,val);
        
    }
    #min(temp){
        if(!temp) return null;
        while(temp.L != null){
            temp = temp.L;
        }
        return temp;
    }
    #max(temp){
        if(!temp) return null;
        while(temp.R != null){
            temp = temp.R;
        }
        return temp;
    }
    get(id){
       return this.#search(this.root,id)
    }
    #search(t,val){
        if(t ==  null) return null;
        if(t.id == val) return t;
        if(val > t.id){
           return this.#search(t.R,val);
        }else{
            return this.#search(t.L,val);
        }
    }
}
