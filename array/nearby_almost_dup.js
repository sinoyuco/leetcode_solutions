var containsNearbyAlmostDuplicate = function (nums, k, t) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (Math.abs(nums[j] - nums[i]) <= t && Math.abs(j - i) <= k) {
                console.log(`${i} and ${j}`);
                return true;
            }
        }
    }
    return false;
};

export default containsNearbyAlmostDuplicate;