# Copyright 2020 D-Wave Systems Inc.
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

# --------------------------------------------------------------------------#

# This program demonstrates a basic Ocean program that runs a QUBO problem on
# the D-Wave QPU.

# --------------------------------------------------------------------------#

# Import the functions and packages that are used
from dwave.system import EmbeddingComposite, DWaveSampler

import dwave.system
import dwave.inspector

''' Lines for dynamic analysis of dwave functions '''
from dwave_reverse.DwaveReverse import DwaveReverse
import sys
sys.settrace(DwaveReverse.traceit)
''' End of dynamic analysis of dwave functions '''


# Define the problem as a Python dictionary
def problemDefinition():
    a = {('B','B'): 1,
        ('K','K'): 1,
        ('A','C'): 2,
        ('A','K'): -2,
        ('B','C'): -2}
    return a

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_qubo(problemDefinition(),
                                 num_reads = 10,
                                 label='Example - Simple Ocean Programs: QUBO')
print(sampleset)

dwave.inspector.show(sampleset)
