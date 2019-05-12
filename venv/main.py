import deck,card,comparisons,player,table,round,disconnects

table = table.Table(2000)
table.createPlayer("Steven",20000).createPlayer("Daniel",15000).createPlayer("Kostas",10000).assignBlinds()

print("The table is:"+str(table.getTableInfo()))
print("The active player is: "+str(table.getPlayers()[0].getPlayerInfo())+str(table.getPlayers()[1].getPlayerInfo())+str(table.getPlayers()[2].getPlayerInfo()))