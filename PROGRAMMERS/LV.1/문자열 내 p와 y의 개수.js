function solution(s){
    var answer = true;
    let num_p=0, num_y=0;
    for(let i =0;i<s.length;i++){
        if(s[i].toUpperCase() === 'P' || s[i].toLowerCase() === 'p'){
            num_p+=1;
        }
        else if(s[i].toUpperCase() === 'Y' || s[i].toLowerCase() === 'y'){
            num_y+=1;
        }
    }
    if(num_p===num_y || num_p ===0 && num_y===0 ){
        answer = true;
    }
    else{
        answer = false;
    }

    console.log(answer)
    return answer;
}