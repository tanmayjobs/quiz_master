"""
The services package contains all the business login for this project.
Each service class contains one attribute database_access which is nothing but database access object.
database_access is used to perform the read and write functions for the service.

If a service do not perform any operation on DB only and only then don't use database_access,
in all the other cases use it. Not saying this just for fun but because of Future Scopes of working.
"""