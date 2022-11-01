from tortoise import fields
from tortoise.models import Model


class QGuilds(Model):
    id = fields.BigIntField(pk=True)
    date_added = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "guilds"

    def __str__(self):
        return self.name


class Question(Model):
    id = fields.BigIntField(pk=True)
    guild_id = fields.BigIntField()
    author_id = fields.BigIntField()
    name = fields.CharField(max_length=255)
    question = fields.TextField()
    date_added = fields.DatetimeField(auto_now_add=True)
    author_name = fields.CharField(max_length=255)

    class Meta:
        table = "questions"

    def __str__(self):
        return self.name
