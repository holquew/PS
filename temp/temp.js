function check(arr, leaveCount) {
    let jump = 0; 
    let leng = arr.length; 
    for (let i = 1; i < leng; i++) {
        jump += arr[i] - arr[i-1] - 1; 
    }
    if (jump === leaveCount) {
        return arr[leng-1] - arr[0] + 1; 
    }
}

console.log(check([1, 2, 6, 7, 8], 3));