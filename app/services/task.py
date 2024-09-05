from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from entities.task import Task

def get_tasks(db: Session) -> list[Task]:
    result = db.scalars(select(Task)
                        .order_by(Task.created_at)
                        .options(joinedload(Task.assignee, innerjoin=True))
                        )
    
    return result.all()
