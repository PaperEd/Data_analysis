# 알고리즘

### 정의
문제를 해결하기 위한 방법 또는 절차

### 알고리즘의 조건
1. 명확성
2. 수행 가능성
3. 유한성
4. 0개 이상의 입력
5. 1개 이상의 출력
x`

### 시간 복잡도
1. 이중 포문: n^2 => O(n^2)
2. 단일 포문: n => O(n)
2. 분할 정복: log(n) => O(log(n))
2. 단일 계산: 1 => O(1)
```C
for(int i =0; i < n; i++){
    for(int j = 0; j < n; j++){
        sum+= i;
        // for문이 2번 돌면 n^2다
    }
}
```
- `sum = n * (n + 1) /2` 같은 방법으로 대체할 수 있다
- 이런거 하려고 수학 배운다

## 하노이

### 조건
1. 큰 원판 위에 작은 원판만 올 수 있다.
2. 한 번에 하나의 원판만 이동할 수 있다.

 |원판 개수| 이동 횟수 |
 |:-----: | :-------: |
 |   1    |     1     |
 |   2    |     3     |
 |   3    |     7     |
- 2^n - 1 = 하노이탑의 원판의 이동 횟수

### 코드
```C
#include<stdio.h>

int hanoi(int x) {
	if (x == 1) return 1;

	return hanoi(x - 1) + 1 + hanoi(x - 1);
}

int main() {
	int n;
	scanf("%d", &n);
	printf("%d", hanoi(n));
	return 0;
}
```

### 탑 이동 알고리즘
```c
#include<stdio.h>

void hanoi(int x, char sc, char mc, char dc) {
	if (x == 0) return; // 없으면 유한성에 위배됨
	hanoi(x - 1, sc, dc, mc);
	printf("%d : %c -> %c\n", x, sc, dc);
	hanoi(x - 1, mc, sc, dc); 
}

int main() {
	int n;
	scanf("%d", &n);
	hanoi(n, 'A', 'B', 'C');
	return 0;
}
```

### DPS
|   | A | B | C | D | E | F |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | 0 | 1 | 0 | 0 | 1 | 1 |
| B | 1 | 0 | 1 | 1 | 0 | 0 |
| C | 0 | 1 | 0 | 1 | 0 | 0 |
| D | 0 | 1 | 1 | 0 | 0 | 0 |
| E | 1 | 0 | 0 | 0 | 0 | 1 |
| F | 1 | 0 | 0 | 0 | 1 | 0 |

1. 노드 방문
2. 방문하지 않은 인접노트 탐색
3. 방문하지 않은 노드로 이등
4. 모두 방문했으면 백트래킹

- 노드 - 백트래킹 횟수 - 마지막 노드( 1 )

## 시험

### 알고리즘
- 정의
- 조건
- hanoi
- 시간 복잡도

### 그래프
- kruskal
- prim
- sollin
- DFS
- BFS

### 트리
- 레드 블랙 트리