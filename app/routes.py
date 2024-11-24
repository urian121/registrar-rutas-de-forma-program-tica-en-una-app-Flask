from .views import home, about, contact, services, greet_user

def registrar_rutas(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/about', 'about', about)
    app.add_url_rule('/contact', 'contact', contact)
    app.add_url_rule('/services', 'services', services)
    app.add_url_rule('/greet/<username>', 'greet_user', greet_user)
