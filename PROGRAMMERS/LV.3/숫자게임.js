function solution (A, B) {
    let answer = 0;
    A.sort((a,b) => b-a);
    B.sort((a,b) => a-b);
    for(const num of A) {
      const max = B[B.length - 1];
      if(max > num) {
        answer++;
        B.pop();
      }
    }
    return answer;
  }