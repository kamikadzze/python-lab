from .base import BaseTestCase
from app.auth.models import User
from app.todo.models import Todo                                                     


class ModelTests(BaseTestCase):
    
    def test_user_model(self):
        """
        GIVEN  a user model
        WHEN a new user is created 
        THEN check the email and password fields are defined correctly
        """
        
        user = User(username = "test1", email = "test1@gmail.com", password = "test1test1")
        assert user.username == 'test1'
        assert user.email == 'test1@gmail.com'
        assert user.password == 'test1test1'
        
        
    def test_todo_model(self):
        """
        GIVEN  a todo model
        WHEN a new todo is created 
        THEN check the title and description fields are defined correctly
        """
        
        todo = Todo(todo_item = "todo title", description = "this is todo description")
        assert todo.todo_item == "todo title"
        assert todo.description == "this is todo description"