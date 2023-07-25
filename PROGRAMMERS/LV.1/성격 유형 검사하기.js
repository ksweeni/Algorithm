function score(dic){
    let answer = '';
    dic['R'] >= dic['T'] ? answer+='R' : answer+='T'
    dic['C'] >= dic['F'] ? answer+='C' : answer+='F'
    dic['J'] >= dic['M'] ? answer+='J' : answer+='M'
    dic['A'] >= dic['N'] ? answer+='A' : answer+='N'
    return answer;
}

function solution(survey, choices) {
    var dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0};
    for(let i =0; i < choices.length; i++){
        if(choices[i]>4) dic[survey[i][1]] += choices[i]-4;
        else if(choices[i]<4) dic[survey[i][0]]+=Math.abs(choices[i]-4);
    }
    
    return score(dic);
}