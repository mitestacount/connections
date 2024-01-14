import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseTest:

    __database = "./data/example.db"

    @classmethod
    def __getconnection(cls):
        return sqlite3.connect(cls.__database)

    @classmethod
    def select_data(cls, query, parameters=None):
        return cls.__execute_query(query, parameters, fetch=True)

    @classmethod
    def insert_data(cls, query, parameters=None):
        cls.__execute_query(query, parameters, fetch=False)
        logger.info(f"Inserted : {query}, Parameters: {parameters}")

    @classmethod
    def update_data(cls, query, parameters=None):
        cls.__execute_query(query, parameters, fetch=False)
        logger.info(f"Updated: {query}, Parameters: {parameters}")

    @classmethod
    def delete_data(cls, query, parameters=None):
        cls.__execute_query(query, parameters, fetch=False)
        logger.info(f"Deleted: {query}, Parameters: {parameters}")

    @classmethod
    def __execute_query(cls, query, parameters=None, fetch=False):
        # Connect to SQLite database
        conn = cls.__getconnection()
        cursor = conn.cursor()

        try:
            # Execute the query
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)

            # Commit the changes for INSERT, UPDATE, DELETE
            if not fetch:
                conn.commit()
            # Fetch results for SELECT
            if fetch:
                result = cursor.fetchall()
                return result

        except Exception as e:
            logger.error(
                        f"Error executing query: {query}, "
                        f"Parameters: {parameters}, "
                        f"Error: {e}"
                    )
            raise
        finally:
            # Close the connection
            conn.close()


if __name__ == '__main__':
    # Example usage for SELECT:
    select_query = 'SELECT * FROM users'
    select_results = DatabaseTest.select_data(select_query)
    logger.info(f"SELECT Results: {select_results}")

    # Example usage for INSERT:
    insert_query = 'INSERT INTO users (username, email) VALUES (?, ?)'
    insert_params = ('new_user', 'new_user@example.com')
    DatabaseTest.insert_data(insert_query, parameters=insert_params)

    # Example usage for UPDATE:
    update_query = 'UPDATE users SET email = ? WHERE username = ?'
    update_params = ('updated_email@example.com', 'existing_user')
    DatabaseTest.update_data(update_query, parameters=update_params)

    # Example usage for DELETE:
    #delete_query = 'DELETE FROM users WHERE username = ?'
    #delete_params = ('user_to_delete',)
    #DatabaseTest.delete_data(delete_query, parameters=delete_params)
