"""change role_id to nullable true

Revision ID: 9c25ecd18809
Revises: 28ae61e47451
Create Date: 2023-10-20 14:17:01.425014

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '9c25ecd18809'
down_revision: Union[str, None] = '28ae61e47451'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
