import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "25278Jf!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}
def getData(db):
    mycursor = db.cursor()
    # studio query:
    mycursor.execute(("SELECT * FROM studio"))
    print("-- DISPLAYING Studio RECORDS --")
    studio = mycursor.fetchall()
    for studio in studio:
        print("Studio ID: {} \nStudio Name: {}\n".format(studio[0], studio[1]))
    # genre query:
    mycursor.execute(("SELECT * FROM genre"))
    print("-- DISPLAYING Genre RECORDS --")
    genre = mycursor.fetchall()
    for genre in genre:
        print("Genre ID: {} \nGenre Name: {}\n".format(genre[0], genre[1]))
    # short films query:
    mycursor.execute(("SELECT film_name, film_runtime FROM film where film_runtime<=120"))
    print("-- DISPLAYING Short Film RECORDS --")
    film = mycursor.fetchall()
    for film in film:
        print("Film Name: {} \nRuntime: {}\n".format(film[0], film[1]))
    #Director query:
    mycursor.execute(("SELECT film_name, film_director FROM film ORDER BY film_director ASC"))
    print("-- DISPLAYING Director RECORDS in Order --")
    director = mycursor.fetchall()
    for director in director:
        print("Film Name: {} \nDirector: {}\n".format(director[0], director[1]))
    input("Press [Enter] to exit.")
    exit()


try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press [Enter] to continue...")
    getData(db)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()


