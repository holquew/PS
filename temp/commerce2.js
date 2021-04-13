function solution(gift_cards, wants) {
    let answer = 0;
    let len = gift_cards.length;
    let have = gift_cards.slice();
    let finished = Array(len).fill(false);
    
    for (let i = 0; i < len; i++) {
        if (have[i] === wants[i]) finished[i] = true;
        
        for (let j = 0; j < len; j++) {
            if (have[i] === wants[j] && !finished[j]) {
                [have[i], have[j]] = [have[j], have[i]]
            }
        }
    }
    console.log(have, wants);
    answer = have.concat(wants).filter(x => !have.includes(x) || !wants.includes(x));
    
    return answer;
}
console.log(
    solution(
        [5, 4, 5, 4, 5], [1, 2, 3, 5, 4]
    )
)