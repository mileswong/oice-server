"""Add story tag

Revision ID: 0d5da074e3dd
Revises: b63ea28eb5fe
Create Date: 2018-01-08 04:47:33.543201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d5da074e3dd'
down_revision = 'b63ea28eb5fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'story_tag',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(length=128), nullable=False),
        sa.Column('order', sa.Integer(), nullable=False),
        sa.Column('is_hidden', sa.Boolean(), server_default=sa.text('false'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_story_tag_is_hidden'), 'story_tag', ['is_hidden'], unique=False)
    op.create_index(op.f('ix_story_tag_name'), 'story_tag', ['name'], unique=True)

    op.create_table(
        'story_tag_localization',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=False),
        sa.Column('language', sa.Unicode(length=5), server_default='zh-HK', nullable=False),
        sa.Column('name', sa.Unicode(length=128), nullable=False),
        sa.ForeignKeyConstraint(['tag_id'], ['story_tag.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('story_tag_localization_story_tag_language_idx', 'story_tag_localization', ['tag_id', 'language'], unique=True)

    op.create_table(
        'story_tagging',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('story_id', sa.Integer(), nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['story_id'], ['story.id'], ),
        sa.ForeignKeyConstraint(['tag_id'], ['story_tag.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('story_id', 'tag_id', name='story_tagging_unique')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('story_tagging')
    op.drop_index('story_tag_localization_story_tag_language_idx', table_name='story_tag_localization')
    op.drop_table('story_tag_localization')
    op.drop_index(op.f('ix_story_tag_name'), table_name='story_tag')
    op.drop_index(op.f('ix_story_tag_is_hidden'), table_name='story_tag')
    op.drop_table('story_tag')
    # ### end Alembic commands ###
