from flask import Blueprint, render_template, redirect, url_for, flash, send_file
from flask_login import login_required, current_user
from app.models.aspirante import Aspirante
from app.utils.helpers import generar_referencia
from app.services.pdf_service import generar_pdf

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/dashboard')
@login_required
def dashboard():
    aspirante = Aspirante.query.filter_by(id=current_user.aspirante_id).first()
    return render_template("dashboard.html", aspirante=aspirante)

@pdf_bp.route('/ver_pdf')
@login_required
def ver_pdf():
    aspirante = Aspirante.query.filter_by(id=current_user.aspirante_id).first()
    if not aspirante:
        flash("No se encontró el aspirante.", "danger")
        return redirect(url_for('pdf.dashboard'))

    referencia = generar_referencia(aspirante.consecutivo)
    pdf_path = generar_pdf(aspirante, referencia)

    return send_file(pdf_path, as_attachment=False)

@pdf_bp.route('/descargar_pdf')
@login_required
def descargar_pdf():
    aspirante = Aspirante.query.filter_by(id=current_user.aspirante_id).first()
    if not aspirante:
        flash("No se encontró el aspirante.", "danger")
        return redirect(url_for('pdf.dashboard'))

    referencia = generar_referencia(aspirante.consecutivo)
    pdf_path = generar_pdf(aspirante, referencia)

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=f"Ficha_{aspirante.folio}.pdf"
    )