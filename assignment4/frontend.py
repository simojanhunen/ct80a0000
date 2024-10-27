import pymongo
import psycopg2


def main_menu():
    print("\n1) Print data")
    print("2) Insert data")
    print("3) Delete data")
    print("4) Modify data")
    print("0) Exit")


def fetch_databases():
    sql_conn = psycopg2.connect(
        dbname="peopledb",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )

    nosql_client = pymongo.MongoClient("mongodb://localhost:27017/")

    return sql_conn, nosql_client


def main():
    sql_conn, nosql_client = fetch_databases()

    curr = sql_conn.cursor()
    db = nosql_client["countrydb"]
    collection = db["country"]

    while 1:
        main_menu()
        user_input = input("Please make your selection: ")

        match user_input:
            case "0":
                break
            case "1":
                db_type_input = input(
                    "Please make your selection (0 = SQL, 1 = NoSQL, 2 = Both): "
                )
                match db_type_input:
                    case "0":
                        curr.execute("SELECT * FROM people")
                        for table in curr.fetchall():
                            print(table)
                    case "1":
                        entries = collection.find()
                        for entry in entries:
                            print(entry)
                    case "2":
                        all_entries = []

                        # Add SQL entries first
                        curr.execute("SELECT * FROM people")
                        for table in curr.fetchall():
                            all_entries.append(list(table))

                        # Join NoSQL entries
                        new_entries = list(collection.find())

                        for old_entry in all_entries:
                            for new_entry in new_entries:
                                if old_entry[3] == new_entry["country"]:
                                    old_entry.append(new_entry["isd"])

                        for entry in all_entries:
                            print(entry)
                    case _:
                        print("Erronous input, try again!")
            case "2":
                db_type_input = input(
                    "Please make your selection (0 = SQL, 1 = NoSQL): "
                )
                match db_type_input:
                    case "0":
                        name = input("Provide the name: ")
                        email = input("Provide the email: ")
                        country = input("Provide the country: ")
                        phonenumber = input("Provide the phone number: ")
                        curr.execute(f"""
                            INSERT INTO people (name, email, country, phonenumber)
                            VALUES  ('{name}', '{email}', '{country}', {int(phonenumber)});
                        """)
                    case "1":
                        country = input("Provide the country: ")
                        isd = input("Provide the ISD code: ")
                        collection.insert_one({"country": country, "isd": isd})
                    case _:
                        print("Erronous input, try again!")
            case "3":
                db_type_input = input(
                    "Please make your selection (0 = SQL, 1 = NoSQL): "
                )
                match db_type_input:
                    case "0":
                        deleted_person = input("Who should be deleted: ")
                        curr.execute(f"""
                            DELETE FROM people WHERE name = '{deleted_person}';
                        """)
                    case "1":
                        deleted_country = input("Which country should be deleted: ")
                        delete_query = {"country": deleted_country}
                        collection.delete_one(delete_query)
                    case _:
                        print("Erronous input, try again!")
            case "4":
                db_type_input = input(
                    "Please make your selection (0 = SQL, 1 = NoSQL): "
                )
                match db_type_input:
                    case "0":
                        modified_person = input("Who's email should be updated: ")
                        new_email = input("New email address: ")
                        curr.execute(f"""
                            UPDATE people SET email = '{new_email}' WHERE name = '{modified_person}';
                        """)
                    case "1":
                        modified_country = input("Which country should be updated: ")
                        new_isd = int(input("What is the new value for ISD: "))
                        update_query = {"country": modified_country}
                        new_values = {"$set": {"isd": new_isd}}
                        collection.update_one(update_query, new_values)
                    case _:
                        print("Erronous input, try again!")
            case _:
                print("Erronous input, try again!")

    sql_conn.commit()
    sql_conn.close()
    nosql_client.close()
    print("Exiting...")


if __name__ == "__main__":
    main()
