# Copyright 2023 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from abc import ABCMeta, abstractmethod


class QuotaChecker(metaclass=ABCMeta):
    @abstractmethod
    def get_avaliable_worker_num(self):
        pass


class UnlimitedQuotaChecker(QuotaChecker):
    """No resource limits."""

    def get_avaliable_worker_num(self):
        """Assume there is always enough resource."""
        return sys.maxsize
