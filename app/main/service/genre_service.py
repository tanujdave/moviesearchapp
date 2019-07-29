from app.main import db
from app.main.model.genre import Genre


def save_new_genre(data):
    genre = Genre.query.filter_by(name=data['name']).first()
    if not genre:
        new_genre = Genre(            
            name=data['name']
        )
        save_changes(new_genre)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Genre already exists.',
        }
        return response_object, 409


def get_all_genre():
    return Genre.query.all()


def get_a_genre(id):
    return Genre.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()