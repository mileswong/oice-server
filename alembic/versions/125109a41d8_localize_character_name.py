"""Localize character name

Revision ID: 125109a41d8
Revises: 26025843ec3
Create Date: 2016-12-08 06:28:20.154351

"""

# revision identifiers, used by Alembic.
revision = '125109a41d8'
down_revision = '26025843ec3'
branch_labels = None
depends_on = None

import uuid
from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('character', 'name', new_column_name='name_en', existing_type=sa.Unicode(length=1024),
            existing_nullable=False)
    op.add_column('character', sa.Column('name_jp', sa.Unicode(length=1024), nullable=False))
    op.add_column('character', sa.Column('name_tw', sa.Unicode(length=1024), nullable=False))
    conn = op.get_bind()
    conn.execute("""
        UPDATE `character` SET name_jp = name_en;
        UPDATE `character` SET name_tw = name_en;""")
    op.drop_constraint('character_ibfk_1', 'character', type_='foreignkey')
    op.drop_index('key_UNIQUE', table_name='character')
    op.drop_index('library_id', table_name='character')
    op.alter_column('character', 'key', new_column_name='uuid',
            type_=sa.Unicode(length=128), existing_nullable=False)
    op.create_unique_constraint(None, 'character', ['uuid'])
    op.create_unique_constraint(None, 'character', ['library_id', 'uuid'])
    op.create_foreign_key('character_ibfk_1', 'character', 'library', ['library_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('character', 'name_en', new_column_name='name', existing_type=sa.Unicode(length=1024),
            existing_nullable=False)
    op.drop_column('character', 'name_tw')
    op.drop_column('character', 'name_jp')
    op.drop_constraint('character_ibfk_1', 'character', type_='foreignkey')
    op.drop_constraint('uuid', 'character', type_='unique')
    op.drop_constraint('library_id', 'character', type_='unique')
    op.alter_column('character', 'uuid', new_column_name='key',
            type_=sa.Unicode(length=128), existing_nullable=False)
    op.create_index('library_id', 'character', ['library_id', 'key'], unique=True)
    op.create_index('key_UNIQUE', 'character', ['key'], unique=True)
    op.create_foreign_key('character_ibfk_1', 'character', 'library', ['library_id'], ['id'])
    ### end Alembic commands ###