from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app import db
from app.models import Appointment

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

@bp.route('/appointments', methods=['POST'])
def create_appointment():
    title = request.form.get('title')
    date = request.form.get('date')
    notes = request.form.get('notes', '')
    appointment = Appointment(title=title, date=date, notes=notes)
    db.session.add(appointment)
    db.session.commit()
    return redirect(url_for('main.index'))
  
@bp.route('/appointments/<int:id>/edit', methods=['GET'])
def edit_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    return render_template('edit_appointment.html', appointment=appointment)

@bp.route('/appointments/<int:id>/edit', methods=['POST'])
def update_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    appointment.title = request.form.get('title', appointment.title)
    appointment.date = request.form.get('date', appointment.date)
    appointment.notes = request.form.get('notes', appointment.notes)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/appointments/<int:id>/delete', methods=['POST'])
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    db.session.delete(appointment)
    db.session.commit()
    return redirect(url_for('main.index'))