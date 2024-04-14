from database import Database
from CLI.Motorista_CLI import MotoristaCLI
from DAO.Motorista_DAO import MotoristaDAO

# Create an instance of Database
db = Database(database="Taxi", collection="Motorista")
# db.resetDatabase()

# Create an instance of MotoristaDAO
motorista_dao = MotoristaDAO(database=db)

# Pass motorista_dao instance to MotoristaCLI constructor
cli = MotoristaCLI(motorista_dao)
cli.menu()
