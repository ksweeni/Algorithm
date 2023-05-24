function solution(files) {
    const pattern = /(\D+)(\d{1,5})/;
    //\D+ (숫자가 아닌것을 1개 이상 찾는다.)
    //\d{1,5} (숫자인 것을 1개 이상 5개 이하로 찾는다.)
    return files.sort((a,b)=>{
        let [HA, numa] = a.match(pattern).slice(1, 3);
        let [HB, numb] = b.match(pattern).slice(1, 3);
        HA = HA.toLowerCase();
        HB = HB.toLowerCase();
        if (HA === HB && numa === numb) return 0;
		    if (HA === HB) return numa - numb;
		    if (HA > HB) return 1;
			   else return -1;
    })
 
}