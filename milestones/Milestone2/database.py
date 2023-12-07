import os

import pymysql.cursors

db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

class Database:
    @staticmethod
    def connect():
        try:
            conn = pymysql.connect(host=db_host,
                                   port=3306,
                                   user=db_username,
                                   password=db_password,
                                   db=db_name,
                                   charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
            return conn
        except pymysql.MySQLError as err:
            print(f"An error occurred: {err}")
            return None

    @staticmethod
    def get_response(query, values=None, fetch=False, many_entities=False):
        conn = Database.connect()
        if conn is None:
            return None

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, values)
                if fetch:
                    response = cursor.fetchall() if many_entities else cursor.fetchone()

                else:
                    conn.commit()
                    response = None
        except pymysql.MySQLError as err:
            print(f"An error occurred: {err}")
            conn.rollback()
            response = None
        finally:
            conn.close()
        return response

    @staticmethod
    def select(query, values=None):
        return Database.get_response(query, values=values, fetch=True, many_entities=True)

    @staticmethod
    def insert(query, values=None):
        return Database.get_response(query, values=values)

    @staticmethod
    def update(query, values=None):
        return Database.get_response(query, values=values)

    @staticmethod
    def delete(query, values=None):
        return Database.get_response(query, values=values)

class Query:
  # User Queries
  CREATE_USER = "INSERT INTO user (username, email, date_joined, last_login) VALUES (%s, %s, %s, %s)"
  READ_USER = "SELECT * FROM user WHERE user_id = %s"
  UPDATE_USER = "UPDATE user SET username = %s, email = %s, last_login = %s WHERE user_id = %s"
  DELETE_USER = "DELETE FROM user WHERE user_id = %s"

  # Mission Queries
  CREATE_MISSION = "INSERT INTO Mission (start_date, end_date, objective, status) VALUES (%s, %s, %s, %s)"
  READ_MISSION = "SELECT * FROM Mission WHERE mission_id = %s"
  UPDATE_MISSION = "UPDATE Mission SET start_date = %s, end_date = %s, objective = %s, status = %s WHERE mission_id = %s"
  DELETE_MISSION = "DELETE FROM Mission WHERE mission_id = %s"

  # Rover Queries
  CREATE_ROVER = "INSERT INTO Rover (name, launch_date, arrival_date, status, Mission_mission_id) VALUES (%s, %s, %s, %s, %s)"
  READ_ROVER = "SELECT * FROM Rover WHERE rover_id = %s"
  UPDATE_ROVER = "UPDATE Rover SET name = %s, launch_date = %s, arrival_date = %s, status = %s WHERE rover_id = %s"
  DELETE_ROVER = "DELETE FROM Rover WHERE rover_id = %s"
  
  # Mars Queries
  CREATE_MARS = "INSERT INTO Mars (region, atmosphere_composition, surface_conditions, Mission_mission_id) VALUES (%s, %s, %s, %s)"
  READ_MARS = "SELECT * FROM Mars WHERE mars_id = %s"
  UPDATE_MARS = "UPDATE Mars SET region = %s, atmosphere_composition = %s, surface_conditions = %s WHERE mars_id = %s"
  DELETE_MARS = "DELETE FROM Mars WHERE mars_id = %s"

  # Martian Terrain Queries
  CREATE_TERRAIN = "INSERT INTO `Martian Terrain` (mineral_composition, characteristics, Mars_mars_id) VALUES (%s, %s, %s)"
  READ_TERRAIN = "SELECT * FROM `Martian Terrain` WHERE terrain_id = %s"
  UPDATE_TERRAIN = "UPDATE `Martian Terrain` SET mineral_composition = %s, characteristics = %s WHERE terrain_id = %s"
  DELETE_TERRAIN = "DELETE FROM `Martian Terrain` WHERE terrain_id = %s"

  # Research Document Queries
  CREATE_DOCUMENT = "INSERT INTO `Research Document` (title, author_id, publish_date, `Research Team_team_id`) VALUES (%s, %s, %s, %s)"
  READ_DOCUMENT = "SELECT * FROM `Research Document` WHERE document_id = %s"
  UPDATE_DOCUMENT = "UPDATE `Research Document` SET title = %s, publish_date = %s WHERE document_id = %s"
  DELETE_DOCUMENT = "DELETE FROM `Research Document` WHERE document_id = %s"

  # Training Module Queries
  CREATE_MODULE = "INSERT INTO `Training Module` (title, length, difficulty_level) VALUES (%s, %s, %s)"
  READ_MODULE = "SELECT * FROM `Training Module` WHERE module_id = %s"
  UPDATE_MODULE = "UPDATE `Training Module` SET title = %s, length = %s, difficulty_level = %s WHERE module_id = %s"
  DELETE_MODULE = "DELETE FROM `Training Module` WHERE module_id = %s"

  # Notification System Queries
  CREATE_NOTIFICATION = "INSERT INTO `Notification System` (type, message, date_sent, user_user_id) VALUES (%s, %s, %s, %s)"
  READ_NOTIFICATION = "SELECT * FROM `Notification System` WHERE notification_id = %s"
  UPDATE_NOTIFICATION = "UPDATE `Notification System` SET type = %s, message = %s, date_sent = %s WHERE notification_id = %s"
  DELETE_NOTIFICATION = "DELETE FROM `Notification System` WHERE notification_id = %s"

  # API Access Queries
  CREATE_API_ACCESS = "INSERT INTO `API Access` (access_level, issue_date, expiry_date, user_user_id) VALUES (%s, %s, %s, %s)"
  READ_API_ACCESS = "SELECT * FROM `API Access` WHERE apikey_id = %s"
  UPDATE_API_ACCESS = "UPDATE `API Access` SET access_level = %s, expiry_date = %s WHERE apikey_id = %s"
  DELETE_API_ACCESS = "DELETE FROM `API Access` WHERE apikey_id = %s"

  # Role Queries
  CREATE_ROLE = "INSERT INTO Role (role_name, permissions) VALUES (%s, %s)"
  READ_ROLE = "SELECT * FROM Role WHERE role_id = %s"
  UPDATE_ROLE = "UPDATE Role SET role_name = %s, permissions = %s WHERE role_id = %s"
  DELETE_ROLE = "DELETE FROM Role WHERE role_id = %s"

  # Account Queries
  CREATE_ACCOUNT = "INSERT INTO Account (user_id, created_date, last_activity_date) VALUES (%s, %s, %s)"
  READ_ACCOUNT = "SELECT * FROM Account WHERE account_id = %s"
  UPDATE_ACCOUNT = "UPDATE Account SET created_date = %s, last_activity_date = %s WHERE account_id = %s"
  DELETE_ACCOUNT = "DELETE FROM Account WHERE account_id = %s"

  # Saved Searches Queries
  CREATE_SAVED_SEARCH = "INSERT INTO `Saved Searches` (account_id, search_query, user_user_id) VALUES (%s, %s, %s)"
  READ_SAVED_SEARCH = "SELECT * FROM `Saved Searches` WHERE search_id = %s"
  UPDATE_SAVED_SEARCH = "UPDATE `Saved Searches` SET search_query = %s WHERE search_id = %s"
  DELETE_SAVED_SEARCH = "DELETE FROM `Saved Searches` WHERE search_id = %s"

  # Mission Sensors Queries
  CREATE_MISSION_SENSOR = "INSERT INTO `Mission Sensors` (sensor_id, satellite_id, Mission_mission_id, Machine_machine_id) VALUES (%s, %s, %s, %s)"
  READ_MISSION_SENSOR = "SELECT * FROM `Mission Sensors` WHERE mission_sensors_id = %s"
  UPDATE_MISSION_SENSOR = "UPDATE `Mission Sensors` SET sensor_id = %s, satellite_id = %s, Mission_mission_id = %s, Machine_machine_id = %s WHERE mission_sensors_id = %s"
  DELETE_MISSION_SENSOR = "DELETE FROM `Mission Sensors` WHERE mission_sensors_id = %s"

  # Discussion Replies Queries
  CREATE_REPLY = "INSERT INTO `Discussion Replies` (thread_id, reply_text, reply_date, user_user_id) VALUES (%s, %s, %s, %s)"
  READ_REPLY = "SELECT * FROM `Discussion Replies` WHERE reply_id = %s"
  UPDATE_REPLY = "UPDATE `Discussion Replies` SET reply_text = %s, reply_date = %s WHERE reply_id = %s"
  DELETE_REPLY = "DELETE FROM `Discussion Replies` WHERE reply_id = %s"

  # Document Citations Queries
  CREATE_CITATION = "INSERT INTO `Document Citations` (document_id, citation_text) VALUES (%s, %s)"
  READ_CITATION = "SELECT * FROM `Document Citations` WHERE citation_id = %s"
  UPDATE_CITATION = "UPDATE `Document Citations` SET citation_text = %s WHERE citation_id = %s"
  DELETE_CITATION = "DELETE FROM `Document Citations` WHERE citation_id = %s"

  # Module Feedback Queries
  CREATE_FEEDBACK = "INSERT INTO `Module Feedback` (module_id, rating, comment, user_user_id) VALUES (%s, %s, %s, %s)"
  READ_FEEDBACK = "SELECT * FROM `Module Feedback` WHERE feedback_id = %s"
  UPDATE_FEEDBACK = "UPDATE `Module Feedback` SET rating = %s, comment = %s WHERE feedback_id = %s"
  DELETE_FEEDBACK = "DELETE FROM `Module Feedback` WHERE feedback_id = %s"

  # Mailing List Queries
  CREATE_MAILING_LIST = "INSERT INTO `Mailing List` (name, description) VALUES (%s, %s)"
  READ_MAILING_LIST = "SELECT * FROM `Mailing List` WHERE list_id = %s"
  UPDATE_MAILING_LIST = "UPDATE `Mailing List` SET name = %s, description = %s WHERE list_id = %s"
  DELETE_MAILING_LIST = "DELETE FROM `Mailing List` WHERE list_id = %s"

  # Payment Queries
  CREATE_PAYMENT = "INSERT INTO Payment (amount, date, method, user_user_id, Account_account_id) VALUES (%s, %s, %s, %s, %s)"
  READ_PAYMENT = "SELECT * FROM Payment WHERE payment_id = %s"
  UPDATE_PAYMENT = "UPDATE Payment SET amount = %s, date = %s, method = %s WHERE payment_id = %s"
  DELETE_PAYMENT = "DELETE FROM Payment WHERE payment_id = %s"

  # Weather Queries
  CREATE_WEATHER = "INSERT INTO Weather (temperature, pressure, wind_speed, Mission_mission_id) VALUES (%s, %s, %s, %s)"
  READ_WEATHER = "SELECT * FROM Weather WHERE weather_id = %s"
  UPDATE_WEATHER = "UPDATE Weather SET temperature = %s, pressure = %s, wind_speed = %s WHERE weather_id = %s"
  DELETE_WEATHER = "DELETE FROM Weather WHERE weather_id = %s"

  # User Has Mailing List Queries
  LINK_USER_MAILING_LIST = "INSERT INTO user_has_Mailing_List (user_user_id, Mailing_List_list_id) VALUES (%s, %s)"
  UNLINK_USER_MAILING_LIST = "DELETE FROM user_has_Mailing_List WHERE user_user_id = %s AND Mailing_List_list_id = %s"

  # Research Team Has User Queries
  LINK_RESEARCH_TEAM_USER = "INSERT INTO Research_Team_has_user (Research_Team_team_id, user_user_id) VALUES (%s, %s)"
  UNLINK_RESEARCH_TEAM_USER = "DELETE FROM Research_Team_has_user WHERE Research_Team_team_id = %s AND user_user_id = %s"

  # Martian Terrain Has Mission Queries
  LINK_TERRAIN_MISSION = "INSERT INTO Martian_Terrain_has_Mission (Martian_Terrain_terrain_id, Mission_mission_id) VALUES (%s, %s)"
  UNLINK_TERRAIN_MISSION = "DELETE FROM Martian_Terrain_has_Mission WHERE Martian_Terrain_terrain_id = %s AND Mission_mission_id = %s"

  # Training Module Has User Queries
  LINK_MODULE_USER = "INSERT INTO Training_Module_has_user (Training_Module_module_id, user_user_id) VALUES (%s, %s)"
  UNLINK_MODULE_USER = "DELETE FROM Training_Module_has_user WHERE Training_Module_module_id = %s AND user_user_id = %s"

  # User Has Role Queries
  ASSIGN_ROLE_TO_USER = "INSERT INTO user_has_Role (user_user_id, Role_role_id) VALUES (%s, %s)"
  REVOKE_ROLE_FROM_USER = "DELETE FROM user_has_Role WHERE user_user_id = %s AND Role_role_id = %s"

  # Role Has Account Queries
  LINK_ROLE_ACCOUNT = "INSERT INTO Role_has_Account (Role_role_id, Account_account_id) VALUES (%s, %s)"
  UNLINK_ROLE_ACCOUNT = "DELETE FROM Role_has_Account WHERE Role_role_id = %s AND Account_account_id = %s"

  # Visualization Queries
  CREATE_VISUALIZATION = "INSERT INTO Visualization (created_by) VALUES (%s)"
  READ_VISUALIZATION = "SELECT * FROM Visualization WHERE Visualization_id = %s"
  UPDATE_VISUALIZATION = "UPDATE Visualization SET created_by = %s WHERE Visualization_id = %s"
  DELETE_VISUALIZATION = "DELETE FROM Visualization WHERE Visualization_id = %s"

  # Dataset Queries
  CREATE_DATASET = "INSERT INTO Dataset (source_id, date_collected, Mission_mission_id, Visualization_Visualization_id) VALUES (%s, %s, %s, %s)"
  READ_DATASET = "SELECT * FROM Dataset WHERE dataset_id = %s"
  UPDATE_DATASET = "UPDATE Dataset SET source_id = %s, date_collected = %s, Mission_mission_id = %s, Visualization_Visualization_id = %s WHERE dataset_id = %s"
  DELETE_DATASET = "DELETE FROM Dataset WHERE dataset_id = %s"

  # Machine Queries
  CREATE_MACHINE = "INSERT INTO Machine (type, status, location, Mission_mission_id) VALUES (%s, %s, %s, %s)"
  READ_MACHINE = "SELECT * FROM Machine WHERE machine_id = %s"
  UPDATE_MACHINE = "UPDATE Machine SET type = %s, status = %s, location = %s WHERE machine_id = %s"
  DELETE_MACHINE = "DELETE FROM Machine WHERE machine_id = %s"

  # Components Queries
  CREATE_COMPONENT = "INSERT INTO Components (type, status, data_output, Machine_machine_id) VALUES (%s, %s, %s, %s)"
  READ_COMPONENT = "SELECT * FROM Components WHERE component_id = %s"
  UPDATE_COMPONENT = "UPDATE Components SET type = %s, status = %s, data_output = %s WHERE component_id = %s"
  DELETE_COMPONENT = "DELETE FROM Components WHERE component_id = %s"

  # Research Team Queries
  CREATE_RESEARCH_TEAM = "INSERT INTO `Research Team` (team_name, lead_researcher) VALUES (%s, %s)"
  READ_RESEARCH_TEAM = "SELECT * FROM `Research Team` WHERE team_id = %s"
  UPDATE_RESEARCH_TEAM = "UPDATE `Research Team` SET team_name = %s, lead_researcher = %s WHERE team_id = %s"
  DELETE_RESEARCH_TEAM = "DELETE FROM `Research Team` WHERE team_id = %s"

  # Discussion Thread Queries
  CREATE_DISCUSSION_THREAD = "INSERT INTO `Discussion Thread` (title, created_by, created_date, user_user_id) VALUES (%s, %s, %s, %s)"
  READ_DISCUSSION_THREAD = "SELECT * FROM `Discussion Thread` WHERE Thread_id = %s"
  UPDATE_DISCUSSION_THREAD = "UPDATE `Discussion Thread` SET title = %s, created_by = %s, created_date = %s WHERE Thread_id = %s"
  DELETE_DISCUSSION_THREAD = "DELETE FROM `Discussion Thread` WHERE Thread_id = %s"

