"""change role_id to nullablel true

Revision ID: 28ae61e47451
Revises: 6f6a40a34103
Create Date: 2023-10-20 14:02:31.058058

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '28ae61e47451'
down_revision: Union[str, None] = '6f6a40a34103'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###
