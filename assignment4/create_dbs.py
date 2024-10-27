import psycopg2
import pymongo


def setup_postgresql():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("CREATE DATABASE peopledb")

    conn.close()
    cur.close()

    conn = psycopg2.connect(
        dbname="peopledb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE people (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(100),
            country VARCHAR(100),
            phonenumber INTEGER
        );
    """)

    cur.execute("""
        INSERT INTO people (name, email, country, phonenumber)
        VALUES  ('Matti Meikäläinen', 'mm@jippii.fi', 'Finland', 345646456),
                ('Juri Saar', 'juri@eesti.ee', 'Estonia', 345634535),
                ('Harald Haraldsson', 'harald@oil.no', 'Norway', 345686347),
                ('Karl Karlsson', 'kk@epost.se', 'Sweden', 456728345);
    """)

    conn.close()
    cur.close()


def setup_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["countrydb"]
    col = db["country"]

    people = [
        {"country": "Finland", "isd": 358},
        {"country": "Estonia", "isd": 372},
        {"country": "Norway", "isd": 47},
        {"country": "Sweden", "isd": 46},
    ]

    col.insert_many(people)

    client.close()


def setup_databases():
    setup_postgresql()
    setup_mongodb()


setup_databases()
