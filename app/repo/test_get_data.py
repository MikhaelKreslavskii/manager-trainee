# from pymongo import MongoClient
# from dotenv import load_dotenv
# import os
#
# # взять:\
# #     Motor (асихронная для Монго)
# #     ODM -> bini
# # Получаем переменные из .env
# load_dotenv()
#
# DB_USER = os.getenv("MONGODB_USERNAME")
# DB_PASSWORD = os.getenv("MONGODB_PASSWORD")
# DB_PORT = os.getenv("DB_PORT")
# DB_URL = os.getenv("DB_URL")
#
# if __name__ == "__main__":
#     # Connection to the BD
#     client = MongoClient(DB_URL.format(DB_USER, DB_PASSWORD, DB_PORT))
#
#     # Get list of all DBs
#     db_list = client.list_database_names()
#     print("Список баз данных: ", db_list)
#
#     # Switch to "app_database"
#     db = client["app_database"]
#
#     # Get collections
#     collections = db.list_collection_names()
#     print(f"List of collections in the DB: {collections}")
#
#     # Data in Conversations
#     documents = [
#             {
#                 "id": "dialog_001",
#                 "user_id": "user_123",
#                 "model_id": "model_alpha",
#                 "completionOptions": {
#                     "temperature": 0.7,
#                     "max_tokens": 100,
#                     "stream": True
#                 },
#                 "created_at": "2023-05-10T12:34:56Z",
#                 "updated_at": "2023-05-10T13:00:00Z",
#                 "messages": {
#                     "role": "assistant",
#                     "content": "Hello! How can I help you?",
#                     "verified": True
#                 },
#                 "evaluation": "positive"
#             },
#             {
#                 "id": "dialog_002",
#                 "user_id": "user_456",
#                 "model_id": "model_beta",
#                 "completionOptions": {
#                     "temperature": 0.9,
#                     "max_tokens": 50,
#                     "stream": False
#                 },
#                 "created_at": "2023-06-15T08:30:00Z",
#                 "updated_at": "2023-06-15T08:45:00Z",
#                 "messages": {
#                     "question": "Where can I find a good restaurant?",
#                     "assistant_replied": False,
#                     "priority": 1
#                 },
#                 "evaluation": "neutral"
#             },
#             {
#                 "id": "dialog_003",
#                 "user_id": "user_999",
#                 "model_id": "model_gamma",
#                 "completionOptions": {
#                     "temperature": 0.0,
#                     "max_tokens": 200,
#                     "stream": False
#                 },
#                 "created_at": "2023-07-01T11:20:00Z",
#                 "updated_at": "2023-07-01T11:50:00Z",
#                 "messages": {
#                     "content": "Just testing different fields in messages",
#                     "is_test": True,
#                     "score": 5
#                 },
#                 "evaluation": "negative"
#             }]
#
#     conversation_collection = db["conversation"]
#     #
#     result = conversation_collection.insert_many(documents)
#
#     all_conversations = conversation_collection.find()
#     for conv in all_conversations:
#         print(conv)
