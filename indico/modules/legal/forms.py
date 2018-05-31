# This file is part of Indico.
# Copyright (C) 2002 - 2018 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from wtforms.fields import TextAreaField
from wtforms.fields.html5 import URLField
from wtforms.validators import URL

from indico.util.i18n import _
from indico.web.forms.base import IndicoForm
from indico.web.forms.widgets import CKEditorWidget


class LegalMessagesForm(IndicoForm):
    network_protected_disclaimer = TextAreaField(_("Network-protected information disclaimer"), widget=CKEditorWidget())
    restricted_disclaimer = TextAreaField(_("Restricted information disclaimer"), widget=CKEditorWidget())
    tos_url = URLField(_('URL'), [URL()],
                       description=_("The URL to an external page with terms and conditions"))
    tos = TextAreaField(_("Text"), widget=CKEditorWidget(),
                        description=_('Only used if no URL is provided'))
    privacy_policy_url = URLField(_('URL'), [URL()],
                                  description=_("The URL to an external page with the privacy policy"))
    privacy_policy = TextAreaField(_("Text"), widget=CKEditorWidget(),
                                   description=_('Only used if no URL is provided'))
