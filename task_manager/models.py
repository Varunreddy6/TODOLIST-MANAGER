from task_manager import db
from task_manager import datetime,date


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    completed = db.Column(db.Integer, default=0)
   # time_stamp = db.Column(db.DateTime, nullable=False)
  # timeelapsed=db.Column(db.DtaeTime)
    days=db.Column(db.Integer, default=0)
    status=db.Column(db.String(500), default="pending")
    deadline=db.Column(db.Date ,default=date.today())
    hours=db.Column(db.Integer, default=0)
    minutes=db.Column(db.Integer, default=0)
    seconds=db.Column(db.Integer, default=0)
    time_stamp=db.Column(db.DateTime,default=datetime.utcnow)
  #  timesof=db.Column(db.String(500),nullable=False)
    def __repr__(self):
        return '<Task {}>'.format(self.id)
