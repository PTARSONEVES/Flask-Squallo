from itsdangerous import URLSafeTimedSerializer
from app import CREDENCIAIS



def gera_token(email):
    serializer = URLSafeTimedSerializer(CREDENCIAIS.get('secret'))
    return serializer.dumps(email,salt=CREDENCIAIS.get('secsalt'))

def confirma_token(token,expiration=3600):
    serializer = URLSafeTimedSerializer(CREDENCIAIS.get('secret'))
    try:
        email = serializer.loads(
            token,
            salt=CREDENCIAIS.get('secsalt'),
            max_age=expiration
        )
    except:
        return False
    return email