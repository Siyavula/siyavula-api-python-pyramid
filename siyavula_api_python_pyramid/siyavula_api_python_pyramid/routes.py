def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('standalone_responsive', '/standalone')
    config.add_route('assignment_responsive', '/assignment')
    config.add_route('practice_responsive', '/practice')
    config.add_route('practice_toc', '/practice-toc')
