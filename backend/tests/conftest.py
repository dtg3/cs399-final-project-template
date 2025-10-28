
import pytest
from app import create_app, db 
from app.models.database import create_task 

TEST_DATABASE_URI = 'sqlite:///:memory:' 


@pytest.fixture
def app():
    if hasattr(db, 'app'):
        del db.app 
        
    app = create_app(testing=True)

    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI, 
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    })

    db.init_app(app)

    with app.app_context():
        db.drop_all() 
        db.create_all()
        
        create_task(title='Setup pytest', completed=True)
        create_task(title='Write feature tests', completed=False)
        
    yield app

    with app.app_context():
        db.session.remove()
        
    if hasattr(db, 'app'):
        del db.app 


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db_conn(app):
    with app.app_context():
        yield db.session 
        db.session.rollback()
        db.session.remove()
