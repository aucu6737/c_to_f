#攝氏('C)轉換成華氏('F)程式
c = input('請輸入攝氏溫度')
c = float(c) #因為溫度是有可能有小數點的，所以用float
f = c * 9 / 5 + 32 #記得每個符號後面都要加上空格
print('華氏溫度為: ', f)