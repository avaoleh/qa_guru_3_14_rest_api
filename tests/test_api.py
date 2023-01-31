import requests
from requests import Response
from pytest_voluptuous import S
from schemas import schemas
from utils.base_session import test_session
from mimesis.enums import Locale, Gender
from mimesis import Person
import logging


def test_create_user():
    # GIVEN:
    person = Person(Locale.EN)
    user_data = {
        'name': person.first_name(gender=Gender.MALE),
        'job': person.occupation(),
    }

    # WHEN:
    response: Response = test_session.post(
        url='/api/users',
        data=user_data
    )

    # THEN:
    assert response.status_code == 201
    assert response.json() == S(schemas.create_user)
    # logging.info(response.json())
    assert response.json()['name'] == user_data['name']
    assert response.json()['job'] == user_data['job']


def test_update_user():
    # GIVEN:
    person = Person(Locale.EN)
    updated_user_data = {
        'name': person.first_name(gender=Gender.MALE),
        'job': person.occupation(),
    }

    # WHEN:
    response: Response = test_session.put(
        url='/api/users/2',
        data=updated_user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.json() == S(schemas.update_user)
    # logging.info(response.json())
    assert response.json()['name'] == updated_user_data['name']
    assert response.json()['job'] == updated_user_data['job']


def test_delete_user():
    # WHEN:
    response: Response = test_session.delete(
        url='/api/users/2',
    )

    # THEN:
    assert response.status_code == 204


def test_register_user_successful():
    # GIVEN:
    register_user_data = {
        'email': 'eve.holt@reqres.in',
        'password': 'qwerty',
    }

    # WHEN:
    response: Response = test_session.post(
        url='/api/register',
        data=register_user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.json() == S(schemas.register_user)


def test_register_user_unsuccessful():
    # GIVEN:
    register_user_data_unsuccessful = {
        "email": "eve.holt@reqres.in",
    }

    # WHEN:
    response: Response = test_session.post(
        url='/api/register',
        data=register_user_data_unsuccessful
    )

    # THEN:
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
    # logging.info(response.json())


def test_login_user_successful():
    # GIVEN:
    login_user_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    # WHEN:
    response: Response = test_session.post(
        url='/api/login',
        data=login_user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.json() == S(schemas.login_user)


def test_login_user_unsuccessful():
    # GIVEN:
    login_user_data_unsuccessful = {
        "email": "eve.holt@reqres.in"
    }

    # WHEN:
    response: Response = test_session.post(
        url='/api/login',
        data=login_user_data_unsuccessful
    )

    # THEN:
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
