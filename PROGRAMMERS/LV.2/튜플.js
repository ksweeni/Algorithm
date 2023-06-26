function solution(s) {
    var answer = []
    const sub = s.substring(1, s.length-2).split('},')
    	.map(str=>str.substring(1).split(',')
        .map(v=>Number(v)));
 
    sub.sort((a, b) => a.length - b.length);
 
    sub.forEach((v)=>{
        v.forEach((val)=>{
            if(!answer.includes(val)){
                //console.log(val)
                answer.push(val)
            }
        })
    })

    return answer;
    
  
}