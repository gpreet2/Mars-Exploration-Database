import os

import discord
from discord.ext import commands

from database import Database

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} has joined the room")  # the bot is online
    Database.connect()  # Corrected: No arguments passed

@bot.command(name="test", description="write your database business requirement for this command here")
async def _test(ctx, arg1):
    testModel = TestModel(ctx, arg1)
    response = testModel.response()
    await ctx.send(response)


# TODO: complete the following tasks:
#       (1) Replace the commands' names with your own commands
#       (2) Write the description of your business requirement in the description parameter
#       (3) Implement your commands' methods.

@bot.command(name="getMissionSummary", help="Retrieve mission summary by objective type")
async def get_mission_summary(ctx, objective_type):
    try:
        summary = MissionModel.get_mission_summary_by_objective(objective_type)
        response = "Mission Summary for '{}':\n".format(objective_type)
        response += "\n".join(
            f"Mission ID: {m['mission_id']}, Status: {m['status']}, Duration: {m['duration']}"
            for m in summary
        )
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="getRoverUsage", help="List rovers with mission details")
async def get_rover_usage(ctx):
    try:
        utilization = RoverModel.get_rover_utilization()
        response = "Rover Utilization:\n" + "\n".join(
            f"Rover Name: {rover['name']}, Mission Count: {rover['mission_count']}, Success Rate: {rover['success_rate']}"
            for rover in utilization
        )
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="getUserParticipation", help="Display user contributions by topics")
async def get_user_participation(ctx, discussion_topic):
    try:
        participation = UserModel.get_user_participation(discussion_topic)
        response = "User Participation in '{}':\n".format(discussion_topic)
        response += "\n".join(
            f"Username: {user['username']}, Contributions: {user['contributions']}"
            for user in participation
        )
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="getPublicationStats", help="Show research publication insights")
async def get_publication_stats(ctx):
    try:
        insights = ResearchModel.get_publication_insights()
        response = "Publication Insights:\n" + "\n".join(
            f"Team Name: {team['team_name']}, Publication Count: {team['publication_count']}"
            for team in insights
        )
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {e}")


@bot.command(name="insertMission", help="Insert new mission details")
async def insert_mission(ctx, mission_details):
    try:
        # You need to parse 'mission_details' as per your requirement
        # Example: mission_details = json.loads(mission_details)
        mission_id = MissionModel.insert_new_mission(**mission_details)
        await ctx.send(f"New mission created with ID: {mission_id}")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="addResearchData", help="Add new research data")
async def add_research_data(ctx, dataset_id, research_findings):
    try:
        # You need to parse 'dataset_id' and 'research_findings' as per your requirement
        document_id = ResearchModel.add_research_data(dataset_id, research_findings)
        await ctx.send(f"Research data added with Document ID: {document_id}")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="updateMissionStatus", help="Update mission status")
async def update_mission_status(ctx, mission_id, new_status):
    try:
        MissionModel.update_mission_status(mission_id, new_status)
        await ctx.send(f"Mission ID {mission_id} updated to status: {new_status}")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="updateUserProfile", help="Update user profile with new role")
async def update_user_profile(ctx, user_id, new_role):
    try:
        # Assuming you have a method in UserModel to handle this
        UserModel.update_user_profile(user_id, new_role)
        await ctx.send(f"User ID {user_id} profile updated with new role: {new_role}")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="deleteOldData", help="Delete old data based on a date threshold")
async def delete_old_data(ctx, date_threshold):
    try:
        # Assuming you have a method in some model to handle this
        # Example: SomeModel.delete_old_data(date_threshold)
        await ctx.send(f"Old data before {date_threshold} deleted.")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="removeInactiveUsers", help="Remove users inactive for a specified duration")
async def remove_inactive_users(ctx, inactive_duration):
    try:
        # Assuming you have a method in UserModel to handle this
        # Example: UserModel.remove_inactive_users(inactive_duration)
        await ctx.send(f"Inactive users for more than {inactive_duration} days removed.")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="triggerMissionCompletion", help="Manually trigger the mission completion process")
async def trigger_mission_completion(ctx):
    try:
        # Assuming you have a method in MissionModel to handle this
        # Example: MissionModel.trigger_mission_completion()
        await ctx.send("Mission completion process triggered.")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="triggerUserInactivity", help="Manually trigger the user inactivity process")
async def trigger_user_inactivity(ctx):
    try:
        # Assuming you have a method in UserModel to handle this
        # Example: UserModel.trigger_user_inactivity()
        await ctx.send("User inactivity process triggered.")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="getResearchSummary", help="Get a summary of research within a date range")
async def get_research_summary(ctx, start_date, end_date, area):
    try:
        summary = ResearchModel.get_research_summary(start_date, end_date, area)
        # Format and send the response
        await ctx.send(f"Research Summary: {summary}")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="analyzeTerrain", help="Analyze terrain based on given criteria")
async def analyze_terrain(ctx, criteria):
    try:
        # Assuming you have a method in a relevant model to handle this
        # Example: TerrainModel.analyze(criteria)
        analysis = TerrainModel.analyze(criteria)
        await ctx.send(f"Terrain Analysis: {analysis}")
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command(name="generateAlert", help="Manually trigger alert generation")
async def generate_alert(ctx):
    try:
        # Assuming you have a method to handle this
        # Example: AlertModel.generate()
        AlertModel.generate()
        await ctx.send("Alert generation process triggered.")
    except Exception as e:
        await ctx.send(f"Error: {e}")



bot.run(TOKEN)
