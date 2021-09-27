
from datetime import datetime
from sqlalchemy import (Column, DateTime)

from user_app.models.user_models import BaseModel


class AuditBase(BaseModel):
    created_on = Column(DateTime(), default=datetime.utcnow, nullable=False)
    last_updated = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.now, nullable=False)