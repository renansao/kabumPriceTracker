from daoUtil import Conexao
from datetime import datetime

def insertKabumPricesToDatabase(item, kabumDict):

    sql = Conexao()

    sql.executeInsert("INSERT INTO hardware_analysis (analysisDate) VALUES (' " + str(datetime.now()) + "')")
    analysisUid = sql.executeQuery("SELECT max(analysisUid) from hardware_analysis")[0][0]

    for key, values in kabumDict.items():

        queryStr = "SELECT hardwareUid from hardware where hardwareName = '" + key + "'"
        hardwareUid = sql.executeQuery(queryStr)
        if len(hardwareUid) == 0:
            sql.executeInsert("INSERT INTO hardware (hardwareType, hardwareName) VALUES (" + item +", '" + key + "')")
            hardwareUid = sql.executeQuery("SELECT hardwareUid from hardware where hardwareName = '" + key + "'")
        
        valueStr = values['price'][3:].replace(".", "").replace(",", ".")
        valueFloat = float(valueStr)
        
        insertStr = 'INSERT INTO hardware_prices (hardwareuid, price, availability, analysisuid) VALUES (%s, %s, %s, %s)' % (hardwareUid[0][0], valueFloat, values["availability"], analysisUid)
        sql.executeInsert(insertStr)