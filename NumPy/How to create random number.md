## 난수 생성
- `numpy.random`은 내장 함수 `random`을 보강하여 난수를 생성한다.
- 다양한 종류의 확률분포로부터 표본 값을 생성할 수 있다

### np.random.seed( )
- 난수의 시드를 지정한다

### np.random.rand( )
- 균등분포에서 표본을 추출한다
- 균등분포: 값이 균등하게 분포되어있는 경우

### np.random.randint( )
- 주어진 범위에서 임의의 난수를 추출한다

### np.random.randn( )
- 표준편차가 1이고 평균이 0인 정규분포에서 표본을 추출한다

### np.random.binomial(n, p, size)
- `n` : 사건이 일어나는 횟수
  - `float`도 인식하긴 하지만 `integer`로 변환된다
- `p` : 사건이 일어날 확률
  - 당연한 거지만 1 이하의 숫자만 인자로 받는다

### np.random.normal( )
- 가우시안 정규분포에서 표본을 추출한다

### np.random.shuffle( )
- 리스트나 배열의 순서를 섞는다
- 반환값이 없다. 인자로 넣은 배열의 순서가 바뀐다

### np.random.permutation( )
- 순서를 섞은 순열을 **반환**한다

### np.random.beta( )
- 베타분포에서 표본을 추출한다
- 베타분포는 다운링크 빔포밍에서 쓰인다고 한다

### np.random.chisquare( )
- 카이제곱분포에서 표본을 추출한다

### np.random.gamma( )
- 감마분포에서 표본을 추출한다

### np.random.uniform( )
- 균등(0,1)분포에서 표본을 추출한다