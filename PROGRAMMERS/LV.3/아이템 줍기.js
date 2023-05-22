function solution(rectangle, characterX, characterY, itemX, itemY) {
	const dx = [1, -1, 0, 0];
	const dy = [0, 0, 1, -1];
	const maxSize = 101;
	const visited = Array.from({ length: maxSize }, () => Array(maxSize).fill(0));

	const newRect = rectangle.map((el) => el.map((v) => v * 2));

	newRect.forEach(([x1, y1, x2, y2]) => {
		for (let i = y1; i <= y2; i++) {
			for (let j = x1; j <= x2; j++) {
				// 테두리 일경우
				if (j === x1 || j === x2 || i === y1 || i === y2) {
					// 이미 테두리 인경우 === 테두리가 교차됬을 경우는 값 유지
					if (visited[j][i] === 1) continue;
					// 그러나, 현재 값이 테두리 이지만 저장된 값이 테두리가 아닐경우 +1
					// (0일때는 1이 되고 1 이상일 때는 테두리가 아니므로 값이 저장되어 지나갈 수 없다.)
					else visited[j][i] += 1;
				} else visited[j][i] += 2;
			}
		}
	});
    
  characterX *= 2;
	characterY *= 2;
	itemX *= 2;
	itemY *= 2;

	// 최단 거리이므로 bfs 실행
	const q = [[characterX, characterY, 0]];
	visited[characterX][characterY] += 100;

	while (q.length) {
		const [nowX, nowY, step] = q.shift();

		// 목표 지점에 도착했을 경우 (결과값 / 2) 를 반환
		if (nowX === itemX && nowY === itemY) return step / 2;

		for (let i = 0; i < 4; i++) {
			const [curX, curY] = [nowX + dx[i], nowY + dy[i]];

			if ( curX>= 0 && curX < 101 && curY >= 0 && curY < 101)
				if (visited[curX][curY] === 1) {
					visited[curX][curY] += 100;
					q.push([curX, curY, step + 1]);
				}
		}
	}
}