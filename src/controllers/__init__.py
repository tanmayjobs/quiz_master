"""
The controller package contains all the controllers for the project.
The controllers are grouped based on their functionality or resource.
Each controller file contains one controller class.
Controller classes can be decorated by validate_token_details, for usage check rbac module in utils.

Each controller class implements two methods __init__ and __call__,
    1.__init__:
        Takes query, path and request body as parameter if and only if required and extract necessary details.
    2.__call__:
        Here the main functionality is handled also handling the expected custom exceptions.
        Will create the response here.

NOTE: If you want to understand the reason of choosing __init__ and __call__ only then read forward.
    1.__init__:
        Takes query, path and request body as parameter if and only if required.
        FUTURE SCOPE:
            Takes all the parameters and request body even if not required and then extract necessary things.
            If any further validations are required on fields then that can be done here.
    2.__call__:
        This makes the controller object callable.
        YES, I KNOW WE CAN CREATE A DIFFERENT FUNCTION SUGGESTED(run, execute, work).
        BUT I WANT TO KEEP IT THIS WAY IT'S MORE READABLE IN ROUTERS AFTER YOU GET THE HAND OF IT.
        ALSO, IT WILL BE MUCH BETTER IN CASE WE USE DEPENDENCY IN FUTURE ON ROUTERS TOGETHER WITH FUTURE SCOPE OF __init__.

"""
