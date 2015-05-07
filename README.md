# Python
code for work
圖檔找尋

Search.py + searchlist.txt

自動搜尋並備份搜尋圖片結果,同時回報結果和模糊搜尋功能(for color)


目錄製作

catalog.py

將同一資料夾內1:1比例的圖片自動生成每頁5x5個樣品目錄

catalog_BZ.py

將同一資料夾內4:1比例的圖片自動生成每頁2x8個樣品目錄

pdf_merge.py

將同一資料夾內pdf目錄整合成一個檔案


*需安裝pyPdf-1.13.win32.exe與CuteWriter.exe


目錄圖製作

resizeJPG.py

將同一資料夾內圖檔自動產生300x300px 縮小目錄圖(無產品型號)

resizeJPGwName.py

將同一資料夾內圖檔自動產生300x300px 縮小目錄圖(有產品型號)


*需安裝Pillow-2.6.1.win32-py2.7.exe與PIL-1.1.7.win32-py2.7.exe


檔名更改

rename_Quick_cata.py

將同一資料夾內圖檔檔名自動改名僅有產品型號

圖檔找尋

1. Search.py 將自動搜尋 searchlist.txt 裡的產品圖片. 
在找尋之前會詢問是否需要針對color 的fuzzy search, 請輸入(Y/N)選擇. 

2. searchlist.txt 中格式須為TYPE-ITEM-COLOR, 例如ET-2631-AT. 最後一行需為斷行符號(Enter鍵)

3. Search.py script 將於同一資料夾中自動產生result資料夾和nofoundlist.txt 
在每次執行新的搜尋前,請先清空result資料夾以確保結果正確


目錄製作

1. 安裝pyPdf-1.13.win32.exe與CuteWriter.exe以確保能夠合併與列印PDF檔案

2. 將目錄製作所需圖檔與python script置於同一資料夾中

3. 執行catalog.py或catalog_BZ.py將會自動產生catalog.html 目錄網頁檔,選擇 File -> Print Preview, 確定 Scale 值為 Shrink To Fit; Margin 均為0.5; Header/Footer 均為 --blank-- 

4. Print 選擇PDF Printer 即可
