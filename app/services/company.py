from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from entities.company import Company
from sqlalchemy.orm import Session
from models import CompanyModel
from services import utils, exception
from uuid import UUID

def get_companies(db: Session) -> list[Company]:
    result = db.scalars(select(Company).order_by(Company.created_at))
    
    return result.all()

def get_company_by_id(db: Session, company_id: UUID) -> Company:
    result = db.scalars(select(Company).filter(Company.id == company_id))
    
    return result.first()

def add_new_company(db: Session, data: CompanyModel) -> Company:
    company = Company(**data.model_dump())

    company.created_at = utils.get_current_utc_time()
    company.updated_at = utils.get_current_utc_time()
    
    db.add(company)
    db.commit()
    db.refresh(company)
    
    return company

def update_company(db: Session, company_id: UUID, data: CompanyModel) -> Company:
    company = get_company_by_id(db, company_id)

    if company is None:
        raise exception.ResourceNotFoundError()
    
    company.name = data.name
    company.description = data.description
    company.mode = data.mode
    company.updated_at = utils.get_current_utc_time()
    
    db.commit()
    db.refresh(company)
    
    return company

def delete_company(db: Session, id: UUID) -> None:
    company = get_company_by_id(db, id)

    if company is None:
        raise exception.ResourceNotFoundError()
    
    db.delete(company)
    db.commit()
