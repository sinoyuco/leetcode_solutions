var sortArray = function (nums) {
    if (nums.length < 2) { return nums; }
    let pivot = nums.pop();
    let left = [];
    let right = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > pivot) {
            right.push(nums[i])
        } else {
            left.push(nums[i])
        }
    }

    return sortArray(left).concat([pivot], sortArray(right))
};