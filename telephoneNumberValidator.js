 /*
 Return true if the passed string looks like a valid US phone number.

The user may fill out the form field any way they choose as long as it has the format of a valid US number. The following are examples of valid formats for US numbers (refer to the tests below for other variants):

555-555-5555
(555)555-5555
(555) 555-5555
555 555 5555
5555555555
1 555 555 5555
For this challenge you will be presented with a string such as 800-692-7753 or 8oo-six427676;laskdjf. Your job is to validate or reject the US phone number based on any combination of the formats provided above. The area code is required. If the country code is provided, you must confirm that the country code is 1. Return true if the string is a valid US phone number; otherwise return false
*/
 
function telephoneCheck(str){
    let reg1 = /[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]/;
    let reg2 = /[(][0-9][0-9][0-9][)] [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]/;
    let reg3 = /[(][0-9][0-9][0-9][)][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]/;
    let reg4 = /[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9][0-9]/;
    let reg5 = /[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]/;
    // console.log(reg1.test(str),"reg1");
    // console.log(reg2.test(str),"reg2");
    // console.log(reg3.test(str),"reg3");
    // console.log(reg4.test(str),"reg4");
    // console.log(reg5.test(str),"reg5");
    if(reg1.test(str))str = str.replace(reg1,"");
    if(reg2.test(str))str = str.replace(reg2,"");
    if(reg3.test(str))str = str.replace(reg3,"");
    if(reg4.test(str))str = str.replace(reg4,"");
    if(reg5.test(str))str = str.replace(reg5,"");
    str = str.trim();
    if(str.length == 0 || (str.length == 1 &&str[0] == "1")) return true;
    return false;
}
console.log(telephoneCheck("1 555 555 5555"));
  console.log(telephoneCheck("555-555-5555"))
  console.log(telephoneCheck("-1 (757) 622-7382"));