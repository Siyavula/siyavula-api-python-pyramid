import os
import requests

from pyramid.view import view_config


@view_config(route_name='standalone_responsive', renderer='/templates/standalone_responsive.jinja2')
def standalone_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    template_id = 2122
    region = 'ZA'  # The country shortcode, can be either 'ZA', 'NG' or 'INTL'.
    curriculum = 'CAPS'  # The curriculum code, can be either 'CAPS', 'NG' or 'INTL'.
    # Use 'responsive' to get a responsive theme for modern devices
    # or 'basic' for older devices without JS support.
    theme = 'responsive'  # The theme to use, can be either 'responsive' or 'basic'.
    random_seed = 487029  # Random seed is optional, one will be generated if not provided.
    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': region,
        'curriculum': curriculum,
        'theme': theme
    }

    # Request client token
    res = requests.post('{}/api/siyavula/v1/get-token'.format(api_base_url),
                        verify=False, json=data)
    token = res.json()['token']

    # Request user token
    # Ensure you have created a user with the external id specified or this won't work.
    user_id = '1'
    headers = {'JWT': token}
    res = requests.get('{}/api/siyavula/v1/user/{}/token'.format(api_base_url, user_id),
                       verify=False, json=data, headers=headers)
    user_token = res.json()['token']

    return {
        'token': token,
        'user_token': user_token,
        'template_id': template_id,
        'random_seed': random_seed,
        'api_base_url': api_base_url + '/'
    }


@view_config(route_name='assignment_responsive', renderer='/templates/assignment_responsive.jinja2')
def assignment_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    region = 'ZA'  # The country shortcode, can be either 'ZA', 'NG' or 'INTL'.
    curriculum = 'CAPS'  # The curriculum code, can be either 'CAPS', 'NG' or 'INTL'.
    # Use 'responsive' to get a responsive theme for modern devices
    # or 'basic' for older devices without JS support.
    theme = 'responsive'  # The theme to use, can be either 'responsive' or 'basic'.
    assignment_id = 9664  # Change this to one of your own assignments.
    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': region,
        'curriculum': curriculum,
        'theme': theme
    }

    # Request client token
    res = requests.post('{}/api/siyavula/v1/get-token'.format(api_base_url),
                        verify=False, json=data)
    token = res.json()['token']

    # Request user token
    # Ensure you have created a user with the external id specified or this won't work.
    user_id = '1'
    headers = {'JWT': token}
    res = requests.get('{}/api/siyavula/v1/user/{}/token'.format(api_base_url, user_id),
                       verify=False, json=data, headers=headers)
    user_token = res.json()['token']

    return {
        'token': token,
        'user_token': user_token,
        'assignment_id': assignment_id,
        'api_base_url': api_base_url + '/'
    }


@view_config(route_name='practice_responsive', renderer='/templates/practice_responsive.jinja2')
def practice_responsive(request):
    api_base_url = request.registry.settings['api_base_url']
    region = 'ZA'  # The country shortcode, can be either 'ZA', 'NG' or 'INTL'.
    curriculum = 'CAPS'  # The curriculum code, can be either 'CAPS', 'NG' or 'INTL'.
    # Use 'responsive' to get a responsive theme for modern devices
    # or 'basic' for older devices without JS support.
    theme = 'responsive'  # The theme to use, can be either 'responsive' or 'basic'.
    section_id = 204  # Change this to the section you wish to practice.
    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': region,
        'curriculum': curriculum,
        'theme': theme
    }

    # Request client token
    res = requests.post('{}/api/siyavula/v1/get-token'.format(api_base_url),
                        verify=False, json=data)
    token = res.json()['token']

    # Request user token
    # Ensure you have created a user with the external id specified or this won't work.
    user_id = '1'
    headers = {'JWT': token}
    res = requests.get('{}/api/siyavula/v1/user/{}/token'.format(api_base_url, user_id),
                       verify=False, json=data, headers=headers)
    user_token = res.json()['token']

    return {
        'token': token,
        'user_token': user_token,
        'section_id': section_id,
        'api_base_url': api_base_url + '/'
    }
