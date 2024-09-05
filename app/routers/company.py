from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from database import get_async_db_context, get_db_context
from models.company import CompanyViewModel, CompanyModel
from services import company as CompanyService
from services.auth import authorizer
from models.user import UserClaims
from services.exception import AccessDeniedError
from uuid import UUID

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.get("", status_code=status.HTTP_200_OK, response_model=list[CompanyViewModel])
async def get_all_company(
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer)):
    return CompanyService.get_companies(db)

@router.get("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyViewModel)
async def get_company_details(
    company_id: UUID,
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer)):
    return CompanyService.get_company_by_id(db, company_id)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=CompanyViewModel)
async def create_company(
    request: CompanyModel, 
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer)):
    if not user.is_admin:
        raise AccessDeniedError()
    return CompanyService.add_new_company(db, request)

@router.put("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyViewModel)
async def update_company(
    company_id: UUID,
    request: CompanyModel, 
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer)):
    if not user.is_admin:
        raise AccessDeniedError()
    return CompanyService.update_company(db, company_id, request)

@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(company_id: UUID, db: Session = Depends(get_db_context)):
    CompanyService.delete_company(db, company_id)
