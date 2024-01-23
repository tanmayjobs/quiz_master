from flask_jwt_extended import create_access_token


def generate_token(user):
    return create_access_token(identity=user.user_id, additional_claims={"role": user.role})
