"""empty message

Revision ID: 7240d2a4695b
Revises: 
Create Date: 2021-09-03 10:43:43.132902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7240d2a4695b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table_status',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('status_id')
    )
    op.create_table('user',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('profession', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('country',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=200), nullable=False),
    sa.Column('display_name', sa.String(length=200), nullable=False),
    sa.Column('timezone', sa.String(length=10), nullable=False),
    sa.Column('local_timezone', sa.String(length=10), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('country_id'),
    sa.UniqueConstraint('country')
    )
    op.create_table('crawl_frequency',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('cf_id', sa.Integer(), nullable=False),
    sa.Column('crawl_frequency', sa.String(length=100), nullable=False),
    sa.Column('display_name', sa.String(length=200), nullable=False),
    sa.Column('crawl_day', sa.String(length=10), nullable=False),
    sa.Column('crawl_time', sa.Time(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('cf_id'),
    sa.UniqueConstraint('crawl_frequency')
    )
    op.create_table('module',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('module_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('display_name', sa.String(length=200), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('module_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product_identifier',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('identifier_id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(length=200), nullable=False),
    sa.Column('display_name', sa.String(length=200), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('identifier_id'),
    sa.UniqueConstraint('identifier')
    )
    op.create_table('product_record_type',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('record_type_id', sa.Integer(), nullable=False),
    sa.Column('record_type', sa.String(length=200), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('record_type_id'),
    sa.UniqueConstraint('record_type')
    )
    op.create_table('product_tag',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('tag_name', sa.String(length=200), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('tag_id'),
    sa.UniqueConstraint('tag_name')
    )
    op.create_table('account',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.country_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('account_id')
    )
    op.create_table('account_module_mapping',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('mapping_id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('module_id', sa.Integer(), nullable=True),
    sa.Column('cf_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.account_id'], ),
    sa.ForeignKeyConstraint(['cf_id'], ['crawl_frequency.cf_id'], ),
    sa.ForeignKeyConstraint(['module_id'], ['module.module_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('mapping_id'),
    sa.UniqueConstraint('account_id', 'module_id', 'cf_id', name='account_module_crawl')
    )
    op.create_table('module_other_config',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('mapping_id', sa.Integer(), nullable=False),
    sa.Column('field', sa.String(length=100), nullable=False),
    sa.Column('field_value', sa.String(length=200), nullable=False),
    sa.Column('others', sa.JSON(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mapping_id'], ['account_module_mapping.mapping_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('mapping_id', 'field', 'field_value')
    )
    op.create_table('module_product_mapping',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('mapping_id', sa.Integer(), nullable=False),
    sa.Column('identifier_id', sa.Integer(), nullable=True),
    sa.Column('custom_tag_id', sa.Integer(), nullable=True),
    sa.Column('record_type_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=1000), nullable=False),
    sa.Column('image_url', sa.String(length=1000), nullable=False),
    sa.Column('level1_price', sa.Float(), nullable=True),
    sa.Column('level2_price', sa.Float(), nullable=True),
    sa.Column('level3_price', sa.Float(), nullable=True),
    sa.Column('zipcode', sa.JSON(), nullable=True),
    sa.Column('others', sa.JSON(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['custom_tag_id'], ['product_tag.tag_id'], ),
    sa.ForeignKeyConstraint(['identifier_id'], ['product_identifier.identifier_id'], ),
    sa.ForeignKeyConstraint(['mapping_id'], ['account_module_mapping.mapping_id'], ),
    sa.ForeignKeyConstraint(['record_type_id'], ['product_record_type.record_type_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('product_id', 'mapping_id')
    )
    op.create_table('module_source_mapping',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('mapping_id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=100), nullable=False),
    sa.Column('display_name', sa.String(length=100), nullable=False),
    sa.Column('source_type', sa.String(length=100), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.country_id'], ),
    sa.ForeignKeyConstraint(['mapping_id'], ['account_module_mapping.mapping_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('source_id', 'mapping_id'),
    sa.UniqueConstraint('mapping_id'),
    sa.UniqueConstraint('source')
    )
    op.create_table('module_attribute_mapping',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('mapping_id', sa.Integer(), nullable=False),
    sa.Column('attribute', sa.String(length=100), nullable=False),
    sa.Column('attribute_value', sa.String(length=200), nullable=False),
    sa.Column('manufacture', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=1000), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('others', sa.JSON(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mapping_id'], ['account_module_mapping.mapping_id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['module_source_mapping.source_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['table_status.status_id'], ),
    sa.PrimaryKeyConstraint('mapping_id', 'attribute', 'attribute_value')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('module_attribute_mapping')
    op.drop_table('module_source_mapping')
    op.drop_table('module_product_mapping')
    op.drop_table('module_other_config')
    op.drop_table('account_module_mapping')
    op.drop_table('account')
    op.drop_table('product_tag')
    op.drop_table('product_record_type')
    op.drop_table('product_identifier')
    op.drop_table('module')
    op.drop_table('crawl_frequency')
    op.drop_table('country')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_table('table_status')
    # ### end Alembic commands ###