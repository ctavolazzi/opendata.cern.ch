# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Frontpage records."""

from invenio_search.engine import dsl
from invenio_search.api import RecordsSearch


class FeaturedArticlesSearch(RecordsSearch):
    """Search class for records that goes on the frontpage."""

    class Meta:
        """Default index and filter for frontpage search."""

        index = 'records-docs-v1.0.0'

    def __init__(self, **kwargs):
        """Initialize instance."""
        super(FeaturedArticlesSearch, self).__init__(**kwargs)
        self.query = dsl.Q('exists', field='featured')
