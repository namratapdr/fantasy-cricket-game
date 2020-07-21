#To calculate the man of the match
import points,sqlite3
#players
db = sqlite3.connect("fanatasy-cricket.db")
cursordb = db.cursor()
totalPoints = 0
sql = "SELECT * FROM match2;"

cursordb.execute(sql)
while True:
    record = cursordb.fetchone()
    if record == None:
        break
    print(record)
    pointsCalc = points.bat(record)
    pointsCalc += points.bowl(record)
    totalPoints += pointsCalc
    print(record[0] ,": ", pointsCalc)
print("Total Points: ",totalPoints)

db.close()
