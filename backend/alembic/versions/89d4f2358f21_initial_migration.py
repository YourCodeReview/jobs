"""Initial migration

Revision ID: 89d4f2358f21
Revises: ed8b6279e603
Create Date: 2024-01-15 18:20:25.538292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89d4f2358f21'
down_revision: Union[str, None] = 'ed8b6279e603'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
