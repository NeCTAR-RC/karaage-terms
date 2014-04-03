# Copyright 2014 The University of Melbourne
#
# This file is part of karaage-terms.
#
# karaage-terms is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# karaage-terms is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with karaage-terms If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from karaage.applications import models as application_models
from karaage.people import models as people_models
from karaage.machines import models as machine_models


class Terms(models.Model):
    title = models.CharField(max_length=255L)
    machine = models.ForeignKey(machine_models.MachineCategory, editable=False)
    terms = models.TextField()
    class Meta:
        db_table = 'terms'


class UserAgreed(models.Model):
    person = models.ForeignKey(people_models.Person, related_name='terms_agreed', editable=False)
    terms = models.ForeignKey(Terms, related_name='users_agreed', editable=False)
    when = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'user_agreed_terms'
