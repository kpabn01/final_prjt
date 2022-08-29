"""empty message

Revision ID: c5a2a98c45ef
Revises: 7abc7f614086
Create Date: 2022-08-30 00:27:15.435114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5a2a98c45ef'
down_revision = '7abc7f614086'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Show_venue_id_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_venue_id_fkey', 'Show', 'Venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###
