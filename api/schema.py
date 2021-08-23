from graphene import ObjectType, String, Schema, Field, List
import json

class User(ObjectType):
    name = String()
    repos = List(String)
    
class Query(ObjectType):
    user = Field(User)
    repos = String()

    def resolve_user(root, info):
        with open("api/data.json", "r") as f:
            data = json.load(f) 
            
        return User(name = data["user"], repos = data["repos"])

  
schema = Schema(query=Query)