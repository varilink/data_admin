import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2020 , 3 , 3 ) ,
        title = 'Temporary Performance Venue' ,
        image = '/assets/img/news_items/temporary-venue-card.jpg' ,
        precis = """\
DATA gains Council commitment to temporary performance venue\
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/assembly_rooms_1.jpg"
width="393px" height="583px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="259px" height="385px"
src="/assets/img/news_items/assembly_rooms_1.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/assembly_rooms_1.jpg"
width="139px" height="192px">
<p>
Derby City Council have terminated the project to refurbish the Assembly Rooms,
and said that the Guildhall Theatre will be closed for an extended period while
a holistic view is taken of all of the repairs needed to the building, including
the roof.  The Guildhall closure has caused major financial and logistical
problems to a number of amateur groups who have had to either cancel productions
or relocate them to other venues, in some cases outside the city e.g. Repton and
Long Eaton.  Indeed, there are amateur companies who are in such great financial
difficulties that they could fold.
</p>
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="640px" height="525px">
<img class="float-right show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="328px"
src="/assets/img/news_items/guildhall.jpg">
<img class="float-right show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="550px" height="451px">
<p>
Given these circumstances, DATA have been lobbying the Council hard for a
temporary performance venue close to the city centre. We are pleased to report
that, on Monday 2nd March, the Leader of the Council (Councillor Chris Poulter)
announced that a temporary performance venue will be provided on the Market
Place while the Assembly Rooms remain closed. We have also received a personal
assurance from Councillor Poulter that we will be invited to a meeting in a few
weeks when further details of the project will be shared.
</p>
<p>
This demonstrates the value of amateur theatre and music groups working
together, through DATA, for our common good.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0019_guildhall_news_item' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
