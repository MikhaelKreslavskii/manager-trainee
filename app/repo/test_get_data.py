from pymongo import MongoClient

if __name__ == "__main__":
    # Connection to the BD
    client = MongoClient("mongodb://localhost:27017")

    # Get list of all DBs
    db_list = client.list_database_names()
    print("Список баз данных: ", db_list)

    # Switch to "app_database"
    db = client["app_database"]

    # Get collections
    collections = db.list_collection_names()
    print(f"List of collections in the DB: {collections}")

    # Data in Conversations
    conversation_collection = db["conversation"]
    all_conversations = conversation_collection.find()
    for conv in all_conversations:
        print(conv)
