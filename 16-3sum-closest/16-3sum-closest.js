/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort((a,b) => a-b)
    let closest = (nums[0]+nums[1]+nums[2])
    let difference = Math.abs(closest - target);
    console.log(nums)
    for (let i = 0; i < nums.length; i++) {
        let min = i + 1 ;
        let high = nums.length - 1;
        while(min<high){
        let total = nums[i] + nums[min] + nums[high]
        if (Math.abs(total-target) < difference) {
            closest = total
            difference = Math.abs(total-target)
        }
        if (total > target) high--
        else min ++
    }}
    return closest
};