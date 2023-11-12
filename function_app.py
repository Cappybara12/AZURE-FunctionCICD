import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    endpoint = "https://portfoliodbmlsa.table.cosmos.azure.com:443/"
    #need to find key
    key = ""
    database_name = "portfoliodbmlsa"

    container_name = "table1"

    # Create Cosmos DB client
    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    # Retrieve and increment the visitor count
    item = container.read_item('uniqueCounter', 'uniqueCounter')
    count = item['count']

    # Update the count in the database
    container.upsert_item({'id': 'uniqueCounter', 'count': count + 1})

    # Respond with the updated count
    return func.HttpResponse(f"Visitor Count: {count + 1}")
