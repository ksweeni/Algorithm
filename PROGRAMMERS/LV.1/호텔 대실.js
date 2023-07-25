function nextTime(end) {
    const next = end.split(":");
    return Number(next[0]) * 60 + Number(next[1]) + 10;
  }
  
  function solution(book_time) {
    book_time.sort();
    let room = [];
      
    book_time.forEach((v) => {
      let tmp = v[0].split(":");
      let start = Number(tmp[0]) * 60 + Number(tmp[1]);
      let idx = room.findIndex((e) => e <= start);
      if (idx === -1) room.push(nextTime(v[1]));
      else room[idx] = nextTime(v[1]);
    });
  
    return room.length;
  }