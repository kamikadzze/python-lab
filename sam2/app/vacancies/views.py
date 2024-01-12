from flask import jsonify, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from config import ACCESS_EXPIRES
from ..extensions import jwt_redis_blocklist, jwt_manager
from .models import Vacancy
from . import vacancies_api_bp
from .. import db

@vacancies_api_bp.route('/vacancies', methods=['GET'])
def get_vacancies():
    vacancies = Vacancy.query.all()
    return jsonify([{
        'id': vacancy.id,
        'title': vacancy.title,
        'description': vacancy.description,
        'qualification_level': vacancy.qualification_level
    } for vacancy in vacancies]), 200

@vacancies_api_bp.route('/vacancies/<int:vacancy_id>', methods=['GET'])
def get_vacancy(vacancy_id):
    vacancy = Vacancy.query.get_or_404(vacancy_id)
    return jsonify({
        'id': vacancy.id,
        'title': vacancy.title,
        'description': vacancy.description,
        'qualification_level': vacancy.qualification_level
    }), 200

@vacancies_api_bp.route('/vacancies', methods=['POST'])
@jwt_required()
def create_vacancy():
    data = request.get_json()
    vacancy = Vacancy(title=data['title'], description=data['description'], qualification_level=data['qualification_level'])
    db.session.add(vacancy)
    db.session.commit()
    return jsonify({'message': 'Vacancy created successfully!'}), 201

@vacancies_api_bp.route('/vacancies/<int:vacancy_id>', methods=['PUT'])
@jwt_required()
def update_vacancy(vacancy_id):
    vacancy = Vacancy.query.get_or_404(vacancy_id)
    data = request.get_json()
    vacancy.title = data['title']
    vacancy.description = data['description']
    vacancy.qualification_level = data['qualification_level']
    db.session.commit()
    return jsonify({'message': 'Vacancy updated successfully!'}), 200

@vacancies_api_bp.route('/vacancies/<int:vacancy_id>', methods=['DELETE'])
@jwt_required()
def delete_vacancy(vacancy_id):
    vacancy = Vacancy.query.get_or_404(vacancy_id)
    db.session.delete(vacancy)
    db.session.commit()
    return jsonify({'message': 'Vacancy deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
