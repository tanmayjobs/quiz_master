class ErrorExamples:
    @staticmethod
    def error404(resource):
        return {"code": 404, "error": "Not Found", "message": f"{resource} not found!"}

    @staticmethod
    def error409(resource):
        return {
            "code": 409,
            "error": "Conflict",
            "message": f"conflict arise for {resource}",
        }

    @staticmethod
    def error401():
        return {"code": 401, "error": "Unauthorize", "message": "invalid credentials"}
