import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2022 , 9 , 5 ) ,
        title = 'DATA Subscriptions' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
DATA member society subscriptions are now due\
""" ,
        item_text = """\
<div class="rows columns">
<p>
Because of Covid, we suspended subscriptions in 2020 and 2021, but we now feel
that, as most companies have resumed their performances, it is the right time to
start collecting them again. The subscription is £5 for two years and must be
paid if your member society is to continue to publicise its events via the DATA
Diary under the terms of the <a href="/diary_scheme">Diary Scheme</a>.
</p>
<p>
We will be grateful if member societies can pay their subscription of £5 at
their earliest convenience. Letters have been emailed to our Treasurer contacts
within our member societies requesting payment, along with details of how to pay
but if you believe your member society has not received this due to out of date
contact details then please email <a
href="mailto:admin@derbyartsandtheatre.org.uk">admin@derbyartsandtheatre.org.uk
</a> for further information.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0027_guildhall_theatre_survey' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
