from .models import Todo
from faker import Faker


def run():
    fake=Faker()
    for todo in range(200):
        Todo.objects.create(
            title = fake.sentence(),
            description = fake.text(),
            priority=fake.random_int(min=1, max=3),
            is_done = fake.boolean()
        )
    print('Finished')