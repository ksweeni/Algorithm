function isPrime(number) {
    if (number <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
        return false;
      }
    }
    return true;
  }
  
  function solution(n, k) {
      var answer = 0;
      const arr = n.toString(k).split('0');
      for(let i=0;i<arr.length;i++){
          if(isPrime(arr[i])){
              answer++;
          }
      }
      return answer;
  }