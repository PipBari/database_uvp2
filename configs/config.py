from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:1234@127.0.0.1:5432/reservation',
    echo=True
)
