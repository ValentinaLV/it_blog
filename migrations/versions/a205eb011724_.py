"""empty message

Revision ID: a205eb011724
Revises: 
Create Date: 2020-01-08 15:16:29.250394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a205eb011724'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_us')
    op.drop_index('user_usernameint_uindex', table_name='user')
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('user_usernameint_uindex', 'user', ['username'], unique=True)
    op.create_table('contact_us',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('telephone', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('subject', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='contact_us_pkey')
    )
    # ### end Alembic commands ###
