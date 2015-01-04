@ECHO OFF
set /p FolderPath="Paste absolute folder path and hit enter: "
dir /b "%FolderPath%" > "C:/list.txt"
start C:/list.txt