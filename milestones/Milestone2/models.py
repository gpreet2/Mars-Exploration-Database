"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""
from database import Database, Query


class TestModel:
  """
  This is an object model example. Note that
  this model doesn't implement a DB connection.
  """

  def __init__(self, ctx):
      self.ctx = ctx
      self.author = ctx.message.author.name

  def response(self):
      return f'Hi, {self.author}. I am alive'

class UserModel:
  def __init__(self, user_id=None):
      self.user_id = user_id

  def create_user(self, username, email, date_joined, last_login):
      return Database.insert(Query.CREATE_USER, (username, email, date_joined, last_login))

  def read_user(self):
      return Database.select(Query.READ_USER, (self.user_id, ))

  def update_user(self, username, email, last_login):
      return Database.update(Query.UPDATE_USER, (username, email, last_login, self.user_id))

  def delete_user(self):
      return Database.delete(Query.DELETE_USER, (self.user_id, ))



class MissionModel:
  def __init__(self, mission_id=None):
      self.mission_id = mission_id

  def create_mission(self, start_date, end_date, objective, status):
      return Database.insert(Query.CREATE_MISSION, (start_date, end_date, objective, status))

  def read_mission(self):
      return Database.select(Query.READ_MISSION, (self.mission_id, ))

  def update_mission(self, start_date, end_date, objective, status):
      return Database.update(Query.UPDATE_MISSION, (start_date, end_date, objective, status, self.mission_id))

  def delete_mission(self):
      return Database.delete(Query.DELETE_MISSION, (self.mission_id, ))


class RoverModel:
  def __init__(self, rover_id=None):
      self.rover_id = rover_id

  def create_rover(self, name, launch_date, arrival_date, status, mission_id):
      return Database.insert(Query.CREATE_ROVER, (name, launch_date, arrival_date, status, mission_id))

  def read_rover(self):
      return Database.select(Query.READ_ROVER, (self.rover_id, ))

  def update_rover(self, name, launch_date, arrival_date, status):
      return Database.update(Query.UPDATE_ROVER, (name, launch_date, arrival_date, status, self.rover_id))

  def delete_rover(self):
      return Database.delete(Query.DELETE_ROVER, (self.rover_id, ))


class MarsModel:
  def __init__(self, mars_id=None):
      self.mars_id = mars_id

  def create_mars(self, region, atmosphere_composition, surface_conditions, mission_id):
      return Database.insert(Query.CREATE_MARS, (region, atmosphere_composition, surface_conditions, mission_id))

  def read_mars(self):
      return Database.select(Query.READ_MARS, (self.mars_id, ))

  def update_mars(self, region, atmosphere_composition, surface_conditions):
      return Database.update(Query.UPDATE_MARS, (region, atmosphere_composition, surface_conditions, self.mars_id))

  def delete_mars(self):
      return Database.delete(Query.DELETE_MARS, (self.mars_id, ))


class MartianTerrainModel:
  def __init__(self, terrain_id=None):
      self.terrain_id = terrain_id

  def create_terrain(self, mineral_composition, characteristics, mars_id):
      return Database.insert(Query.CREATE_TERRAIN, (mineral_composition, characteristics, mars_id))

  def read_terrain(self):
      return Database.select(Query.READ_TERRAIN, (self.terrain_id, ))

  def update_terrain(self, mineral_composition, characteristics):
      return Database.update(Query.UPDATE_TERRAIN, (mineral_composition, characteristics, self.terrain_id))

  def delete_terrain(self):
      return Database.delete(Query.DELETE_TERRAIN, (self.terrain_id, ))


class ResearchDocumentModel:
  def __init__(self, document_id=None):
      self.document_id = document_id

  def create_document(self, title, author_id, publish_date, team_id):
      return Database.insert(Query.CREATE_DOCUMENT, (title, author_id, publish_date, team_id))

  def read_document(self):
      return Database.select(Query.READ_DOCUMENT, (self.document_id, ))

  def update_document(self, title, publish_date):
      return Database.update(Query.UPDATE_DOCUMENT, (title, publish_date, self.document_id))

  def delete_document(self):
      return Database.delete(Query.DELETE_DOCUMENT, (self.document_id, ))


class TrainingModuleModel:
  def __init__(self, module_id=None):
      self.module_id = module_id

  def create_module(self, title, length, difficulty_level):
      return Database.insert(Query.CREATE_MODULE, (title, length, difficulty_level))

  def read_module(self):
      return Database.select(Query.READ_MODULE, (self.module_id, ))

  def update_module(self, title, length, difficulty_level):
      return Database.update(Query.UPDATE_MODULE, (title, length, difficulty_level, self.module_id))

  def delete_module(self):
      return Database.delete(Query.DELETE_MODULE, (self.module_id, ))



class NotificationSystemModel:
  def __init__(self, notification_id=None):
      self.notification_id = notification_id

  def create_notification(self, type, message, date_sent, user_id):
      return Database.insert(Query.CREATE_NOTIFICATION, (type, message, date_sent, user_id))

  def read_notification(self):
      return Database.select(Query.READ_NOTIFICATION, (self.notification_id, ))

  def update_notification(self, type, message, date_sent):
      return Database.update(Query.UPDATE_NOTIFICATION, (type, message, date_sent, self.notification_id))

  def delete_notification(self):
      return Database.delete(Query.DELETE_NOTIFICATION, (self.notification_id, ))


class APIAccessModel:
  def __init__(self, apikey_id=None):
      self.apikey_id = apikey_id

  def create_api_access(self, access_level, issue_date, expiry_date, user_id):
      return Database.insert(Query.CREATE_API_ACCESS, (access_level, issue_date, expiry_date, user_id))

  def read_api_access(self):
      return Database.select(Query.READ_API_ACCESS, (self.apikey_id, ))

  def update_api_access(self, access_level, expiry_date):
      return Database.update(Query.UPDATE_API_ACCESS, (access_level, expiry_date, self.apikey_id))

  def delete_api_access(self):
      return Database.delete(Query.DELETE_API_ACCESS, (self.apikey_id, ))


class RoleModel:
  def __init__(self, role_id=None):
      self.role_id = role_id

  def create_role(self, role_name, permissions):
      return Database.insert(Query.CREATE_ROLE, (role_name, permissions))

  def read_role(self):
      return Database.select(Query.READ_ROLE, (self.role_id, ))

  def update_role(self, role_name, permissions):
      return Database.update(Query.UPDATE_ROLE, (role_name, permissions, self.role_id))

  def delete_role(self):
      return Database.delete(Query.DELETE_ROLE, (self.role_id, ))



class AccountModel:
  def __init__(self, account_id=None):
      self.account_id = account_id

  def create_account(self, user_id, created_date, last_activity_date):
      return Database.insert(Query.CREATE_ACCOUNT, (user_id, created_date, last_activity_date))

  def read_account(self):
      return Database.select(Query.READ_ACCOUNT, (self.account_id, ))

  def update_account(self, created_date, last_activity_date):
      return Database.update(Query.UPDATE_ACCOUNT, (created_date, last_activity_date, self.account_id))

  def delete_account(self):
      return Database.delete(Query.DELETE_ACCOUNT, (self.account_id, ))


class SavedSearchesModel:
  def __init__(self, search_id=None):
      self.search_id = search_id

  def create_saved_search(self, account_id, search_query, user_id):
      return Database.insert(Query.CREATE_SAVED_SEARCH, (account_id, search_query, user_id))

  def read_saved_search(self):
      return Database.select(Query.READ_SAVED_SEARCH, (self.search_id, ))

  def update_saved_search(self, search_query):
      return Database.update(Query.UPDATE_SAVED_SEARCH, (search_query, self.search_id))

  def delete_saved_search(self):
      return Database.delete(Query.DELETE_SAVED_SEARCH, (self.search_id, ))



class MissionSensorsModel:
  def __init__(self, mission_sensors_id=None):
      self.mission_sensors_id = mission_sensors_id

  def create_mission_sensor(self, sensor_id, satellite_id, mission_id, machine_id):
      return Database.insert(Query.CREATE_MISSION_SENSOR, (sensor_id, satellite_id, mission_id, machine_id))

  def read_mission_sensor(self):
      return Database.select(Query.READ_MISSION_SENSOR, (self.mission_sensors_id, ))

  def update_mission_sensor(self, sensor_id, satellite_id, mission_id, machine_id):
      return Database.update(Query.UPDATE_MISSION_SENSOR, (sensor_id, satellite_id, mission_id, machine_id, self.mission_sensors_id))

  def delete_mission_sensor(self):
      return Database.delete(Query.DELETE_MISSION_SENSOR, (self.mission_sensors_id, ))


class DiscussionRepliesModel:
  def __init__(self, reply_id=None):
      self.reply_id = reply_id

  def create_reply(self, thread_id, reply_text, reply_date, user_id):
      return Database.insert(Query.CREATE_REPLY, (thread_id, reply_text, reply_date, user_id))

  def read_reply(self):
      return Database.select(Query.READ_REPLY, (self.reply_id, ))

  def update_reply(self, reply_text, reply_date):
      return Database.update(Query.UPDATE_REPLY, (reply_text, reply_date, self.reply_id))

  def delete_reply(self):
      return Database.delete(Query.DELETE_REPLY, (self.reply_id, ))


class DocumentCitationsModel:
  def __init__(self, citation_id=None):
      self.citation_id = citation_id

  def create_citation(self, document_id, citation_text):
      return Database.insert(Query.CREATE_CITATION, (document_id, citation_text))

  def read_citation(self):
      return Database.select(Query.READ_CITATION, (self.citation_id, ))

  def update_citation(self, citation_text):
      return Database.update(Query.UPDATE_CITATION, (citation_text, self.citation_id))

  def delete_citation(self):
      return Database.delete(Query.DELETE_CITATION, (self.citation_id, ))


class ModuleFeedbackModel:
  def __init__(self, feedback_id=None):
      self.feedback_id = feedback_id

  def create_feedback(self, module_id, rating, comment, user_id):
      return Database.insert(Query.CREATE_FEEDBACK, (module_id, rating, comment, user_id))

  def read_feedback(self):
      return Database.select(Query.READ_FEEDBACK, (self.feedback_id, ))

  def update_feedback(self, rating, comment):
      return Database.update(Query.UPDATE_FEEDBACK, (rating, comment, self.feedback_id))

  def delete_feedback(self):
      return Database.delete(Query.DELETE_FEEDBACK, (self.feedback_id, ))


class MailingListModel:
  def __init__(self, list_id=None):
      self.list_id = list_id

  def create_mailing_list(self, name, description):
      return Database.insert(Query.CREATE_MAILING_LIST, (name, description))

  def read_mailing_list(self):
      return Database.select(Query.READ_MAILING_LIST, (self.list_id, ))

  def update_mailing_list(self, name, description):
      return Database.update(Query.UPDATE_MAILING_LIST, (name, description, self.list_id))

  def delete_mailing_list(self):
      return Database.delete(Query.DELETE_MAILING_LIST, (self.list_id, ))


class PaymentModel:
  def __init__(self, payment_id=None):
      self.payment_id = payment_id

  def create_payment(self, amount, date, method, user_id, account_id):
      return Database.insert(Query.CREATE_PAYMENT, (amount, date, method, user_id, account_id))

  def read_payment(self):
      return Database.select(Query.READ_PAYMENT, (self.payment_id, ))

  def update_payment(self, amount, date, method):
      return Database.update(Query.UPDATE_PAYMENT, (amount, date, method, self.payment_id))

  def delete_payment(self):
      return Database.delete(Query.DELETE_PAYMENT, (self.payment_id, ))


class WeatherModel:
  def __init__(self, weather_id=None):
      self.weather_id = weather_id

  def create_weather(self, temperature, pressure, wind_speed, mission_id):
      return Database.insert(Query.CREATE_WEATHER, (temperature, pressure, wind_speed, mission_id))

  def read_weather(self):
      return Database.select(Query.READ_WEATHER, (self.weather_id, ))

  def update_weather(self, temperature, pressure, wind_speed):
      return Database.update(Query.UPDATE_WEATHER, (temperature, pressure, wind_speed, self.weather_id))

  def delete_weather(self):
      return Database.delete(Query.DELETE_WEATHER, (self.weather_id, ))




class UserHasMailingListModel:
  def link_user_mailing_list(self, user_id, list_id):
      return Database.insert(Query.LINK_USER_MAILING_LIST, (user_id, list_id))

  def unlink_user_mailing_list(self, user_id, list_id):
      return Database.delete(Query.UNLINK_USER_MAILING_LIST, (user_id, list_id))

class ResearchTeamHasUserModel:
  def link_research_team_user(self, team_id, user_id):
      return Database.insert(Query.LINK_RESEARCH_TEAM_USER, (team_id, user_id))

  def unlink_research_team_user(self, team_id, user_id):
      return Database.delete(Query.UNLINK_RESEARCH_TEAM_USER, (team_id, user_id))


class MartianTerrainHasMissionModel:
  def link_terrain_mission(self, terrain_id, mission_id):
      return Database.insert(Query.LINK_TERRAIN_MISSION, (terrain_id, mission_id))

  def unlink_terrain_mission(self, terrain_id, mission_id):
      return Database.delete(Query.UNLINK_TERRAIN_MISSION, (terrain_id, mission_id))


class TrainingModuleHasUserModel:
  def link_module_user(self, module_id, user_id):
      return Database.insert(Query.LINK_MODULE_USER, (module_id, user_id))

  def unlink_module_user(self, module_id, user_id):
      return Database.delete(Query.UNLINK_MODULE_USER, (module_id, user_id))


class UserHasRoleModel:
  def assign_role_to_user(self, user_id, role_id):
      return Database.insert(Query.ASSIGN_ROLE_TO_USER, (user_id, role_id))

  def revoke_role_from_user(self, user_id, role_id):
      return Database.delete(Query.REVOKE_ROLE_FROM_USER, (user_id, role_id))


# Focuses on managing the assignment of roles to users.

class RoleHasAccountModel:
  def link_role_account(self, role_id, account_id):
      return Database.insert(Query.LINK_ROLE_ACCOUNT, (role_id, account_id))

  def unlink_role_account(self, role_id, account_id):
      return Database.delete(Query.UNLINK_ROLE_ACCOUNT, (role_id, account_id))


# Manages the relationship between Roles and Accounts.


class VisualizationModel:
  def __init__(self, visualization_id=None):
      self.visualization_id = visualization_id

  def create_visualization(self, created_by):
      return Database.insert(Query.CREATE_VISUALIZATION, (created_by, ))

  def read_visualization(self):
      return Database.select(Query.READ_VISUALIZATION, (self.visualization_id, ))

  def update_visualization(self, created_by):
      return Database.update(Query.UPDATE_VISUALIZATION, (created_by, self.visualization_id))

  def delete_visualization(self):
      return Database.delete(Query.DELETE_VISUALIZATION, (self.visualization_id, ))


class DatasetModel:
  def __init__(self, dataset_id=None):
      self.dataset_id = dataset_id

  def create_dataset(self, source_id, date_collected, mission_id, visualization_id):
      return Database.insert(Query.CREATE_DATASET, (source_id, date_collected, mission_id, visualization_id))

  def read_dataset(self):
      return Database.select(Query.READ_DATASET, (self.dataset_id, ))

  def update_dataset(self, source_id, date_collected, mission_id, visualization_id):
      return Database.update(Query.UPDATE_DATASET, (source_id, date_collected, mission_id, visualization_id, self.dataset_id))

  def delete_dataset(self):
      return Database.delete(Query.DELETE_DATASET, (self.dataset_id, ))


class MachineModel:
  def __init__(self, machine_id=None):
      self.machine_id = machine_id

  def create_machine(self, type, status, location, mission_id):
      return Database.insert(Query.CREATE_MACHINE, (type, status, location, mission_id))

  def read_machine(self):
      return Database.select(Query.READ_MACHINE, (self.machine_id, ))

  def update_machine(self, type, status, location):
      return Database.update(Query.UPDATE_MACHINE, (type, status, location, self.machine_id))

  def delete_machine(self):
      return Database.delete(Query.DELETE_MACHINE, (self.machine_id, ))


class ComponentsModel:
  def __init__(self, component_id=None):
      self.component_id = component_id

  def create_component(self, type, status, data_output, machine_id):
      return Database.insert(Query.CREATE_COMPONENT, (type, status, data_output, machine_id))

  def read_component(self):
      return Database.select(Query.READ_COMPONENT, (self.component_id, ))

  def update_component(self, type, status, data_output):
      return Database.update(Query.UPDATE_COMPONENT, (type, status, data_output, self.component_id))

  def delete_component(self):
      return Database.delete(Query.DELETE_COMPONENT, (self.component_id, ))


class ResearchTeamModel:
  def __init__(self, team_id=None):
      self.team_id = team_id

  def create_research_team(self, team_name, lead_researcher):
      return Database.insert(Query.CREATE_RESEARCH_TEAM, (team_name, lead_researcher))

  def read_research_team(self):
      return Database.select(Query.READ_RESEARCH_TEAM, (self.team_id, ))

  def update_research_team(self, team_name, lead_researcher):
      return Database.update(Query.UPDATE_RESEARCH_TEAM, (team_name, lead_researcher, self.team_id))

  def delete_research_team(self):
      return Database.delete(Query.DELETE_RESEARCH_TEAM, (self.team_id, ))

class DiscussionThreadModel:
  def __init__(self, thread_id=None):
      self.thread_id = thread_id

  def create_discussion_thread(self, title, created_by, created_date, user_id):
      return Database.insert(Query.CREATE_DISCUSSION_THREAD, (title, created_by, created_date, user_id))

  def read_discussion_thread(self):
      return Database.select(Query.READ_DISCUSSION_THREAD, (self.thread_id, ))

  def update_discussion_thread(self, title, created_by, created_date):
      return Database.update(Query.UPDATE_DISCUSSION_THREAD, (title, created_by, created_date, self.thread_id))

  def delete_discussion_thread(self):
      return Database.delete(Query.DELETE_DISCUSSION_THREAD, (self.thread_id, ))


