
const start = () => {

  const randomNumber = Math.floor(Math.random() * 1001);

  console.log(`ランダムな数値を出力します。
    ランダムな数値: ${randomNumber}`);

};

module.exports = {
  start: start
};
