

function solution(n, passenger, train) {
    let answer = [];
    let dp = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        dp[i] = passenger[i];
    }
    let graph = {};
    for (let i = 0; i < train.length; i++) {
        [a, b] = train[i];
        if (graph[a]) {
            graph[a].push(b);
        } else {
            graph[a] = [b];
        }

        if (graph[b]) {
            graph[b].push(a);
        } else {
            graph[b] = [a];
        }
    }
    let visited = new Array(n).fill(false);
    const dfs = (start, visited) => {
        visited[start] = true;
        graph[start].forEach(node => {
            if (!visited[node]) {
                dp[start] += dfs(node, visited);
            }
        })
        
        return dp[start];
    }
    
    dfs('1', visited);
    console.log(dp);


    return answer;
}


console.log(
    solution(
        6,
       [1,1,1,1,1,1], 
       [[1,2],[1,3],[1,4],[3,5],[3,6]]
    )
)