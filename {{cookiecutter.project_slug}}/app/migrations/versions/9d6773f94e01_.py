"""Initial

Revision ID: 9d6773f94e01
Revises:
Create Date: {% now 'local', '%Y-%m-%d %H:%M:%S' %}
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9d6773f94e01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "item",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
    )

    op.create_table(
        "sub_item",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("item_id", sa.Integer(), sa.ForeignKey("item.id", ondelete="CASCADE"), nullable=False),
    )


def downgrade():
    op.drop_table("sub_item")
    op.drop_table("item")
