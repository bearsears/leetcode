/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    //console.log(arr, n);
    if (n === 0)
        return arr;
    ans = [];
    start = 0;
    lvl = 0;
    while (n > 0) {
        let passed = true;

        for (let i = 0; i < arr.length; i += 1) {
            if (typeof arr[i] === "number") {
                ans.push(arr[i]);
            } else {
                passed = false;
                ans.push(...arr[i]);
            }
        }
        n -= 1;
        arr = [...ans];
        ans = []
        //console.log(arr, ans, passed)
        if (passed) 
            break;
    }

    return arr;
};