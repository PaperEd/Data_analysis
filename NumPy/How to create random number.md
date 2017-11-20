## 난수 생성
- `numpy.random`은 내장 함수 `random`을 보강하여 난수를 생성한다.
- 다양한 종류의 확률분포로부터 표본 값을 생성할 수 있다

### np.random.rand( )
- 균등분포에서 표본을 추출한다
- 균등분포: 값이 균등하게 분포되어있는 경우

### np.random.randint( )
- 주어진 범위에서 임의의 난수를 추출한다

### np.random.randn( )
- 표준편차가 1이고 평균이 0인 정규분포에서 표본을 추출한다

### np.random.binomial(n, p, size)
- `n` : 사건이 일어나는 횟수
- `p` : 사건이 일어날 확률
### np.random.rand( ), np.random.randn( ), np.random.randint( )
- `rand`는 uniform 분포를 따르는 0에서 1 사이의 난수를 생성한다.
- `randn`은 가우시안 정규 분포를 따르는 난수를 생성한다.
- `randint`의 첫번째 인자는 `low`, 두번째 인자는 `high`이다. `size=`을 이용해 배열의 크기를 지정 할 수 있다.
  - `high`는 난수 생성 범위에 포함되지 않는다.
- `random.seed`를 사용해 시드값을 지정할 수 있다.