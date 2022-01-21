import mysql.connector


def database_sample():
    with open("config.txt") as f:
        for line in f:
            user, password = line.split(" ")

    connection = mysql.connector.connect(
        user=user, password=password, host="localhost", database="testowa", auth_plugin="mysql_native_password")

    query = "SELECT * FROM People"
    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print(row)


def main():
    database_sample()


if __name__ == "__main__":
    main()
