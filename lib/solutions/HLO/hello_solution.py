from pydantic import TypeAdapter, constr

Name = constr()

adapter = TypeAdapter(str)

class HelloSolution:
    def hello(self, friend_name: str) -> str:
        adapter.validate_python(friend_name)
        return f'Hello, {friend_name}!'



