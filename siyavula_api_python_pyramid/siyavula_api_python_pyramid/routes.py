def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('anonymous_responsive', '/anonymous')
    config.add_route('standalone_responsive', '/standalone')
    config.add_route('standalone_list_responsive', '/standalone-list')
    config.add_route('assignment_responsive', '/assignment')
    config.add_route('practice_responsive', '/practice')
    config.add_route('get_activity', '/get-activity')
    config.add_route('toc', '/toc')
    config.add_route('practice_toc_with_mastery', '/toc-mastery')
    config.add_route('response_data', '/response-data')
