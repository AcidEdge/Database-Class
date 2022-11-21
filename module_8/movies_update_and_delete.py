# Mark Witt
# CSD-310 Module 8
# Update and delete tables in a database

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "25278Jf!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}


def show_films(mycursor, title):

    mycursor.execute("SELECT film_name as 'Film Name', film_director as Director, genre_name as Genre, studio_name as "
                     "'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON "
                     "film.studio_id=studio.studio_id")
    films = mycursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],
                                                                                         film[3]))


def insert_film(mycursor):
    # insert film method
    mycursor.execute("INSERT INTO movies.film (film_name, film_releaseDate, film_runtime, film_director, studio_id, "
                     "genre_id) VALUES ('The Empire Strikes Back', '1980', 124, 'Irvin Kershner', 1, 2)")

    show_films(mycursor, "DISPLAYING FILMS AFTER INSERT")


def update_film(mycursor):
    # update film method
    mycursor.execute("UPDATE film set genre_id=1 where film_name='Alien'")
    show_films(mycursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")


def delete_film(mycursor):
    mycursor.execute("DELETE from film WHERE film_name='Gladiator'")
    show_films(mycursor, "DISPLAYING FILMS AFTER DELETE")


try:
    db = mysql.connector.connect(**config)
    mycursor = db.cursor()
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press [Enter] to continue...")
    show_films(mycursor, "DISPLAYING FILMS")
    insert_film(mycursor)
    update_film(mycursor)
    delete_film(mycursor)
    db.commit()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
