from pydantic import BaseModel, Field
from entities.company import CompanyMode
from datetime import datetime
from uuid import UUID

class CompanyModel(BaseModel):
    name: str = Field(min_length=2)
    description: str = Field(min_length=10)
    mode: CompanyMode = Field(default=CompanyMode.MODE_1)


class CompanyViewModel(BaseModel):
    id: UUID
    name: str
    description: str
    mode: CompanyMode
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True