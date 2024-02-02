class LogText:
    STARTING_SYSTEM = "starting the system..."
    SYSTEM_ERROR = "Some unknown error occurred. Please contact the administrator!"
    EXITING_SYSTEM = "exiting the system"
    LOADING_TOKEN = "loading invalid tokens from database"
    SAVING_TOKEN = "saving invalid tokens to database"
    INVALID_CREDENTIALS = "someone attempted to log in with invalid credentials."
    BLOCKED_TOKEN = "someone used blocked token."
    NOT_ENOUGH_PERMISSIONS = "someone tried to access {} without enough permissions."

    def __getattr__(self, item: str):
        return item.upper()
