from models import About
from flask import render_template, url_for, redirect, Blueprint, request, flash
from flask_login import login_required
from config import db
from abouts.forms import AboutForm

about = Blueprint('about', __name__)

@about.route('/about')
@login_required
def abouts():
    about = About.query.all()
    return render_template('about.html', about=about)
    

@about.route('/about/create', methods=['GET', 'POST'])
@login_required
def create_about():
    form = AboutForm()
    if request.method == 'POST' and form.validate():
        about = About(name=form.name.data, description=form.description.data, birth=form.birth.data,
                      address=form.address.data, email=form.email.data, image_link=form.image_link.data, phone=form.phone.data)
        db.session.add(about)
        db.session.commit()
        flash('Data berhasil di tambahkan', 'success')
        return redirect(url_for('about.about'))
    return render_template('about_create.html', form=form)


@about.route('/about/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_about(id):
    about = About.query.get_or_404(id)
    form = AboutForm()
    if request.method == 'POST' and form.validate():
        about.name = form.name.data
        about.description = form.description.data
        about.birth = form.birth.data
        about.address = form.address.data
        about.email = form.email.data
        about.image_link = form.image_link.data
        about.phone = form.phone.data
        db.session.commit()
        flash('Data berhasil di ubah', 'success')
        return redirect(url_for('about.about', id=about.id))
    elif request.method == 'GET':
        form.name.data = about.name
        form.description.data = about.description
        form.birth.data = about.birth
        form.address.data = about.address
        form.email.data = about.email
        form.image_link.data = about.image_link
        form.phone.data = about.phone
    return render_template('about_create.html', title='Update About', form=form, legend='Update About')


@about.route('/delete/<int:id>/delete', methods=['POST'])
@login_required
def delete_about(id):
    about = About.query.get_or_404(id)
    db.session.delete(about)
    db.session.commit()
    flash('Data Berhasil Dihapus')
    return redirect(url_for('about.about'))
