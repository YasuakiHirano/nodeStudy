/**
 * charcterを動かすサンプル
 */
window.onload=function(){
    // 初期化する
    enchant();

    // gameオブジェクトの作成
    var game = new Core(320, 320);
    game.fps = 20;
    game.preload('../images/chara5.png');

    game.onload = function(){
        // sprite作成
        var charcter = new Sprite(32, 32);

        charcter.image = game.assets['../images/chara5.png'];
        charcter.x = 0;
        charcter.y = 0;
        charcter.frame = [0,0,1,1,2,2];

        // フレーム毎に呼ばれるメソッドにキー判定を追加
        charcter.on('enterframe',function(){
            if (game.input.up) {
                charcter.y -= 1;
            }
            if (game.input.down) {
                charcter.y += 1;
            }
            if (game.input.right) {
                charcter.x += 1;
            }
            if (game.input.left) {
                charcter.x -= 1;
            }
        });
        game.rootScene.addChild(charcter);
    };

    game.start();
};
