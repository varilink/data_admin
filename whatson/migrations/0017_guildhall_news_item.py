# Further update on the Derby Guildhall situation

import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2019 , 7 , 28 ) ,
        title = 'Guildhall Theatre - Questions to the Council' ,
        image = '/assets/img/news_items/guildhall_card.jpg' ,
        precis = """\
DATA continues to lobby on behalf of its members
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="640px" height="525px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="328px"
src="/assets/img/news_items/guildhall.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="550px" height="451px">
<p>
DATA has been campaigning for some time to get the Guildhall Theatre reopened,
after essential roof repairs are completed, at the earliest opportunity. A
member of the DATA Committee - Tom Banks - asked the following question at the
Derby City Council meeting on Wednesday 24th July:
</p>
<p>
"What is the timescale to complete the repairs to the roof of the Guildhall
Theatre and will the Cabinet Member give an assurance that the Guildhall Theatre
will reopen after these repairs are completed?"
</p>
<p>
The answer given by Councillor Matthew Holms, the Deputy Leader of the Council
was:
</p>
<p>
"The council's contractor and consultant teams continue to undertake structural
investigations and remedial works with the aim of completing repairs as soon as
possible to allow the venue to reopen."
</p>
<p>
Tom was allowed to ask a supplementary question, which was:
</p>
<p>
"Is the Cabinet Member aware of the considerable disruption, inconvenience and
cost to amateur theatre companies affected by the extended closure, some of
which have transferred their productions to theatres outside the city, and what
assistance will be offered to encourage previous users of the Guildhall Theatre
to return?"
</p>
<p>
Councillor Holmes said that the second question was outside of his remit and
should be directed to Councillor Robin Wood, the Cabinet Member for Leisure and
Culture. Tom intends to contact Councillor Wood in the next few days.
</p>
<p>
Tom also has a monthly slot on BBC Radio Derby to talk about amateur theatre and
he raised our concerns there earlier in the week. There was also an item on the
Radio Derby news on Friday morning.
</p>
<p>
DATA understands the need for the Guildhall to be made safe for performers and
audiences, but we will continue to press the Council for this essential facility
to be reopened as soon as possible.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0016_derbymuseums_venues' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]