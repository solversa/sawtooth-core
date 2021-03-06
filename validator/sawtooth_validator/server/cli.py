# Copyright 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import sys
import time

from sawtooth_validator.server.core import Validator


def main(args=sys.argv[1:]):
    validator = Validator('0.0.0.0:40000')
    validator.start()

    try:
        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print >>sys.stderr, "Interrupted!"
    finally:
        validator.stop()
