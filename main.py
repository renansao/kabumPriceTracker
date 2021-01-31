import time
from kabumMain import retrieveKabumPrices
from utils import returnSmallestPricedGPUs
from terabyteMain import retrieveTerabytePrices
from daoUtil import Conexao
import psycopg2
from kabumDAO import insertKabumPricesToDatabase

insertKabumPricesToDatabase("2", retrieveKabumPrices("Placas de Vídeo"))
insertKabumPricesToDatabase("3", retrieveKabumPrices("Processadores"))
insertKabumPricesToDatabase("4", retrieveKabumPrices("Memoria ram"))
insertKabumPricesToDatabase("5", retrieveKabumPrices("HD"))
insertKabumPricesToDatabase("6", retrieveKabumPrices("SSD"))
insertKabumPricesToDatabase("7", retrieveKabumPrices("Placa mae"))
insertKabumPricesToDatabase("8", retrieveKabumPrices("Monitor"))
insertKabumPricesToDatabase("9", retrieveKabumPrices("Headset Gamer"))
insertKabumPricesToDatabase("10", retrieveKabumPrices("Mouse Gamer"))
insertKabumPricesToDatabase("11", retrieveKabumPrices("Teclado Gamer"))
insertKabumPricesToDatabase("12", retrieveKabumPrices("Gabinetes"))
insertKabumPricesToDatabase("13", retrieveKabumPrices("Coolers"))