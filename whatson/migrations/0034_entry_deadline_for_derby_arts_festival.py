import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2024 , 1 , 1 ) ,
        title = 'End of January deadline for entries to the Derby Arts Festival 2024' ,
        image = '/assets/img/news_items/derby-arts-festival-card.jpg' ,
        precis = """\
A reminder that entries for the 2024 Derby Arts Festival must be submitted by 31st January\
""" ,
        item_text = """\
<div class="rows columns clearfix">
<img src="/assets/img/news_items/derby-arts-festival.jpg" class="float-left" width="400"
style="margin-right: 1em;">
<p>
Entries for the 2024 Derby Arts Festival close on 31st January. All participants are encouraged to enter online - see <a href="https://derbyartsfestival.co.uk/enter/" target="_blank">derbyartsfestival.co.uk/enter/</a>.
</p>
<p>
Here is the Derby Arts Festival <a href="https://derbyartsfestival.co.uk/syllabus-2024/" target="_blank">Syllabus 2024</a>. Enquiries can also be emailed to <a href="mailto:enquires@derbyartsfestival.co.uk">enquires@derbyartsfestival.co.uk</a>.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0033_good_news_about_the_guildhall' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
