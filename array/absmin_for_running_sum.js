function absMinForRunningSum(arr){
    let absmin = Infinity;
    let runningsum = 0;
    for(let i = 0; i < arr.length; i++){
        runningsum += arr[i];
        absmin = Math.min(absmin, runningsum);
    }
    return 1-absmin;

}