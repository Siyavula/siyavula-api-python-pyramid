def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('get_question', '/')
    config.add_route('get_question_responsive', '/responsive')
    config.add_route('get_question_basic', '/basic')
