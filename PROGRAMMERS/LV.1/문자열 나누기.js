function solution(s) {
    var index = 0;
    var count = 0;
    var answer = [];
    
    for(i = 0; i < s.length; i++){
        if(s[i] === s[index]) count++;
        else count--;  
        if(count === 0) {
            answer.push(s.substring(index,i+1))
            index = i+1;
        }
    }
    return answer.join('').length === s.length ? answer.length : answer.length+1;
}