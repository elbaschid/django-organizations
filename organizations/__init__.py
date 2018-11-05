#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012-2018, Ben Lopatin and contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.  Redistributions in binary
# form must reproduce the above copyright notice, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided with
# the distribution
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__ = "Ben Lopatin"
__email__ = "ben@wellfire.co"
__version__ = "2.0.0a1"


default_app_config = "organizations.apps.OrganizationsConfig"


ORGANIZATION_MODEL = "organizations.Organization"
ORGANIZATION_USER_MODEL = "organizations.OrganizationUser"
ORGANIZATION_OWNER_MODEL = "organizations.OrganizationOwner"
ORGANIZATION_INVITATION_MODEL = "organizations.OrganizationInvitation"


def _get_model_from_setting(name):
    from django.conf import settings
    from django.apps import apps
    org_model = getattr(settings, name, globals()[name])
    return apps.get_model(*org_model.rsplit(".", 1))


def get_org_model():
    return _get_model_from_setting("ORGANIZATION_MODEL")


def get_org_user_model():
    return _get_model_from_setting("ORGANIZATION_USER_MODEL")


def get_org_owner_model():
    return _get_model_from_setting("ORGANIZATION_OWNER_MODEL")


def get_org_invitation_model():
    return _get_model_from_setting("ORGANIZATION_INVITATION_MODEL")
