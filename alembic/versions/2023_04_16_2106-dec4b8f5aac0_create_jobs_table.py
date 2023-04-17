"""create jobs table

Revision ID: dec4b8f5aac0
Revises: c8911f124d4b
Create Date: 2023-04-16 21:06:15.566877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dec4b8f5aac0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
    CREATE TABLE jobs (
        AREA varchar(255),
        AREA_TITLE varchar(255),
        AREA_TYPE varchar(255),
        PRIM_STATE varchar(255),
        NAICS varchar(255),
        NAICS_TITLE varchar(255),
        I_GROUP varchar(255),
        OWN_CODE varchar(255),
        OCC_CODE varchar(255),
        OCC_TITLE varchar(255),
        O_GROUP varchar(255),
        TOT_EMP int,
        EMP_PRSE decimal,
        JOBS_1000 varchar(255),
        LOC_QUOTIENT varchar(255),
        PCT_TOTAL varchar(255),
        PCT_RPT varchar(255),
        H_MEAN decimal,
        A_MEAN decimal,
        MEAN_PRSE decimal,
        H_PCT10 decimal,
        H_PCT25 decimal,
        H_MEDIAN decimal,
        H_PCT75 decimal,
        H_PCT90 decimal,
        A_PCT10 decimal,
        A_PCT25 decimal,
        A_MEDIAN decimal,
        A_PCT75 decimal,
        A_PCT90 decimal,
        ANNUAL boolean,
        HOURLY boolean
        );
    
    ''')

    


def downgrade():
    op.drop_table('jobs')
