from app import app, db
from app.models import Card
from app.forms import AddNewBusiness
from flask import redirect, render_template



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create_card():
    form = AddNewBusiness()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        phone = form.phone.data
        email = form.email.data
        website = form.website.data
        facebook = form.facebook.data
        address = form.address.data
        sentence = form.sentence.data
        new_card = Card(name=name, category=category, phone=phone, email=email,
                        website=website, facebook=facebook, address=address, sentence=sentence)
        db.session.add(new_card)
        db.session.commit()
        return redirect('/')
    return render_template('create_card.html', form=form)

    # return redirect('/card')


@app.route('/card')
def card():
    pass
