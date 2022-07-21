import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2019 , 9 , 25 ) ,
        title = 'Delay to Completion of Guildhall Works' ,
        image = '/assets/img/news_items/guildhall_card.jpg' ,
        precis = """\
DATA notified of extension to closure of Guildhall Theatre\
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
On 25th September 2019 DATA received the following update on the Guildhall
closure from Derby City Council:
</p>
<blockquote>
<p>
In the light of new survey findings Derby's Guildhall Theatre will remain closed
for an extended period of time.
</p>
<p>
Following planned work to the auditorium ceiling last year, problems were found
which led to the eventual closure in January 2019 due to safety concerns.
Initially it was hoped that the venue would be re-opened later this year.
</p>
<p>
As the project has progressed, contractors were able to undertake more extensive
surveys. Earlier this month findings of the surveys show that the condition of
the fabric of the building is much worse than previously thought and is beyond
the original scope of work.
</p>
<p>
During this period, the Council has also been exploring all the available
options to put in position temporary measures to make the building safe to open.
Despite our best efforts all the measures considered would put at risk the
historic infrastructure and require Listed Building Consent and are not viable.
</p>
<p>
The Christmas show, The Christmas Toy shop Mystery, will be cancelled and all
customers will be refunded in full. To further compensate customers we’ll be
offering a special discount for Peter Pan, the pantomime at Derby Arena this
Christmas.
</p>
<p>
The Council has decided to take this opportunity to undertake an holistic review
of the building to determine what is required to ensure the Guildhall Theatre’s
long term future. It will look to complete the review of the building by the end
of the year and a new programme of work is being drawn up.
</p>
<p>
Councillor Matthew Holmes, Deputy Leader of Derby City Council, said:
</p>
<p>
“This has been an immensely frustrating situation for us all as each step in the
repair process has led to the discovery of additional issues.
</p>
<p>
It is, of course, disappointing that we can’t re-open for Christmas but this is
now the right time to take a breath and rather than just repair the ceiling, we
need to consider what else we need to do to be able to restore this vital
historic building properly.”
<cite>Derby City Council</cite>
</blockquote>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0018_assembly_rooms' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]