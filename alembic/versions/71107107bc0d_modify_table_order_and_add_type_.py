"""modify table order and add type & material enum column

Revision ID: 71107107bc0d
Revises: d24b6d4e0188
Create Date: 2025-06-23 21:59:43.505907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '71107107bc0d'
down_revision: Union[str, Sequence[str], None] = 'd24b6d4e0188'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'type',
               existing_type=mysql.ENUM('sepatu', 'tas', 'topi'),
               type_=sa.Enum('SH', 'TS', 'TP', name='typeenum'),
               existing_nullable=False)
    op.alter_column('order', 'material',
               existing_type=mysql.ENUM('kulit', 'suede', 'kanvas'),
               type_=sa.Enum('kl', 'sd', 'kv', name='materialenum'),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'material',
               existing_type=sa.Enum('kl', 'sd', 'kv', name='materialenum'),
               type_=mysql.ENUM('kulit', 'suede', 'kanvas'),
               existing_nullable=False)
    op.alter_column('order', 'type',
               existing_type=sa.Enum('SH', 'TS', 'TP', name='typeenum'),
               type_=mysql.ENUM('sepatu', 'tas', 'topi'),
               existing_nullable=False)
    # ### end Alembic commands ###
