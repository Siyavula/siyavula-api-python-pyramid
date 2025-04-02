import os

from datetime import date
from random import randint
import requests

from dateutil.relativedelta import relativedelta
from pyramid.view import view_config

REGION = "ZA"  # The country code - can be: 'ZA', 'NG', 'RW', 'INTL'
CURRICULUM = "CAPS"  # The curriculum code - can be: 'CAPS', 'NG', 'CBC', 'INTL'


@view_config(route_name="anonymous", renderer="/templates/anonymous.jinja2")
def anonymous(request):
    api_base_url = request.registry.settings["api_base_url"]
    template_id = 2122
    random_seed = 487029  # Random seed is optional, one will be generated if not provided.

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)

    return {
        "token": client_token,
        "template_id": template_id,
        "random_seed": random_seed,
        "api_base_url": api_base_url + "/",
        "sandbox_mode": False,
    }


@view_config(route_name="standalone", renderer="/templates/standalone.jinja2")
def standalone(request):
    api_base_url = request.registry.settings["api_base_url"]
    template_id = 2122
    random_seed = 487029  # Random seed is optional, one will be generated if not provided.
    user_id = "1"

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        "token": client_token,
        "user_token": user_token,
        "template_id": template_id,
        "random_seed": random_seed,
        "api_base_url": api_base_url + "/",
    }


@view_config(route_name="standalone_list", renderer="/templates/standalone_list.jinja2")
def standalone_list(request):
    api_base_url = request.registry.settings["api_base_url"]
    # Format [[template_id, random_seed(optional)], ...]
    template_list = [[4858], [2216, 339850], [2198], [4901, 339297], [4902]]
    user_id = "1"

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        "token": client_token,
        "user_token": user_token,
        "template_list": template_list,
        "api_base_url": api_base_url + "/",
    }


@view_config(route_name="assignment", renderer="/templates/assignment.jinja2")
def assignment(request):
    api_base_url = request.registry.settings["api_base_url"]
    assignment_id = 9664  # Change this to one of your own assignments.
    user_id = "1"

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        "token": client_token,
        "user_token": user_token,
        "assignment_id": assignment_id,
        "api_base_url": api_base_url + "/",
    }


@view_config(route_name="practice", renderer="/templates/practice.jinja2")
def practice(request):
    api_base_url = request.registry.settings["api_base_url"]
    section_id = 204  # Change this to the section you wish to practice.
    user_id = "1"

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        "token": client_token,
        "user_token": user_token,
        "section_id": section_id,
        "api_base_url": api_base_url + "/",
    }


@view_config(route_name="get_activity", renderer="/templates/get_activity.jinja2")
def get_activity(request):
    api_base_url = request.registry.settings["api_base_url"]
    activity_template_id = "0fb33b26-4ac1-45a2-9b9f-5b53e76ad944"
    template_response_uuid = "a388fd98-85da-4d29-9535-5f31ddab1606"
    user_id = "1"

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        "token": client_token,
        "user_token": user_token,
        "activity_template_id": activity_template_id,
        "template_response_uuid": template_response_uuid,
        "api_base_url": api_base_url + "/",
    }


@view_config(route_name="toc", renderer="/templates/toc.jinja2")
def toc(request):
    api_base_url = request.registry.settings["api_base_url"]

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)

    # Get the Practice Table of Contents
    headers = {"JWT": client_token}
    res = requests.get(f"{api_base_url}/api/siyavula/v1/toc", verify=False, headers=headers)
    toc = res.json()

    return {"toc": toc}


@view_config(route_name="practice_toc_with_mastery", renderer="/templates/toc.jinja2")
def practice_toc_with_mastery(request):
    api_base_url = request.registry.settings["api_base_url"]
    user_id = "1"

    # The options for subject are:
    #    South Africa:                     'maths', 'science'
    #    Rest of Africa and International: 'maths', 'physics', 'chemistry'
    subject = "maths"

    # The options are:
    #     South Africa:    8 - 12
    #     Nigeria:         7 - 12
    #     Rwanda:          7 - 10
    #     International:   8 - 12
    grade = "8"

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    # Get the Practice Table of Contents
    headers = {"JWT": client_token, "Authorization": user_token}

    res = requests.get(
        "{}/api/siyavula/v1/toc/user/{}/subject/{}/grade/{}".format(
            api_base_url, user_id, subject, grade
        ),
        verify=False,
        headers=headers,
    )

    toc = res.json()

    return {"toc": toc}


@view_config(route_name="response_data", renderer="/templates/response_data.jinja2")
def response_data(request):
    api_base_url = request.registry.settings["api_base_url"]

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)

    headers = {"JWT": client_token}

    last_month = date.today().replace(day=1) + relativedelta(months=-1)
    first_day = last_month + relativedelta(day=1)
    last_day = last_month + relativedelta(day=31)

    # The start and end dates must be in the format of ISO8601.
    data = {"start": first_day.isoformat(), "end": last_day.isoformat()}

    res = requests.post(
        f"{api_base_url}/api/siyavula/v1/responses", verify=False, json=data, headers=headers
    )
    response = res.json()

    return {"responses": response}


@view_config(route_name="user_link_token", renderer="/templates/user_link_token.jinja2")
def user_link_token(request):
    api_base_url = request.registry.settings["api_base_url"]

    # Authentication payload
    data = {
        "name": os.environ["api_client_name"],
        "password": os.environ["api_client_password"],
        "region": REGION,
        "curriculum": CURRICULUM,
    }

    client_token = get_client_token(api_base_url, data)

    headers = {"JWT": client_token}

    # Create User Login Token
    data = {
        "external_user_id": f"user_token_test_{randint(0, 99999)}",
        "redirect_url": request.route_url("user_link_token_redirect"),
    }
    res = requests.post(
        f"{api_base_url}/api/siyavula/v1/user/link", verify=False, json=data, headers=headers
    )
    create_token_response = res.json()

    # Get token
    res = requests.get(
        f'{api_base_url}/api/siyavula/v1/user/link/{create_token_response["token"]}',
        verify=False,
        headers=headers,
    )
    get_token_response = res.json()

    return {
        "token_data": get_token_response,
        "verification_url": create_token_response["verification_url"],
    }


@view_config(
    route_name="user_link_token_redirect", renderer="/templates/user_link_token_redirect.jinja2"
)
def user_link_token_redirect(request):
    token_id = request.GET.get("token")
    status = request.GET.get("token_status")
    external_user_id = request.GET.get("external_user_id")
    error = request.GET.get("error")

    return {
        "token_id": token_id,
        "status": status,
        "external_user_id": external_user_id,
        "error": error,
    }


def get_client_token(api_base_url, data):
    response = requests.post(f"{api_base_url}/api/siyavula/v1/get-token", verify=False, json=data)
    return response.json()["token"]


def get_user_token(api_base_url, user_id, client_token, data):
    # Ensure you have created a user with the external id specified or this won't work.
    headers = {"JWT": client_token}
    res = requests.get(
        f"{api_base_url}/api/siyavula/v1/user/{user_id}/token",
        verify=False,
        json=data,
        headers=headers,
    )
    return res.json()["token"]
