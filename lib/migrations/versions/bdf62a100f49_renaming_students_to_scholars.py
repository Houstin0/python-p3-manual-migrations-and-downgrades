"""Renaming students to scholars

Revision ID: bdf62a100f49
Revises: 791279dd0760
Create Date: 2023-09-03 07:37:53.016294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdf62a100f49'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')
