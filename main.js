// const nemo = ["nemo",];

// const everyone = ["dary", "bruce", "marlin" ,  "gill", "bloat", "nigel", "squirt", "darla" , "hank", "nemo"];
 
// const large = new Array(10).fill("nemo");

// function findNemo(array) {
//     let t0 = performance.now();
    
//     for (let i=0; i<array.length; i++) {
//         console.log("running")
//         if(array[i] === "nemo") {
//             console.log("found Nemo");
//             break;
//         }
//     }
//     let t1 = performance.now();
//     console.log("call to find nemo took " +(t1-t0) + " milliseconds")
// }

// findNemo(everyone); //O(n) -> linear time 

// const boxes = [1,2,3,4,5];   

// function logAllPairsOfArray( array) {
//     for (let i=0; i< array.length; i++ ) {
//         for(let j=0; j<array.length; j++) {
//             console.log(array[i], array[j]);
//         }
        
//     }
// }
// logAllPairsOfArray(boxes);

// const array1 = ['a', 'b', 'c', 'd'];
// const array2 = ['a', 'f', 'a', 'd'];

// console.log("olalekanBankole".length);

// function containsCommonItem(arr1, arr2) {
//     for (let i=0; i < arr1.length; i++) {
//         for(let j=0; j< arr2.length; j++)  {
//             // console.log(arr1[i], arr2[j])
//             if (arr1[i] === arr2[j]) {
//                 console.log("true")
//             } 
//         }
//     }
//     // console.log("false");
// }


//O(a*b)

// containsCommonItem(array1, array2);

// const array1 = ['a', 'e', 'q', 'd'];
// const array2 = ['t', 'v', 'q', 'u'];

//array1 ===> obj {
// a: true,
// b: true,
// c: true,
// x: true
// }

// array2[index] ===object.properties


// function  containsCommonItem2 (arr1, arr2){
// //loop through first  and create object where properties === items in the array
// //loop through second array and check if item in second array exists on created object.

// let map = {}

// for (let i=0; i < arr1.length; i++) {
//     if (!map[arr1[i]]) {
//         const item = arr1[i];
//         map[item] = true;
//     }
// }
// console.log(map)

// for 
// (let j=0; j<arr2.length; j++) {
//     if (map[arr2[j]]) {
//         console.log ("true");
//         // return true;
//     } else if (!map[arr2[j]]) {
//         console.log("false");
//         // return false

//     }
// }
// // console.log("false");
// }

// containsCommonItem2(array1, array2);
// //O (a+b)   

// function containsCommonitem3 (arr1, arr2) { 
//     return arr1.some(item => arr2.includes(item))
//     co
     
// }

// containsCommonitem3(array1, array2);

// string[x?].push .pop .unshift .splice 

// var object1 = {value: 10};
// var object2 = object1;
// var object3 = {value: 10};

// const object4 = {
//     a: function() {
//         console.log(this);
//     }
// }

//instantiation

// class player {
//     constructor(name, type) {
//         console.log("player", this)
//         this.name = name;
//         this.type = type;
//     }
//     introduce() {
//         console.log(`Hi, I am ${this.name}, I'm a ${this.type}`)    
//     }
// }

// class wizard extends player {
//     constructor(name, type) {
//         super(name, type)
//         console.log("wizard", this)
//     }
//     play() {
//         console.log(`WEEEEEEE I'm a ${this.type}`)
//     }
// }

// const wizard1 = new wizard('shelly', 'Healer');
// const wizard2 = new wizard('shawn', 'dark magician');

// class MyArray {
//     constructor () {
//         this.length=0;
//         this.data = {};
//     }

//     get(index) {
//         return this.data[index]
//     }

//     push(item) {
//         this.data[this.length] = item;
//         this.length++;
//         return this.length;
//     }

//     pop() {
//         const lastItem = this.data[this.length-1];
//         delete this.data[this.length-1];
//         this.length--;
//         return lastItem;
//     }

//     delete(index) {
//         const item = this.data[index];
//         this.shiftItems(index);
//     }

//     shiftItems(index) {
//         for (let i= index; i < this.length - 1; i++) {
//             this.data[i] = this.data[i+1];
//         }
//         delete this.data[this.length-1];
//         this.length--;
//     }
// }

// const newArray = new MyArray();
// newArray.push("hi,");
// newArray.push("you");
// newArray.push("are");
// newArray.push("lekan");
// // newArray.pop();
// // newArray.pop();
// // newArray.delete(0);
// console.log(newArray);


class HashTable {
    constructor(size) {
        this.data = new Array(size);
        ['grapes', 100000]
    }

    _hash(key) {
        let hash = 0;
        for (let i=0; i<key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) %
            this.data.length
            // console.log(hash);
        }

        return hash;
    }

    set(key, value) {
        let address  = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
            this.data[address].push([key, value])
            console.log(this.data)
        }
        // this.data[address].push([key, value])
        // return this.data
    }

}

const myHashTable = new HashTable(50);
// console.log(myHashTable._hash("grapes", 10000))
myHashTable.set("grapes", 10000)

myHashTable.set("apple", 10000)