from textwrap import dedent

TITLE = "LMOS user management"

DESCRIPTION = dedent("""
    # LMOS user management API

    This API provides endpoints for managing users in the LMOS system.
    It allows you to create, retrieve, update, and delete user records.

    ## Authentication

    All endpoints require authentication using a valid API key.
    Include the API key in the `Authorization` header as follows:
    ```
        Authorization: Bearer <your_api_key>
    ```
             
""")
