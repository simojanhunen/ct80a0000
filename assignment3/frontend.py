import psycopg2


def fetch_database_cursors():
    turku_conn = psycopg2.connect(
        dbname="turkudb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )

    mumbai_conn = psycopg2.connect(
        dbname="mumbaidb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )

    rio_conn = psycopg2.connect(
        dbname="riodb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )

    return turku_conn, mumbai_conn, rio_conn


def handle_query(query, cursor):
    try:
        cursor.execute(query)
        for table in cursor.fetchall():
            print(table)
    except Exception as e:
        print(f"error: {e}")


def main_menu():
    print("\n1) Choose location")
    print("2) Print tables")
    print("3) Run a query")
    print("0) Exit")


def main():
    turku_conn, mumbai_conn, rio_conn = fetch_database_cursors()

    turku_curr = turku_conn.cursor()
    mumbai_curr = mumbai_conn.cursor()
    rio_curr = rio_conn.cursor()
    active_cursor = None

    while 1:
        main_menu()
        user_input = input("Please make your selection: ")

        match user_input:
            case "0":
                break
            case "1":
                print("\nAvailable locations")
                print("1) Turku")
                print("2) Mumbai")
                print("3) Rio De Janeiro")
                location_input = input("Please make your selection: ")

                match location_input:
                    case "1":
                        active_cursor = turku_curr
                    case "2":
                        active_cursor = mumbai_curr
                    case "3":
                        active_cursor = rio_curr
                    case _:
                        print("Erronous input, nothing happened")
            case "2":
                if active_cursor is None:
                    print("No active location selected")
                else:
                    handle_query(
                        """SELECT table_name
                        FROM information_schema.tables
                        WHERE table_schema = 'public'""",
                        active_cursor,
                    )
            case "3":
                if active_cursor is None:
                    print("No active location selected")
                else:
                    input_query = input("Please write your query: ")
                    handle_query(input_query, active_cursor)
            case _:
                print("Erronous input, try again!")

    turku_conn.commit()
    mumbai_conn.commit()
    rio_conn.commit()

    turku_curr.close()
    turku_conn.close()
    mumbai_curr.close()
    mumbai_conn.close()
    rio_curr.close()
    rio_conn.close()

    print("Exiting...")


if __name__ == "__main__":
    main()
