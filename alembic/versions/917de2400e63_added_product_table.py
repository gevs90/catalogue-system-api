"""Added product table

Revision ID: 917de2400e63
Revises: de5790c837cb
Create Date: 2023-09-23 22:22:28.666158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '917de2400e63'
down_revision: Union[str, None] = 'de5790c837cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("products",
                    sa.Column('id', sa.BigInteger(),
                              autoincrement=True, primary_key=True),
                    sa.Column('sku', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('price', sa.Float()),
                    sa.Column('brand', sa.String(), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table("products")
