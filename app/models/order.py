from ..database import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(100))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    items = db.relationship('OrderItem', back_populates='order')

    @property
    def to_json(self):
        return {
            "id": self.id,
            "order_date": self.order_date,
            "items": [item.to_json for item in self.items]
        }
    