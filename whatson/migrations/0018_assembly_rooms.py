import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2019 , 9 , 23 ) ,
        title = 'Delay to Completion of Assembly Rooms Works' ,
        image = '/assets/img/news_items/assembly_rooms_card.jpg' ,
        precis = """\
DATA notified of delay to completion of scheduled works to November 2021\
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/ground-floor-entrance-area.jpg"
width="640px" height="360px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="225px"
src="/assets/img/news_items/ground-floor-entrance-area.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/ground-floor-entrance-area.jpg"
width="550px" height="310px">
<p>
DATA received an update on 23rd September 2019 concerning the planned Assembly
Rooms works as follows:
</p>
<blockquote>
<p>
Derby City Council will begin the next phase of work on the new and improved Assembly
Rooms after planners approved designs. It has also renewed its commitment to delivering
the venue at the agreed budget of £24m.
</p>
<p>
This major investment will be key to a vibrant city centre. It aligns with the key priority of
Derby’s City Centre Masterplan 2030, complementing a mix of retail, leisure with
accommodation developments across the city as part of the council’s plans to boost future
investment into Derby.
</p>
<p>
Following a review over the summer a revised programme has been presented to the
Council with a scheduled completion of works in November 2021. A contractor has been
appointed and will be on-site in November to begin initial works including the removal of
asbestos.
</p>
<p>
Perfect Circle, which was appointed to design the new Assembly Rooms, previously advised
that the project could be completed by autumn 2020.
</p>
<p>
However over the summer, Perfect Circle presented a much longer project timeline. On
receipt of this information, the Council asked that an independent review of the project was
undertaken by specialist external consultants.
</p>
<p>
A new external project manager had been appointed and Derby City Council has worked
robustly with Perfect Circle on a new project timeline for this complex project.
</p>
<p>
Councillor Matthew Holmes, Deputy Leader of Derby City Council, said:
</p>
<p>
"Obtaining planning consent is an important milestone for this project and I’m delighted that
the first contractors will be on site as soon as next month.”
</p>
<p>
“We are committed to getting the new improved Assembly Rooms open as the Council’s
number one city centre priority. We are working collaboratively with project partners to
ensure that everything practicably possible will be done to see the venue open as soon as
possible.
</p>
<p>
“As a consequence of our robust intervention into this project, I am confident that the new
and improved Assembly Rooms will be delivered and act as a catalyst for the continued
regeneration of Derby. The benefits for our local economy and businesses will be significant
as well as offering a superb conference and events venue for residents and visitors to enjoy
a varied and exciting programme for many years to come.”
</p>
<cite>Derby City Council</cite>
</blockquote>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0017_guildhall_news_item' ) ,
    ]

    operations = [

        migrations.RunPython ( news_item ) ,

    ]
