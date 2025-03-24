"""remove current_clients

Revision ID: 1f557db4f100
Revises: 8dd30c5fd47d
Create Date: 2025-01-31 19:08:35.312152

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1f557db4f100"
down_revision: Union[str, None] = "8dd30c5fd47d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("servers", schema=None) as batch_op:
        batch_op.drop_column("current_clients")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("servers", schema=None) as batch_op:
        batch_op.add_column(sa.Column("current_clients", sa.INTEGER(), nullable=False))
    # ### end Alembic commands ###
