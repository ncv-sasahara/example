const module1 = require('./module1'),
      module2 = require('./module2'),
      module3 = require('./module3');

// --- プログラム部分 ---

// main関数
const main = () => {

  // keyに引数を代入する。引数がない場合は終了
  const key = process.argv[2];

  if(!key){
    console.log('引数がないです');
    return;
  }

  // app[key].startを実行 keyがない場合（m1, m2, m3以外の場合）は終了
  switch(key) {
    case 'm1':
      module1.start();
      break;
    
    case 'm2':
      module2.start();
      break;
    
    case 'm3':
      module3.start();
      break;
    
    default:
      console.log('moduleがないです');
      break;
  }

};

// main関数を実行
main();
