import os
import requests

from pyramid.view import view_config

REGION = 'ZA'           # The country code - can be: 'ZA', 'NG', 'RW', 'INTL'
CURRICULUM = 'CAPS'     # The curriculum code - can be: 'CAPS', 'NG', 'CBC', 'INTL'


@view_config(route_name='standalone_responsive', renderer='/templates/standalone_responsive.jinja2')
def standalone_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    template_id = 2122
    random_seed = 487029  # Random seed is optional, one will be generated if not provided.
    user_id = '1'

    # Use 'responsive' to get a responsive theme for modern devices or 'basic' for older devices
    # without JavaScript support.
    theme = 'responsive'

    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': REGION,
        'curriculum': CURRICULUM,
        'theme': theme
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        'token': client_token,
        'user_token': user_token,
        'template_id': template_id,
        'random_seed': random_seed,
        'api_base_url': api_base_url + '/'
    }


@view_config(route_name='standalone_list_responsive',
             renderer='/templates/standalone_list_responsive.jinja2')
def standalone_list_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    # Format [[template_id, random_seed(optional)], ...]
    template_list = [[4858], [2216, 339850], [2198], [4901, 339297], [4902]]
    user_id = '1'

    # Use 'responsive' to get a responsive theme for modern devices or 'basic' for older devices
    # without JavaScript support.
    theme = 'responsive'

    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': REGION,
        'curriculum': CURRICULUM,
        'theme': theme
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        'token': client_token,
        'user_token': user_token,
        'template_list': template_list,
        'api_base_url': api_base_url + '/'
    }


@view_config(route_name='assignment_responsive', renderer='/templates/assignment_responsive.jinja2')
def assignment_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    assignment_id = 9664  # Change this to one of your own assignments.
    user_id = '1'

    # Use 'responsive' to get a responsive theme for modern devices or 'basic' for older devices
    # without JavaScript support.
    theme = 'responsive'

    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': REGION,
        'curriculum': CURRICULUM,
        'theme': theme
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        'token': client_token,
        'user_token': user_token,
        'assignment_id': assignment_id,
        'api_base_url': api_base_url + '/'
    }


@view_config(route_name='practice_responsive', renderer='/templates/practice_responsive.jinja2')
def practice_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    section_id = 204  # Change this to the section you wish to practice.
    user_id = '1'

    # Use 'responsive' to get a responsive theme for modern devices or 'basic' for older devices
    # without JavaScript support.
    theme = 'responsive'

    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': REGION,
        'curriculum': CURRICULUM,
        'theme': theme
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        'token': client_token,
        'user_token': user_token,
        'section_id': section_id,
        'api_base_url': api_base_url + '/'
    }


@view_config(route_name='get_activity', renderer='/templates/get_activity.jinja2')
def get_activity_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    activity_template_id = '0fb33b26-4ac1-45a2-9b9f-5b53e76ad944'
    template_response_uuid = 'a388fd98-85da-4d29-9535-5f31ddab1606'
    user_id = '1'

    # Use 'responsive' to get a responsive theme for modern devices or 'basic' for older devices
    # without JavaScript support.
    theme = 'responsive'

    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': REGION,
        'curriculum': CURRICULUM,
        'theme': theme
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    return {
        'token': client_token,
        'user_token': user_token,
        'activity_template_id': activity_template_id,
        'template_response_uuid': template_response_uuid,
        'api_base_url': api_base_url + '/'
    }


@view_config(route_name='practice_toc', renderer='/templates/practice_toc.jinja2')
def practice_toc(request):
    api_base_url = request.registry.settings['api_base_url']

    # Use 'responsive' to get a responsive theme for modern devices or 'basic' for older devices
    # without JavaScript support.
    theme = 'responsive'

    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': REGION,
        'curriculum': CURRICULUM,
        'theme': theme
    }

    client_token = get_client_token(api_base_url, data)

    # Get the Practice Table of Contents
    headers = {'JWT': client_token}
    res = requests.get('{}/api/siyavula/v1/toc'.format(api_base_url), verify=False,
                       headers=headers)
    toc = res.json()

    return {
        'toc': toc
    }


@view_config(route_name='practice_toc_with_mastery', renderer='/templates/practice_toc.jinja2')
def practice_toc_with_mastery(request):
    api_base_url = request.registry.settings['api_base_url']
    user_id = '1'

    # The options for subject are:
    #    South Africa:                     'maths', 'science'
    #    Rest of Africa and International: 'maths', 'physics', 'chemistry'
    subject = 'maths'

    # The options are:
    #     South Africa:    8 - 12
    #     Nigeria:         7 - 12
    #     Rwanda:          7 - 10
    #     International:   8 - 12
    grade = '8'

    # Use 'responsive' to get a responsive theme for modern devices or 'basic' for older devices
    # without JavaScript support.
    theme = 'responsive'

    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': REGION,
        'curriculum': CURRICULUM,
        'theme': theme
    }

    client_token = get_client_token(api_base_url, data)
    user_token = get_user_token(api_base_url, user_id, client_token, data)

    # Get the Practice Table of Contents
    headers = {
        'JWT': client_token,
        'Authorization': user_token
    }

    res = requests.get(
        '{}/api/siyavula/v1/toc/user/{}/subject/{}/grade/{}'.format(
            api_base_url, user_id, subject, grade),
        verify=False, headers=headers)

    toc = res.json()

    return {
        'toc': toc
    }


def get_client_token(api_base_url, data):
    response = requests.post('{}/api/siyavula/v1/get-token'.format(api_base_url),
                             verify=False, json=data)
    return response.json()['token']


def get_user_token(api_base_url, user_id, client_token, data):
    # Ensure you have created a user with the external id specified or this won't work.
    headers = {'JWT': client_token}
    res = requests.get('{}/api/siyavula/v1/user/{}/token'.format(api_base_url, user_id),
                       verify=False, json=data, headers=headers)
    return res.json()['token']
