from ..database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False)
    last_name = db.Column(db.String(100), unique=False)
    orders = db.relationship('Order', backref='user')

    @property
    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "orders": [order.to_json for order in self.orders]
        }