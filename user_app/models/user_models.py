from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime, Time, Float, JSON, Text)
from sqlalchemy import UniqueConstraint

BaseModel = declarative_base()


from datetime import datetime
from sqlalchemy.orm import relationship


class AuditBase:
    created_on = Column(DateTime(), default=datetime.utcnow, nullable=False)
    last_updated = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.now, nullable=False)



class User(AuditBase, BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, nullable=False, primary_key=True, index=True)
    display_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String(100), nullable=False)
    profession = Column(String(50), nullable=False)


class TableStatus(AuditBase, BaseModel):
    __tablename__ = 'table_status'

    status_id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)


class Module(AuditBase, BaseModel):
    __tablename__ = 'module'

    module_id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    display_name = Column(String(200), nullable=False)

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    accounts = relationship("AccountModuleMapping", back_populates="module")


class Country(AuditBase, BaseModel):
    __tablename__ = 'country'

    country_id = Column(Integer(), primary_key=True)
    country = Column(String(200), nullable=False, unique=True)
    display_name = Column(String(200), nullable=False)
    timezone = Column(String(10), nullable=False)
    local_timezone = Column(String(10), nullable=False)

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    accounts = relationship("Account", back_populates="country")
    sources = relationship("ModuleSourceMapping", back_populates="country")


class Account(AuditBase, BaseModel):
    __tablename__ = 'account'

    account_id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)

    country_id = Column(Integer(), ForeignKey('country.country_id'))
    country = relationship("Country", back_populates="accounts")

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    modules = relationship("AccountModuleMapping", back_populates="account")


class CrawlFrequency(AuditBase, BaseModel):
    __tablename__ = 'crawl_frequency'

    cf_id = Column(Integer(), primary_key=True)
    crawl_frequency = Column(String(100), nullable=False, unique=True)
    display_name = Column(String(200), nullable=False)

    crawl_day = Column(String(10), nullable=False)
    crawl_time = Column(Time(), nullable=False)

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    account_modules = relationship("AccountModuleMapping", back_populates='crawl_frequency')


class AccountModuleMapping(AuditBase, BaseModel):
    __tablename__ = 'account_module_mapping'

    mapping_id = Column(Integer(), primary_key=True)

    account_id = Column(Integer(), ForeignKey('account.account_id'))
    account = relationship("Account", back_populates="account_modules")

    module_id = Column(Integer(), ForeignKey('module.module_id'))
    module = relationship("Module", back_populates="accounts")

    cf_id = Column(Integer(), ForeignKey('crawl_frequency.cf_id'))
    crawl_frequency = relationship("CrawlFrequency", back_populates="account_modules")

    start_time = Column(DateTime(), nullable=False)
    end_time = Column(DateTime(), nullable=False)

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    module_products = relationship('ModuleProductMapping', back_populates='mapping')
    module_sources = relationship('ModuleSourceMapping', back_populates='mapping')
    module_attributes = relationship('ModuleAttributeMapping', back_populates='mapping')
    other_configs = relationship('ModuleOtherConfig', back_populates='mapping')

    __table_args__ = (
        UniqueConstraint('account_id', 'module_id', 'cf_id', name='account_module_crawl'),)


class ProductTag(AuditBase, BaseModel):
    __tablename__ = 'product_tag'

    tag_id = Column(Integer(), primary_key=True)
    tag_name = Column(String(200), nullable=False, unique=True)

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    module_products = relationship('ModuleProductMapping', back_populates='custom_tag')


class ProductRecordType(AuditBase, BaseModel):
    __tablename__ = 'product_record_type'

    record_type_id = Column(Integer(), primary_key=True)
    record_type = Column(String(200), nullable=False, unique=True)

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    module_products = relationship('ModuleProductMapping', back_populates='record_type')


class ProductIdentifier(AuditBase, BaseModel):
    __tablename__ = 'product_identifier'

    identifier_id = Column(Integer(), primary_key=True)
    identifier = Column(String(200), nullable=False, unique=True)
    display_name = Column(String(200), nullable=False)

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")

    module_products = relationship('ModuleProductMapping', back_populates='identifier')


class ModuleProductMapping(AuditBase, BaseModel):
    __tablename__ = 'module_product_mapping'

    product_id = Column(Integer(), primary_key=True)

    mapping_id = Column(Integer(), ForeignKey('account_module_mapping.mapping_id'), primary_key=True)
    mapping = relationship("AccountModuleMapping", back_populates='module_products')

    identifier_id = Column(Integer(), ForeignKey('product_identifier.identifier_id'))
    identifier = relationship("ProductIdentifier", back_populates='module_products')

    custom_tag_id = Column(Integer(), ForeignKey('product_tag.tag_id'))
    custom_tag = relationship("ProductTag", back_populates='module_products')

    record_type_id = Column(Integer(), ForeignKey('product_record_type.record_type_id'))
    record_type = relationship("ProductRecordType", back_populates='module_products')

    title = Column(String(100), nullable=False)
    url = Column(String(1000), nullable=False)
    image_url = Column(String(1000), nullable=False)

    level1_price = Column(Float())
    level2_price = Column(Float())
    level3_price = Column(Float())

    zipcode = Column(JSON())
    others = Column(JSON())

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")


class ModuleSourceMapping(AuditBase, BaseModel):
    __tablename__ = 'module_source_mapping'

    source_id = Column(Integer(), primary_key=True)
    
    mapping_id = Column(Integer(), ForeignKey('account_module_mapping.mapping_id'), primary_key=True, unique=True)
    mapping = relationship("AccountModuleMapping", back_populates='module_sources')

    source = Column(String(100), nullable=False, unique=True)
    display_name = Column(String(100), nullable=False)
    source_type = Column(String(100), nullable=False)

    country_id = Column(Integer(), ForeignKey('country.country_id'))
    country = relationship("Country", back_populates="sources")

    module_sources = relationship("ModuleAttributeMapping", back_populates="source")

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")


class ModuleAttributeMapping(AuditBase, BaseModel):
    __tablename__ = 'module_attribute_mapping'

    mapping_id = Column(Integer(), ForeignKey('account_module_mapping.mapping_id'), primary_key=True)
    mapping = relationship("AccountModuleMapping", back_populates='module_attributes')

    attribute = Column(String(100), nullable=False, primary_key=True)
    attribute_value = Column(String(200), nullable=False, primary_key=True)

    manufacture = Column(String(100), nullable=False)

    url = Column(String(1000), nullable=False)

    source_id = Column(Integer(), ForeignKey('module_source_mapping.source_id'))
    source = relationship("ModuleSourceMapping", back_populates='module_sources')

    others = Column(JSON())

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")


class ModuleOtherConfig(AuditBase, BaseModel):
    __tablename__ = 'module_other_config'

    mapping_id = Column(Integer(), ForeignKey('account_module_mapping.mapping_id', ondelete='CASCADE'), primary_key=True)
    mapping = relationship("AccountModuleMapping", back_populates='other_configs')

    field = Column(String(100), nullable=False, primary_key=True)
    field_value = Column(String(200), nullable=False, primary_key=True)

    others = Column(JSON())

    status_id = Column(Integer(), ForeignKey('table_status.status_id'))
    status = relationship("TableStatus")
