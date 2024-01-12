## ファイル処理プログラム

テキストベースのファイルを対象に特定のコマンドを入力すると、
ファイルの内容をすべて逆にしたり、ファイルの複製などができます。

## コマンド名

・reverse:　対象ファイルの内容を逆にしたものを新しいファイルとして作成します。  
・copy:　対象ファイルを複製します。  
・duplicate-contents:　対象ファイルの内容をN回複製し、複製したものをそのまま対象ファイルに追加します。  
・replace-string:　対象ファイルに含まれる文字を検索し、ヒットしたら文字を置換します。

## コマンド入力方法

・reverse  
　　python3 file_manipulator_program.py reverse 対象ファイル 新ファイル名
  
・copy  
　　python3 file_manipulator_program.py copy 対象ファイル
  
・duplicate-contents  
　　python3 file_manipulator_program.py duplicate-contents 対象ファイル 複製回数
  
・replace-string  
　　python3 file_manipulator_program.py replace-string 対象ファイル 置換前文字 置換後文字
