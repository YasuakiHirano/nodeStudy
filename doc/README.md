#Markdown記法のテスト  
markdown記法のreadmeを書くテスト  
参考にさせていただきました。  
=> http://codechord.com/2012/01/readme-markdown/  
=> http://qiita.com/Qiita/items/c686397e4a0f4f11683d#%E7%B5%B5%E6%96%87%E5%AD%97
  
##改行  
改行は行末に2つのスペースをいれる。  
```
改行[space][space]
Test
```  
↓
改行  
Test


##強調  
強調はアスタリスクまたはアンダーバーで囲むらしい  
`*ガンガン行こうぜ*` => *ガンガン行こうぜ*  
`**いのちを大事に**` => **いのちを大事に**  

##見出し
\#見出しH1
\#\#見出しH2
\#\#\#見出しH3
\#\#\#\#見出しH4
\#\#\#\#\#見出しH5
\#\#\#\#\#\#見出しH6

##水平線
```
---------------------------------------------  
*********************************************  
```
↓
---------------------------------------------  
*********************************************  

##コードの表示
バッククォートをつかう  
\`$hello = "hello, world"; \` => `$hello = "hello, world"; `  

複数行  
\`\`\`  
hogehogehoge  
\`\`\`  
↓
```
hogehogehoge
```

##画像
下記で貼り付けれる  
\!\[alt\]\(url\)  
\!\[alt\]\(url "title"\)  
  
`![codelike](http://codelike.info/images/codelike_logo.png "codelike")`  
![codelike](http://codelike.info/images/codelike_logo.png "codelike")  

##リンク
```
[リンクのテキスト][linkref]  
[linkref]: リンクのアドレス "リンクのタイトル"
```
  
[google]: http://google.com/ "Google"  
[yahoo]:  http://search.yahoo.com/ "Yahoo Search"  
[msn]:    http://search.msn.com/ "MSN Search"  
[codelike]:    http://codelike.info/ "CodeLike"  
  
##エスケープ
バックスラッシュ = \

\:smile:
\:smile:
\:smile:
