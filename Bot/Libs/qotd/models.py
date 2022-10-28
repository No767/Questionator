from tortoise import fields
from tortoise.models import Model


class QGuilds(Model):
    id = fields.BigIntField(pk=True)
    join_date = fields.DatetimeField(null=True, auto_now_add=True)

    class Meta:
        table = "guilds"

    def __str__(self):
        return self.name
