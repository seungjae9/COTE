# 자료구조

### Stack(스택)

##### 정의
	Last in Firtst out(후입선출) 자료구조
	인터넷 페이지라고 생각하면 쉽다.(뒤로가기 버튼 누르면 가장 최근에 봤던 페이지로 이동)



##### 사용방법

![ex_screenshot](/img/stack.JPG)



	1. push, append(삽입): 리스트 마지막에 데이터 넣기 
						  마지막 위치 기억 변수 Top
	2. pop(삭제): 마지막 데이터 삭제 
	3. peek: 가장 마지막 데이터 읽기
	4. is_empty: 스택이 비어있는지 확인








### Queue(큐)

##### 정의
	First in First out(선입선출) 자료구조
	Enqueue(입력), Dequeue(출력) ==> Stack에서의 Push, Pop
	은행에서 번호표라고 생각하면 쉽다.

##### 사용방법

![ex_screenshot](/img/Queue.png)


	1. Enqueue: 큐 맨 뒤에 데이터 추가, 
	2. Dequeue: 큐 맨 앞에 데이터 삭제
	3. Peak: front에 위치한 데이터 읽기(은행에서 다음 손님이 누구인지 확인)
	4. front: 큐 맨 앞의 위치(index) 번호
	5. rear: 큐 맨 뒤의 위치(index) 번호







### Dequeue(디큐)
			from collections import deque
			q = dequeue()    # 비어있는 큐
	        q = dequeue([1, 2, 3])   # 큐에 값있을 때





### Brute-force(완전탐색)

##### 정의
	가능한 방법을 모든 경우의 수를 다 해본다.

##### 완전탐색 방법
	1. Brute-Force: for문, if문을 이용해 처음부터 끝까지 탐색
	2. 비트마스크(비트연산): 이진법 활용
	3. 순열
	4. 백트래킹
	5. BFS, DFS



##### 조합

		python itertools 내장함수 사용
		itertools.combinations("원하는거", 몇개원하는지)
	
		ex)
		import itertools
		
		A = [1,2,3]
		B = itertools.combinations(A, 3)
		print(list(B))
				====>[(1, 2), (1, 3), (2, 3)]
				
		A = itertools.combinations('ABC', 2)
		print(list(A))
				===>[('A', 'B'), ('A', 'C'), ('B', 'C')]
