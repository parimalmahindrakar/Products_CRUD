from extensions import db


class BaseModel:
    model = None

    @classmethod
    def create_record(cls, values, db=db):
        obj = cls.model(**values)
        db.session.add(obj)
        db.session.flush()
        return obj

    @classmethod
    def get_record_with_id(cls, model_id, db=db):
        return db.session.query(cls.model).filter(cls.model.id == model_id).first()

    @classmethod
    def update_record_with_id(cls, id, db=db, **kwargs):
        db.session.query(cls.model).filter(cls.model.id == id).update(kwargs)
        db.session.flush()

    @classmethod
    def get_all_records(cls, limit=100, db=db):
        query = db.query(cls.model).order_by(cls.model.id.desc())
        return query.all() if limit == 0 else query.limit(limit).all()

    @classmethod
    def get_paginated_records_with_filters(cls, page_number, page_size, query):
        return query.paginate(page=page_number, per_page=page_size)

    @classmethod
    def delete_record(cls, db, model_id):
        return db.session.query(cls.model).filter(cls.model.id == model_id).delete()
