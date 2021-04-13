const combinations = (arr, select) => {
    const results = [];
    if (select === 1) return arr.map(value => [value]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1); 
        const combs = combinations(rest, select - 1); 
        const attached = combs.map((combination) => [fixed, ...combination]);
        results.push(...attached); 
      });

    return results;
}

function solution(needs, r) {
    let answer = -987654321;
    let partsLen = needs[0].length;
    let parts = []; 
    for (let i = 0; i < partsLen; i++) {
        parts.push(i);
    }

    let partsCombs = combinations(parts, r);
    for (let i = 0; i < partsCombs.length; i++) {
        let temp = 0;
        let comb = partsCombs[i];
        needs.forEach(need => {
            for (let i = 0; i < need.length; i++) {
                if (need[i] === 1) {
                    if (!comb.includes(i)) {
                        return;
                    }
                }
            }
            temp++;
        })
        if (answer < temp) {
            answer = temp;
        }
    }

    return answer;
}

console.log(
    solution(
        [ [ 1, 0, 0, 1 ], [1, 1, 0, 0], [1, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0] ],
        3
    )
)