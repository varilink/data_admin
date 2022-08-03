import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2022 , 8 , 3 ) ,
        title = 'Guildhall Theatre survey to inform DATA\'s lobbying position' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
Survey of DATA member societies regarding the Guildhall Theatre\
""" ,
        item_text = """\
<div class="rows columns">
<p>
DATA has been lobbying Derby City Council for information and action on the re-
opening of the Guildhall Theatre ever since its closure for repairs in January
2019. Prior to that date, the Guildhall had been used by many amateur groups for
their productions. We have been informed that the Council want to take a
holistic view of how a refurbished Guildhall could/should fit into the cultural
offer of the Market Place area. One senior councillor told us that the reopening
was unlikely before 2025.
</p>
<p>
In the meantime, amateur groups who previously used the Guildhall have either
found alternative venues or, sadly, ceased operating. DATA would like to press
the Council more vigorously for information but, before we do, we need to know
the extent of the interest in hiring the Guildhall when it reopens. We would
therefore be grateful if you would anonymously complete <a target="_blank"
href="https://www.surveymonkey.co.uk/r/MLDD8LF">this very short questionnaire
</a>. We are not asking for a firm commitment, just an indication of your
thinking.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0026_chair_xmas_letter_2021' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
