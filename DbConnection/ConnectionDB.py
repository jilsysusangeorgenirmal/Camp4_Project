import configparser, pymysql
from pymysql.err import MySQLError

class ConnectionDB:
    """here we are using singleton  design pattern"""
    """this class will create only one instance"""

    #singleton design pattern: create a object in a class, and using that object, 
    # so that in heap memory only one object is used resulting performance speed.

    __instance = None #hold or stores the singleton instance

    #override inbuilt method to achieve single ton
    def __new__(cls): #__new__(cls) special method to create a new object
        """
        Ensures only one instance of ConnectionDb is ceated 
        """
        if cls.__instance is None: #if no instance is created
            cls.__instance = super(ConnectionDB, cls).__new__(cls)
            cls.__instance.__initialize()#intialize the connection once 
        return cls.__instance
        
    def __initialize(self):
        """
       initialize the database coonection using properties from the db_config.ini
        """
        try:
            #load the congiguration file
            config = configparser.ConfigParser() #ConfigParser is class and config is object created from it
            config.read("db_config.ini")
            """
            configparser is a built-in Python module used to work with configuration files (usually .ini files).
            configparser allows you to:
                # Read configuration files
                # Write configuration files
                # Update and delete configuration values
                # Store settings in sections and key–value pairs
            """

            #establish the mysql connection
            self.connection = pymysql.connect(
                host = config.get("mysql","host"),
                user = config.get("mysql","user"),
                password = config.get("mysql","password"),
                database = config.get("mysql", "database")
            )
            print("Connected to MYSQL database...")
        except MySQLError as e:
            print(f"Error while connecting to MYSQL:{e}")
            self.connection = None
    
    def get_connection(self):
        return self.connection #object