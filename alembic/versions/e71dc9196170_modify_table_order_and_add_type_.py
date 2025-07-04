"""modify table order and add type & material enum column

Revision ID: e71dc9196170
Revises: 97ed3f0c3685
Create Date: 2025-06-23 22:10:30.381730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e71dc9196170'
down_revision: Union[str, Sequence[str], None] = '97ed3f0c3685'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.DECIMAL(precision=18, scale=2), nullable=True),
    sa.Column('qty', sa.String(length=50), nullable=True),
    sa.Column('type', sa.Enum('SH', 'TS', 'TP', name='typeenum'), nullable=False),
    sa.Column('material', sa.Enum('KL', 'SD', 'KV', name='materialenum'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_id')
    )
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_table('order')
    # ### end Alembic commands ###
