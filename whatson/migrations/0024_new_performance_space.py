import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2021 , 6 , 15 ) ,
        title = 'Derby Market Place: Temporary Performance Venue' ,
        image = '/assets/img/news_items/performance-venue-card.png' ,
        precis = """\
A new performance venue has become available in Derby Market Place that has the
potential to be used for events staged by DATA members\
""" ,
        item_text = """\
<div class="rows columns">
<p>
A new performance venue has become available in Derby Market Place that has the
potential to be used for events staged by DATA members. This opportunity has
been created by Derby City Council&#39;s Derby Market Place project.
</p>
<img class="float-center" src="/assets/img/news_items/performance-venue.png">
<p>
The marquee venue, which opens with performances on 26<sup>th</sup> June, will
have a maximum seating capacity of 300 (though, of course, this will be reduced
whilst social distancing measures remain). The venue will have a wide range of
events, including classical concerts, comedy, musical theatre performances, a
beer festival, jazz gigs, corporate events, markets, virtual reality experiences
and more! These will run through to the end of the year, when the venue and city
centre move into &nbsp;Festive Derby&nbsp; mode.
</p>
<p>
You can find more details on the <a href="https://www.derbymarketplace.co.uk"
target="_blank">Derby Market Place website</a>.
</p>
<p>
Several local companies will be staging concert performances in the venue (which
will have stage, sound and lighting facilities) during October, and there are
opportunities for DATA member organisations to be involved if they have suitable
shows. A &quot;standard&quot; package deal (with further options, depending on
requirements) has been worked out, to enable local performance companies to use
the space on a &quot;low-risk&quot; basis. Should any companies wish to discuss
this further, please contact Bob Rushton (who some will know from Derby LIVE /
Guildhall Theatre) on <a href="mailto:dmp@bobonarts.co.uk">dmp@bobonarts.co.uk
</a>
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0023_waiving_renewal_fees' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
