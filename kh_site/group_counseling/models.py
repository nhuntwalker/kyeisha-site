"""Group coaching models."""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from redactor.fields import RedactorField


DATE_FMT = '%b %d, %Y'
DEFAULT_LOGISTICS = """<ul>
    <li><p>8 group sessions total</p></li>
    <li><p>Total of 12 phenomenal women per group</p></li>
    <li><p>Weekly "office hours" (TBD in the new year) over the phone where I’m available for troubleshooting, Q&A, and check-ins</p></li>
    <li><p>Formation of daily self-care practice-exercises (Monday through Friday) to help you stay focused, build momentum, and move forward throughout the week</p></li>
    <li><p>Tailored invitations to work on between sessions to help you get stronger and more free</p></li>
</ul>"""
DEFAULT_OUTLINE = """
<div>
    <h4>Session 1 &amp; 2  &mdash; Foundational Self Love</h4>
    <p class="group-coach-subhead">Topics:</p>
    <ul>
        <li>Developing self-care practices, transforming self-talk</li>
        <li>Identifying the origin of negative self-talk</li>
        <li>Identifying trauma’s lies, finding personal truths</li>
    </ul>
</div>
<div>
    <h4>Session 3 &amp; 4 &mdash; Transforming Beliefs</h4>
    <p class="group-coach-subhead">Topics:</p>
    <ul>
        <li>Understanding the common limiting beliefs associated with having to navigate domestic violence and childhood abuse.</li>
        <li>Identifying your "Goliath limited beliefs" and its impact on the way you view safety, trust, power/control, intimacy, and self esteem.</li>
        <li>Learn tools to challenge and revise old negative patterns of thinking.</li>
    </ul>
</div>
<div>
    <h4>Session 5 &amp; 6 &mdash; Evaluating Core Values</h4>
    <p class="group-coach-subhead">Topics:</p>
    <ul>
        <li>Articulate your values and WHY you have them</li>
        <li>Identify and re-design your "rulebook" for success and how to acquire what you value; one's judgment of what is important in life.</li>
        <li>Align beliefs to achieve practice values.</li>
    </ul>
</div>
<div>
    <h4>Session 7 &amp; 8 &mdash; Restoring Passion</h4>
    <p class="group-coach-subhead">Topics:</p>
    <ul>
        <li>Identify an area of "Play" and engage in it weekly or monthly.</li>
        <li>Articulate your life goals in the following areas: career, physical health, mental health, emotional health, and spirituality.</li>
        <li>Create a 90-day life goal plan for different life areas.</li>
        <li>Receive guidance and support to create clarity, purpose and restore your passion.</li>
    </ul>
</div>"""
DEFAULT_LOCATION = "600 North 65th street, Seattle, WA"


class CoachingEvent(models.Model):
    """Model for a group coaching event."""

    start_date = models.DateField()
    end_date = models.DateField()
    meeting_days = models.CharField(max_length=1024, default='Wednesdays')
    start_time = models.TimeField()
    end_time = models.TimeField()
    cost = models.DecimalField(
        decimal_places=2, max_digits=5,
        help_text='Cost per person ($)', default=79.00
    )
    external_link = models.URLField(
        max_length=1024,
        help_text='Full URL to the event invite page. Ex: https://www.eventbrite.com/...'
    )
    location = models.CharField(
        default=DEFAULT_LOCATION,
        max_length=1024
    )
    logistics = RedactorField(default=DEFAULT_LOGISTICS)
    outline = RedactorField(default=DEFAULT_OUTLINE)
    current_event = models.BooleanField(
        default=False, help_text='Is this the next group?'
    )

    def __repr__(self):
        return f"<Coaching Event | start { self.start_date.strftime(DATE_FMT) } >"

    def str(self):
        return f"Starting { self.start_date.strftime(DATE_FMT) }"


@receiver(post_save, sender=CoachingEvent)
def one_current(sender, **kwargs):
    instance = kwargs['instance']
    if instance.current_event:
        events = CoachingEvent.objects.exclude(pk=instance.pk).filter(current_event=True).all()
        for event in events:
            event.current_event = False
            event.save()
