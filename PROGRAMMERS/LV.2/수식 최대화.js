function solution(expression) {
    const combination = [
        ['-', '*', '+'],
        ['-', '+', '*'],
        ['*', '-', '+'],
        ['*', '+', '-'],
        ['+', '-', '*'],
        ['+', '*', '-']
    ];
    let answer = [];

    for (let comb of combination) {
        const temp = expression.split(/(\D)/);
        for (let op of comb) {
            while (temp.includes(op)) {
                const idx = temp.indexOf(op)
                temp.splice(idx - 1, 3, eval(temp.slice(idx - 1, idx + 2).join('')));
            }
        }
        answer.push(Math.abs(temp[0]));
    }
    
    return Math.max(...answer);
}