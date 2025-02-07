// Initialization of DB
db = db.getSiblingDB('app_database');
db.createCollection("Dialog");
db.createCollection("User");
db.createCollection("Message");
db.createCollection("Scenario");
db.createCollection("Client")
