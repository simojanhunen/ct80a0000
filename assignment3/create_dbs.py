import psycopg2


def setup_databases():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.autocommit = True
    cur = conn.cursor()

    for db in ["turkudb", "mumbaidb", "riodb"]:
        cur.execute(f"CREATE DATABASE {db}")

    cur.close()
    conn.close()

    conn = psycopg2.connect(
        dbname="turkudb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.autocommit = True

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE movies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            rating DECIMAL(3,1),
            lang VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE series (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            rating DECIMAL(3,1),
            lang VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100)
        );
    """)

    cur.execute("""
        CREATE TABLE subscription (
            id SERIAL PRIMARY KEY,
            userid INT,
            FOREIGN KEY (userid) REFERENCES users(id)
        );
    """)

    cur.execute("""
        INSERT INTO movies (title, rating, lang)
        VALUES  ('Tuntematon Sotilas', '8.0', 'Finnish'),
                ('Uuno Turhapuro', '5.9', 'Finnish'),
                ('Uuno Epsanjassa', '6.1', 'Finnish');
    """)

    cur.execute("""
        INSERT INTO series (title, rating, lang)
        VALUES  ('Kummeli', '8.4', 'Finnish'),
                ('Speden Spelit', '6.1', 'Finnish'),
                ('Pulttibois', '6.3', 'Finnish');
    """)

    cur.execute("""
        INSERT INTO users (username, email, password)
        VALUES  ('johndoe1', 'john@email.com', 'password123'),
                ('janesmith99', 'janesmith99@email.com', 'password123'),
                ('username1', 'myemail@email.com', 'asdasdasd');
    """)

    cur.execute("""
        INSERT INTO subscription (userid)
        VALUES  (1),
                (2);
    """)

    conn.close()
    cur.close()

    conn = psycopg2.connect(
        dbname="riodb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.autocommit = True

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE movies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            rating DECIMAL(3,1),
            lang VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE series (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            rating DECIMAL(3,1),
            lang VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100)
        );
    """)

    cur.execute("""
        CREATE TABLE subscription (
            id SERIAL PRIMARY KEY,
            userid INT,
            FOREIGN KEY (userid) REFERENCES users(id)
        );
    """)

    cur.execute("""
        INSERT INTO movies (title, rating, lang)
        VALUES  ('Elite Squad', '8.0', 'Portuguese'),
                ('Meu Pé de Laranja Lima', '7.1', 'Portuguese');
    """)

    cur.execute("""
        INSERT INTO series (title, rating, lang)
        VALUES  ('Ìdolo de Pano', '9.4', 'Portuguese'),
                ('Um Pé De Quê?', '9.4', 'Portuguese');
    """)

    cur.execute("""
        INSERT INTO users (username, email, password)
        VALUES  ('miguel4', 'miguel4@email.com', 'password123'),
                ('maria5', 'maria5@email.com', 'asdasdasd'),
                ('antonio2', 'antonio2@email.com', 'password321');
    """)

    cur.execute("""
        INSERT INTO subscription (userid)
        VALUES  (2),
                (1),
                (3);
    """)

    conn.close()
    cur.close()

    conn = psycopg2.connect(
        dbname="mumbaidb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.autocommit = True

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE movies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            rating DECIMAL(3,1),
            lang VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE series (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            rating DECIMAL(3,1),
            lang VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100)
        );
    """)

    cur.execute("""
        CREATE TABLE subscription (
            id SERIAL PRIMARY KEY,
            userid INT,
            FOREIGN KEY (userid) REFERENCES users(id)
        );
    """)

    cur.execute("""
        INSERT INTO movies (title, rating, lang)
        VALUES  ('The World of Apu', '8.7', 'Hindi'),
                ('Anbe Sivam', '8.6', 'Hindi');
    """)

    cur.execute("""
        INSERT INTO series (title, rating, lang)
        VALUES  ('Taaza Khabar', '8.1', 'Hindi'),
                ('Zindaginama', '8.9', 'Hindi');
    """)

    cur.execute("""
        INSERT INTO users (username, email, password)
        VALUES  ('raju123', 'raju123@email.com', 'asdasdasd'),
                ('sharma123', 'sharma123@email.com', 'password321'),
                ('rama77', 'rama77@email.com', 'mikespassword');
    """)

    cur.execute("""
        INSERT INTO subscription (userid)
        VALUES  (1),
                (2);
    """)

    conn.close()
    cur.close()


setup_databases()
