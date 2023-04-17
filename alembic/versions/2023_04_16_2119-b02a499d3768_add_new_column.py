"""ADD new column

Revision ID: b02a499d3768
Revises: dec4b8f5aac0
Create Date: 2023-04-16 21:19:48.954273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b02a499d3768'
down_revision = 'dec4b8f5aac0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('''
    ALTER TABLE jobs
    ADD Description text;
    ''')


def downgrade() -> None:
    op.execute('''
    ALTER TABLE jobs
    DROP COLUMN Description;
    ''')
