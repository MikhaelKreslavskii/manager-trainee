// Initialization of DB
db = db.getSiblingDB('app_database');
db.createCollection("user");
db.createCollection("dialog");
db.createCollection("message");
db.createCollection("llm_model")

