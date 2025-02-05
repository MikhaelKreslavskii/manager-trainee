// Initialization of DB
db = db.getSiblingDB('app_database');
db.createCollection("user");
db.createCollection("conversation");
db.createCollection("message");
db.createCollection("llm_model")

