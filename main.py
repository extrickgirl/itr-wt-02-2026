from datetime import datetime

from blog.person.name import Name
from blog.person.person import Person
from blog.post import Post

print(
    Post(
        author=Person(
            name=Name(first_name="Иван", last_name="Иванов"), registered_on=datetime.now()
        ),
        text="некоторый текст",
    )
)
