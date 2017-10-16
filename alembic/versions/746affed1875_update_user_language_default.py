"""Update user language default

Revision ID: 746affed1875
Revises: 4fe6c9548cfd
Create Date: 2017-08-03 06:52:21.571810

"""

# revision identifiers, used by Alembic.
revision = '746affed1875'
down_revision = '4fe6c9548cfd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'language', type_=sa.Unicode(7), existing_nullable=True)

    conn = op.get_bind()
    conn.execute("""
        UPDATE `user`
        SET `language` = NULL
    """)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    conn.execute("""
        UPDATE `user`
        SET `language` = 'zh_HK'
    """)

    op.alter_column('user', 'language', type_=sa.Unicode(5), existing_server_default="zh_HK", existing_nullable=False)
    # ### end Alembic commands ###