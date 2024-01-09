from .models import Feedback
from .forms import FeedbackForm
from flask import flash, redirect, render_template, url_for
from . import feedback
from .. import db, navigation

@feedback.context_processor
def inject_navigation():
    return dict(navigation=navigation())

@feedback.route('/reviews', methods=['GET', 'POST'])
def feedbacks():
    form = FeedbackForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        feedback_entry = Feedback(name=name, email=email, message=message)
        db.session.add(feedback_entry)
        db.session.commit()

        flash('Ваш відгук був збережений', 'success')
        return redirect(url_for('feedback.feedbacks'))

    Reviews = Feedback.query.all()

    return render_template('reviews.html', form=form, feedbacks=Reviews)