# ---------------------------------------------------------------------------
# MTDA Service discovery using Zeroconf
# ---------------------------------------------------------------------------
#
# This software is a part of MTDA.
# Copyright (C) 2021 Siemens Digital Industries Software
#
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
# ---------------------------------------------------------------------------

import zeroconf


class ServiceHandlers(object):

    def __init__(self, listener):
        self.listener = listener

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if self.listener.onServiceEvent:
            self.listener.onServiceEvent("ADD", name, info)

    def remove_service(self, zeroconf, type, name):
        if self.listener.onServiceEvent:
            self.listener.onServiceEvent("REMOVE", name)

    def update_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if self.listener.onServiceEvent:
            self.listener.onServiceEvent("UPDATE", name, info)


class ServiceListener(object):

    def __init__(self, domain, onServiceEvent=None):
        self.browser = None
        self.domain = domain
        self.onServiceEvent = onServiceEvent

    def listen(self):
        all = zeroconf.InterfaceChoice.All
        self.zeroconf = zeroconf.Zeroconf(interfaces=all)
        self.browser = zeroconf.ServiceBrowser(
                self.zeroconf, self.domain, ServiceHandlers(self))
        self.browser.run()

    def shutdown(self):
        if self.browser:
            self.browser.cancel()
