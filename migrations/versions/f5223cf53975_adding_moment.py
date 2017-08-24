"""Adding moment

Revision ID: f5223cf53975
Revises:
Create Date: 2017-08-24 15:58:08.715380

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f5223cf53975'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moments',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_on', sa.DateTime(), nullable=True),
                    sa.Column('updated_on', sa.DateTime(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('event_date', sa.Date(), nullable=False),
                    sa.Column('details', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moments')
    # ### end Alembic commands ###