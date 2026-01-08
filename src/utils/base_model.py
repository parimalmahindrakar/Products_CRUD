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
        return db.query(cls.model).filter(cls.model.id == model_id).first()

    @classmethod
    def get_all_records(cls, limit=100, db=db):
        query = db.query(cls.model).order_by(cls.model.id.desc())
        return query.all() if limit == 0 else query.limit(limit).all()
