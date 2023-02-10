from models import Services
from flask import render_template, url_for, redirect, Blueprint, request, flash
from flask_login import login_required
from config import db
from services.forms import ServiceForm

service = Blueprint('service', __name__)

@service.route('/service')
@login_required
def service():
    service = Services.query.all()
    return render_template('service.html', service=service)

@service.route('/service/create', methods=['GET', 'POST'])
@login_required
def create_service():
    form = ServiceForm()
    if request.method == 'POST' and form.validate():
        service = Services(title=form.title.data,  description=form.description.data, icon=form.icon.data)
        db.session.add(service)
        db.session.commit()
        flash('Data berhasil ditambahkan', 'success')
        return redirect(url_for('service.service'))
    return render_template('create_service.html', form=form)


