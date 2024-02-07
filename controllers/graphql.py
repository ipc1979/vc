from flask import Flask
from flask_graphql import GraphQLView
from gql.resolvers import schema

def register_graphql_controllers(app: Flask) -> None:
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # Habilita la interfaz GraphiQL
        )
    )