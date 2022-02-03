/*
Design a cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.

cid is a 2D array listing available currency.

The checkCashRegister() function should always return an object with a status key and a change key.

Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if you cannot return the exact change.

Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it is equal to the change due.

Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order, as the value of the change key.

Currency Unit	Amount
Penny	$0.01 (PENNY)
Nickel	$0.05 (NICKEL)
Dime	$0.1 (DIME)
Quarter	$0.25 (QUARTER)
Dollar	$1 (ONE)
Five Dollars	$5 (FIVE)
Ten Dollars	$10 (TEN)
Twenty Dollars	$20 (TWENTY)
One-hundred Dollars	$100 (ONE HUNDRED)
*/



function checkCashRegister(Price, Cash, cid) {
    let cd = cid;
    let price = Price;
    let cash = Cash;
    for(let i =0;i<cd.length;i++){
        switch(i){
            case 0:
                cd[i].push(0.01)
            break;
            case 1:
                cd[i].push(0.05)
            break;
            case 2:
                cd[i].push(0.1)
            break;
            case 3:
                cd[i].push(0.25)
            break;
            case 4:
                cd[i].push(1)
            break;
            case 5:
                cd[i].push(5)
            break;
            case 6:
                cd[i].push(10)
            break;
            case 7:
                cd[i].push(20)
            break;
            case 8:
                cd[i].push(100);
            break;
        }
    }
    let change = [];

    for(let i=cd.length-1;i>=0;i--){
        let paticularchange = 0;
        while(cash-cd[i][2] >= price && cd[i][1] > 0){
            cash = (cash-cd[i][2]).toFixed(2);
            paticularchange = parseFloat((paticularchange+cd[i][2]).toFixed(2));
            cd[i][1] = (cd[i][1]-cd[i][2]).toFixed(2);
        }
        if(paticularchange != 0 || cd[i][1] == 0)change.push([cd[i][0],paticularchange])
        //console.log(cash,price,paticularchange,cd[i][1],cd[i][2]);
    }
    change = change.reverse()
    let status = "";
    if(price != cash) {
        status = "INSUFFICIENT_FUNDS";
        change = [];
    }else{
        for(let i =0;i<cd.length;i++){
            if(cd[i][1] != 0) status = "OPEN" 
        }
        if(status.length == 0) status = "CLOSED"

    }
    //sorting change
    for(let i =0;i<change.length;i++){
        let max = i;
        for(let j =i;j<change.length;j++){
            if(change[max][1] < change[j][1]){
                max = j;
            }
        }
        let temp = change[max];
        change[max] = change[i];
        change[i] = temp;
    }
    
    return {status:status,change:change};
}

console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]))