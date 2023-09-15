def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('anonymous', '/anonymous')
    config.add_route('standalone', '/standalone')
    config.add_route('standalone_list', '/standalone-list')
    config.add_route('assignment', '/assignment')
    config.add_route('practice', '/practice')
    config.add_route('get_activity', '/get-activity')
    config.add_route('toc', '/toc')
    config.add_route('practice_toc_with_mastery', '/toc-mastery')
