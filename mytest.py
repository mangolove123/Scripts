from datetime import datetime
id_board = "5a1a9502e7d1b140dbf6a73a"
myresultDate = datetime.fromtimestamp(int(id_board[0:8],16))
print(myresultDate)








