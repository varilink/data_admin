import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2021 , 6 , 29 ) ,
        title = 'New Opera Company seeks Musical Director' ,
        image = '/assets/img/news_items/noc-logo.png' ,
        precis = """\
New Opera Company, a DATA member society, is seeking to appoint a Musical
Director\
""" ,
        item_text = """\
<div class="rows columns">
<p>
New Opera Company, Derby is seeking to appoint a Musical Director following the
retirement in June 2020 of Miss Margaret Slater who has conducted and guided the
Company very successfully for many years.
</p>
<p>
Formed in 1959, New Opera Company, Derby is an enthusiastic and friendly group
of singers with the aim to provide opportunities for all persons to enjoy
singing or performing grand opera or operetta locally, either on stage or in
concerts. The company rehearses in St Augustine’s Community Centre, at Normanton
Library, Derby on Wednesday evenings and performs at venues in Derby or in
Derbyshire and neighbouring counties.
</p>
<p>The Company now presents four concert performances in the summer and two in
the winter at varied venues attracting enthusiastic audiences. Recent programmes
have included excerpts from: The Marriage of Figaro, The Bartered Bride, Merrie
England, West Side Story and The Phantom of the Opera. We have a regular, well
qualified accompanist and a deputy when needed.
</p>
<p>
We are looking for someone who can demonstrate an excellent conducting and
rehearsal technique, including the ability to lead and, critically, to develop
the skills of a group with varied singing abilities and experiences. Candidates
should have a wide knowledge of suitable repertoire including Opera, Operetta
and Musical Theatre and be willing to share in selecting concert programmes. The
post requires good personal skills for maintaining a co-operative, encouraging,
working environment, with all in the company including, the Music Committee and
the Accompanist.
</p>
<p>
We are seeking to appoint someone with plenty of enthusiasm, commitment and a
willingness to share in our ambition for the company to grow by attracting new
members, especially younger singers. For more details or an application form
please contact the above email address or telephone number. At a later stage
selected applicants will be invited to conduct a Wednesday evening rehearsal.
</p>
<p>
Contact us for further information via email to <a
href="mailto:newoperacompany@hotmail.com">newoperacompany@hotmail.com</a> or on
telephone number 01332 557096.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0024_new_performance_space' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
