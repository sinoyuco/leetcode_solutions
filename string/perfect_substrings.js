function perfectSubstring(s, k) {
    // Write your code here
    let count = 0;
    for(let i =0; i < s.length; i++){
        for(let j =i+1; j < s.length; j++){
            let sliced = s.slice(i,j+1);
            let hsh = {}

            for(let j = 0; j < sliced.length; j++){
                let el = sliced[j];
                hsh[el] ? hsh[el] += 1 : hsh[el] = 1;
            }
                
            

            if(Object.values(hsh).every(c => c === k)){count+=1;}
        }
    }
    return count
}