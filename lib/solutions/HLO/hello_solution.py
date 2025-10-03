from pydantic import TypeAdapter, constr, ConfigDict

Name = constr(min_length=0)

adapter = TypeAdapter(Name, config=ConfigDict(strict=True))


class HelloSolution:
    def hello(self, friend_name: str) -> str:
        adapter.validate_python(friend_name)
        return f"Hello, {friend_name}!"

